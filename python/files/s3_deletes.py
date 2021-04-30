# KEYS=[python s3 bucket expire cleanup]


"""
This is an example script that takes a bucket table partition structure with:

 <table>/<year>/<month>/<day>/[... more folders or files]

Then deletes whole folders based on their date from <year>/<month>/<day>

It can be easily adapted to different partition strategies e.g

<table>/date=<year>-<month>-<day>  etc.

Please note that if you need to cleanout data automatically from a bucket, bucket lifecycle policies work better.
"""
from datetime import datetime, timedelta
from typing import List

import boto3

client = boto3.client("s3")


def date_from_path(path: str) -> List[str]:
    """
    Takes a path like bla/number1/number2  and returns [number1, number2]
    """
    parts = [p for p in path.split('/') if p.isnumeric()]

    return parts


def ls(bucket: str, prefix: str):
    """
    Returns the prefixes used in a bucket e.g the <table>/<year>/<month>/<day> folders
    """
    paginator = client.get_paginator('list_objects')
    result = paginator.paginate(Bucket=bucket, Prefix=prefix, Delimiter='/')
    for prefix in result.search('CommonPrefixes'):
        if prefix and 'Prefix' in prefix:
            yield prefix['Prefix']


def list_dates(bucket: str, table: str) -> List[str]:
    """
    Expects a partition format <table>/<year>/<month>/<day> and
    returns the different f"{table}/{year}/{month}/{day}" strings in the bucket.

    The method is purposefully not trying to be clever to make it easier to read.
    """
    table = table.rstrip('/')

    years_paths = list(ls(bucket, f"{table}/"))

    paths = []
    for year_path in years_paths:
        year_parts = date_from_path(year_path)
        print(f"{year_path} from {year_parts}")

        if len(year_parts) > 1:
            print(f"Skipping {year_path}")
            continue

        year = year_parts[0]
        month_paths = list(ls(bucket, f"{table}/{year}/"))

        for month_path in month_paths:
            month_parts = date_from_path(month_path)
            if len(month_parts) != 2:
                print(f"Skipping {month_path}")
                continue

            month = month_parts[1]

            day_paths = list(ls(bucket, f"{table}/{year}/{month}/"))
            for day_path in day_paths:
                day_parts = date_from_path(day_path)
                if len(day_parts) != 3:
                    print(f"Skipping {day_path}")
                    continue

                day = day_parts[2]
                paths.append(f"{table}/{year}/{month}/{day}")

    return paths


def extract_date(path: str):
    """
    Take the year, month, day from a path and return a datetime object
    """
    year, month, day = date_from_path(path)
    return datetime.strptime(f"{year}/{month}/{day}", '%Y/%m/%d')


def clean_bucket(bucket: str, table: str):
    """
    Takes a bucket and the top level folder, then deletes all folders
    with partitions indicating its older than 6 months
    """
    date_paths = list_dates(bucket, table)

    today = datetime.utcnow()
    historic_date = today - timedelta(days=(30 * 6))

    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(bucket)

    date_paths = [dp for dp in date_paths if extract_date(dp) < historic_date]
    print(date_paths)
    for date_path in date_paths:
        if extract_date(date_path) < historic_date:
            print(f"delete s3  path: {date_path}")
            s3_bucket.objects.filter(Prefix=f"{date_path}/").delete()


def delete_known_tables():
    """
    A driver method that can be used to delete different top level folders in a bucket
    """
    tables = ["myfolder/"]
    for table in tables:
        clean_bucket(bucket="mybucket", table=table)
