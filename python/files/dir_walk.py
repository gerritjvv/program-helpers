#!/usr/bin/env python

import os
import sys

dir_input = sys.argv[1]


def get_files(dir: str):
    for root, dir_names, file_names in os.walk(dir):
        for file in file_names:
            yield os.path.join(root, file)


for file in get_files(dir_input):
    print(file)
