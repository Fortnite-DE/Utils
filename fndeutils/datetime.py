from datetime import datetime, time

import pytz


def to_utc_datetime(local_dt: datetime, timezone: str) -> datetime:
    """Converts a local datetime object to UTC timezone."""
    tz = pytz.timezone(timezone)
    dt_timezone = tz.localize(dt=local_dt)
    return dt_timezone.astimezone(pytz.utc)


def to_utc_time(local_t: time, timezone: str) -> time:
    """Converts a local time object to UTC timezone."""
    local_dt = datetime.combine(datetime.now().date(), local_t)
    dt_utc = to_utc_datetime(local_dt, timezone)
    return dt_utc.time()
