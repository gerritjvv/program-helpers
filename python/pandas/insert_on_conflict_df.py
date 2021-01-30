import sqlalchemy
from sqlalchemy.dialects.postgresql import insert

Table = None # your sqlalchmey table model
records = [{'date': '2021-01-1', 'a': 12, 'b':300}]
index = ['date', 'a', 'b']

session = None # your sqlalchemy session, connection or engine

for vals in records:
    insert_stmt = sqlalchemy.dialects.postgresql.insert(Table,
                                                        bind=session).values(vals)
    upsert_stmt = insert_stmt.on_conflict_do_update(
            index_elements=index,
            set_=vals
    )

    session.execute(upsert_stmt)