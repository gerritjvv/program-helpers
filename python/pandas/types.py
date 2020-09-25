#!/usr/bin/env python3
# KEYS = [pandas types single type]
import pandas as pd

df = pd.DataFrame({'float': [1.0],
                   'int': [1],
                   'datetime': [pd.Timestamp('20180310')],
                   'string': ['foo']})
# all column types
df.dtypes

# single column's type
df.dtypes['col-name']
