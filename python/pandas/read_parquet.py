# KEYS = [parquet read s3]
# requies pyarray and s3fs
import pandas as pd

df = pd.read_parquet("s3://<bucket>/<file>.parquet")


