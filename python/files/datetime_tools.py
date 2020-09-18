#!/usr/bin/env python3
# KEYS=[python datetime format]

from datetime import datetime


def format(d: datetime) -> str:
    return d.strftime("%Y/%m/%d, %H:%M:%S")


print(format(datetime.utcnow()))
