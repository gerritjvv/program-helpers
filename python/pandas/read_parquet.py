# KEYS = [parquet read s3]
# requires pyarray and s3fs
import pandas as pd

df = pd.read_parquet("s3://<bucket>/<file>.parquet")


