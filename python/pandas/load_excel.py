# KEYS=[python pandas excel xls]
# requires=[openpyxl]

import pandas as pd
from pandas import DataFrame


def open_excel(file_name: str, header: int) -> DataFrame:
    """
    file_name: the file name that is an excel file.
    header: the starting row where the column names are found, the first row is 0
    """
    engine = "openpyxl" if file_name.endswith(".xlsx") else "xlrd"

    with open(file_name, 'rb') as io:
        df = pd.read_excel(io, engine=engine, header=header)

    return df
