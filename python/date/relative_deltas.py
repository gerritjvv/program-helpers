#!/usr/bin/env python3
# KEY = [python delta previous month week day year relative]

import datetime

# see https://labix.org/python-dateutil#head-ba5ffd4df8111d1b83fc194b97ebecf837add454

import dateutil.relativedelta

d = datetime.datetime.strptime("2021-07-08", "%Y-%m-%d")
d2 = d - dateutil.relativedelta.relativedelta(months=1)
