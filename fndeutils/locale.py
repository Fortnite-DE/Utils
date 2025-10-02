from __future__ import annotations

import os
import pathlib
from collections.abc import Callable
from datetime import date, datetime

import babel.core
import fortnite_api
from babel.dates import format_date, format_datetime
from babel.numbers import format_compact_decimal, format_decimal
from discord import app_commands
from redbot.core.i18n import get_babel_locale as red_get_babel_locale, get_locale

__all__ = (
    "Locale",
    "create_locale_str_factory",
    "get_babel_locale",
    "get_game_language",
)


class Locale(babel.core.Locale):
    def format_number(self, number: int | float, compact: bool = False) -> str:
        if compact:
            return format_compact_decimal(number, locale=self, fraction_digits=1)
        return format_decimal(number, locale=self)

    def get_day(self, day: int, type_: str = "wide") -> str:
        # long = 1 January 2020
        # short = 01/01/20
        return self.days["format"][type_][day]

    def format_date(self, date_: date | datetime, format_="medium") -> str:
        f = format_datetime if isinstance(date_, datetime) else format_date
        return f(date_, format_, locale=self)


def get_babel_locale() -> Locale:
    locale = red_get_babel_locale()
    return Locale(locale.language, locale.territory)


def get_game_language() -> fortnite_api.GameLanguage:
    code = get_locale()
    try:
        gl = fortnite_api.GameLanguage(code)
    except ValueError:
        try:
            gl = fortnite_api.GameLanguage(code[:2])
        except ValueError:
            gl = fortnite_api.GameLanguage.ENGLISH
    return gl


def create_locale_str_factory(
    name: str, file_location: str | pathlib.Path | os.PathLike
) -> Callable[[str], app_commands.locale_str]:
    def _locale_str(untranslated: str) -> app_commands.locale_str:
        return app_commands.locale_str(
            untranslated, name=name, file_location=file_location
        )

    return _locale_str
