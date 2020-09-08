#!/usr/bin/env python
# KEYS=[excel csv pandas]

import pandas as pd


def transform_xlsx_to_csv(file_path: str):
    csv_file_path = file_path.split("\.")[0] + ".csv"

    df = pd.read_excel(file_path)
    df.to_csv(csv_file_path, sep=",", index=False)
