#!/usr/bin/env python3
# KEYS=[python datetime format parse]

from datetime import datetime
import dateutil.parser


def format(d: datetime) -> str:
    return d.strftime("%Y/%m/%d, %H:%M:%S")


print(format(datetime.utcnow()))


def parse_date(d: str) -> datetime:
    return dateutil.parser.parse(d)


parse_date('2021-04-01')
# datetime.datetime(2021, 4, 1, 0, 0)
parse_date('2021/04/01')
# datetime.datetime(2021, 4, 1, 0, 0)
parse_date('01/04/2021')
# datetime.datetime(2021, 1, 4, 0, 0)
parse_date('01-04-2021')
# datetime.datetime(2021, 1, 4, 0, 0)
parse_date('April 1 2021')
# datetime.datetime(2021, 4, 1, 0, 0)
