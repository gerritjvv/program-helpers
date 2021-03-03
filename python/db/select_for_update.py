# KEYS=[python postgres sqlalchemy locking select update for_for_update]
import sqlalchemy

"""
Use case:
Th1:
  select table1
  do update


Th1:
  select table1
  do update

"""

# see: https://docs.sqlalchemy.org/en/14/orm/query.html
sqlalchemy.orm.Query.with_for_update(read=False, nowait=False, of=None, skip_locked=False, key_share=False)
