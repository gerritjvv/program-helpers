# KEYS=[python postgres sqlalchemy pagination]

import math
from dataclasses import dataclass
from typing import Optional, List, Union, Any

from sqlalchemy import create_engine, Integer, String, Column, text
from sqlalchemy.engine import ResultProxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


def copy_from(session:Session):

    # this will get a raw cursor bounded to the current transaction
    raw_cursor = session.connection().connection.cursor()

    # copy the gzip csv file into the temp table
    # raw_cursor.copy_from(btsio, temp_table_name, sep="\001", columns=csv_columns)
