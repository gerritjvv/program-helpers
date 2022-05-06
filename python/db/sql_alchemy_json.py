from sqlalchemy import text

from python.db.paginate import Session


def filter_with_text(session: Session, entity):
    return session.query(entity).filter(text("CAST(json_field->>'id' AS INTEGER) == 1"))


def filter_with_as_string(session: Session, entity):
    return session.query(entity).filter(entity.json_field['id'].as_string() == '1')
