#!/usr/bin/env python
# KEYS=[zip]

import os, sys
from typing import Any
from zipfile import ZipFile, ZipInfo

# the destination dir to extract files to
dest_dir = sys.argv[1]
# the zip file to extract
file_name = sys.argv[2]


def all_files(file_name):
    with ZipFile(file_name, 'r') as zip:
        for file in zip.filelist:
            yield file


def get_file_path(file: Any) -> str:
    file_path = str(file)

    if isinstance(file, ZipInfo):
        zip_info: ZipInfo = file
        file_path = zip_info.filename

    return file_path


def extract_file(dest_dir: str, src_file: Any, file: Any):
    """
    Extract a file to dest_dir using the src_file name instead of the original directory it was placed in
    i.e if dest_dir is /tmp/data/  and the file a/b/c//data.csv the file will go to /tmp/data/data.csv
    """
    file_path = get_file_path(file)

    if isinstance(file, ZipInfo):
        zip_info: ZipInfo = file
        file_name = file_path.split("/")[-1:]

        with ZipFile(src_file, "r") as src_zip:
            zip_info.filename = file_name[0]
            src_zip.extract(member=zip_info, path=dest_dir)
    else:
        raise Exception(f"expecing a zipinfo file here but got {file}")


os.makedirs(dest_dir, exist_ok=True)

for file in all_files(file_name):
    print(file)
    if not file.is_dir():
        extract_file(dest_dir, file_name, file)
