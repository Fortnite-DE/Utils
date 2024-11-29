from datetime import datetime, time, timedelta

import pytz
from babel.dates import format_timedelta
from redbot.core.i18n import get_babel_locale


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


def humanize_timedelta(timedelta_: timedelta, include_time: bool = False, format_: str = 'long'):
    seconds = abs(timedelta_.total_seconds())
    
    periods = [
        ('years', 60 * 60 * 24 * 365, lambda x: x),
        ('months', 60 * 60 * 24 * 30, lambda x: x),
        ('weeks', 60 * 60 * 24 * 7, lambda x: x),
        ('days', 60 * 60 * 24, lambda x: x),
    ]

    time_periods = [
        ('hours', 60 * 60, lambda x: x),
        ('minutes', 60, lambda x: x),
    ]

    if include_time or timedelta_.days == 0:
        periods += time_periods

    strings = []
    for period_name, period_seconds, format_func in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            if period_value == 0:
                continue
            strings.append(
                format_timedelta(
                    timedelta(**{period_name: format_func(period_value)}),
                    threshold=1,
                    format=format_,
                    locale="de_DE",
                )
            )
    return ' '.join(strings)
