# KEYS=[python postgres sqlalchemy pagination]

import math
from dataclasses import dataclass
from typing import Optional, List, Union, Any

from sqlalchemy import create_engine, Integer, String, Column, text
from sqlalchemy.engine import ResultProxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

########################################################################################################################
##                DB and test setup
########################################################################################################################

engine = create_engine('sqlite://')

Session = sessionmaker(engine)
session = Session()

session.execute("""
    CREATE TABLE company (name varchar(255), id integer);
    """)
session.commit()


@dataclass
class Company:
    id: int
    name: str


companies = [Company(id=i, name=f"Name: {i}") for i in range(100)]

for company in companies:
    session.execute("""
        INSERT INTO company (name, id) VALUES(:name, :id)
        """, {'id': company.id, 'name': company.name})

session.commit()


########################################################################################################################
##               Pagination with raw sql queries, tested on postgresql and sqllite
########################################################################################################################

@dataclass
class Pagination:
    items: Union[ResultProxy, List[Any]]  # if using paginate_raw thisis a ResultProxy otherwise its a List of entities
    page: int
    pages: int
    page_size: int
    total: int

    def next_page(self) -> Optional[int]:
        return self.page + 1 if self.has_next() else None

    def previous_page(self) -> Optional[int]:
        return self.page - 1 if self.has_previous() else None

    def has_previous(self):
        return self.page > 1;

    def has_next(self):
        previous_items = (self.page - 1) * self.page_size
        row_count = self.items.rowcount if isinstance(self.items, ResultProxy) else len(self.items)
        return previous_items + row_count < self.total


def paginate_raw(session: Session, query: str, page: int, page_size: int):
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if page_size <= 0:
        raise AttributeError('page_size needs to be >= 1')

    offset = (page - 1) * page_size
    final_query = f"{query} LIMIT {page_size} OFFSET {offset}"

    items = session.execute(text(final_query))
    total = session.execute(text(f"SELECT count(*) from ({query}) a")).first()[0]

    return Pagination(items=items, page=page, page_size=page_size, total=total,
                      pages=int(math.ceil(total / float(page_size))))


def get_companies_raw(session: Session, per_page: int, current_page: int = 1) -> Pagination:
    return paginate_raw(session=session, query="select * from company", page=current_page, page_size=per_page)


########################################################################################################################
##               Pagination with sqlalchmey orm
########################################################################################################################


def paginate(query, page, page_size):
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if page_size <= 0:
        raise AttributeError('page_size needs to be >= 1')

    items = query.limit(page_size).offset((page - 1) * page_size).all()
    total = query.order_by(None).count()

    return Pagination(items=items, page=page, page_size=page_size, total=total,
                      pages=int(math.ceil(total / float(page_size))))


Base = declarative_base()


class CompanyEntity(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def get_companies(session: Session, per_page: int, current_page: int = 1) -> Pagination:
    return paginate(session.query(CompanyEntity), page=current_page, page_size=per_page)
