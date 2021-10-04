from datetime import datetime

# pip install croniter
from time import timezone

import croniter as croniter


def utcnow_tz() -> datetime:
    return datetime.now(timezone.utc)


cron_schedule = croniter("cron schedule here", utcnow_tz())
next_date_to_execute = cron_schedule.get_next(datetime)
