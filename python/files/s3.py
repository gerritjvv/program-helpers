# KEYS = [boto3 python s3 upload list ieterate file]
from typing import IO

import boto3


def upload_to_s3(file: str, bucket: str, key: str):
    s3_client = boto3.client('s3')

    s3_client_response = s3_client.upload_file(file, bucket, key)
    print(s3_client_response)


def list_s3_files(bucket: str):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    for obj in bucket.objects.all():
        yield obj.key


# filtering is done on the server side and we don't have to download
# all of the keys
def list_s3_files_filter(bucket: str, prefix: str):
    s3 = boto3.client('s3')
    kwargs = {'Bucket': bucket, 'Prefix': prefix}
    while True:
        resp = s3.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            yield obj['Key']

        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break


def open_s3_file(region, bucket_name: str, file_name: str) -> IO:
    s3 = boto3.resource("s3", region_name=region)
    obj = s3.Object(bucket_name=bucket_name, key=file_name)

    return obj.get()['Body']


for key in list_s3_files('mybucket'):
    print(key)
