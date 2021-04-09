#!/usr/bin/env python3
# KEYS=[python datetime format parse]

from datetime import datetime
import dateutil.parser


def format(d: datetime) -> str:
    return d.strftime("%Y/%m/%d, %H:%M:%S")


print(format(datetime.utcnow()))


def parse_date(d: str) -> datetime:
    return dateutil.parser.parse(d)
