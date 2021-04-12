# KEYS=[python pandas remove nan clean data]

import pandas as pd

df = pd.DataFrame({"a": None}, {"a": 1})
#     a
# 0  NaN
# 1  1.0

df = df.where(df.isnull(), None)

#      a
# 0  None
# 1   1.0
