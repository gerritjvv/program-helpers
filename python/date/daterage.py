#!/usr/bin/env python3
# KEY = [python datetime range daterange]

from datetime import datetime, timedelta


def date_range(start_date: datetime, end_date: datetime):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
