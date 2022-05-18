from typing import Any, Dict, List

from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.engine.row import RowMapping


def select(session:Session, query:str, parameters:Dict[str, Any]) -> List[RowMapping]:
    """
    Returns [{<col_name>:<col-data>, ...}, ...]
    """
    return session.execute(text(query), parameters).mappings().all()