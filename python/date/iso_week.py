#!/usr/bin/env python3
# KEY = [python datetime range daterange week iso month]

import enum
import datetime
import calendar
from typing import Tuple


class Week(enum.Enum):
    MONDAY = 1


def week_of_year(d: datetime.datetime) -> int:
    return int(d.strftime("%W"))


def iso_week_start_end_dates(year, week, week_start=Week.MONDAY) -> Tuple[datetime.datetime, datetime.datetime]:
    """
    Return the start and end date of an iso week
    Iso weeks Monday = 1 Sunday is 6.

    """
    week = int(week)
    assert 1 <= week <= 53

    week_padded = str(week) if week > 9 else f"0{week}"

    start = datetime.datetime.strptime(f"{year}-W{week_padded}-{week_start.value}", "%Y-W%W-%w")

    return start, start + datetime.timedelta(days=6)


def iso_month_start_end_dates(year, month) -> Tuple[datetime.datetime, datetime.datetime]:
    """
    Return the start and end date of an iso month
    """
    year = int(year)
    month = int(month)
    assert 1 <= month <= 12
    start = datetime.datetime(year=year, month=month, day=1, hour=0, minute=0, second=0, microsecond=0)

    day_end_of_month = calendar.monthrange(year, month)[1]

    return start, start + datetime.timedelta(days=day_end_of_month - 1)
