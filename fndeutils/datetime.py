from __future__ import annotations

from datetime import datetime, time, timedelta
from typing import Literal

import pytz
from babel.dates import format_timedelta
from redbot.core.i18n import get_babel_locale

__all__ = [
    "to_utc_datetime",
    "to_utc_time",
    "humanize_timedelta",
]


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


def humanize_timedelta(
    timedelta_: timedelta,
    include_time: bool = False,
    format_: Literal["narrow", "short", "medium", "long"] = "long",
):
    seconds = abs(timedelta_.total_seconds())
    periods = [
        ("days", 60 * 60 * 24 * 365, lambda x: x * 365),  # years
        ("days", 60 * 60 * 24 * 30, lambda x: x * 30),  # months
        ("days", 60 * 60 * 24 * 7, lambda x: x * 7),  # weeks
        ("days", 60 * 60 * 24, lambda x: x),
    ]

    time_periods = [
        ("hours", 60 * 60, lambda x: x),
        ("minutes", 60, lambda x: x),
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
                    locale=get_babel_locale(),
                )
            )
    return " ".join(strings)
