import os
from pathlib import Path
from typing import Callable

from discord import app_commands
from fortnite_api import GameLanguage
from redbot.core.i18n import get_locale


def unpack_error(e: Exception) -> Exception:
    if hasattr(e, 'original'):
        return unpack_error(e.original)
    return e


def get_game_language() -> GameLanguage:
    code = get_locale()
    try:
        gl = GameLanguage(code)
    except ValueError:
        try:
            gl = GameLanguage(code[:2])
        except ValueError:
            gl = GameLanguage.ENGLISH
    return gl


def create_locale_str_factory(
    name: str, file_location: str | Path | os.PathLike
) -> Callable[[str], app_commands.locale_str]:
    def _locale_str(untranslated: str) -> app_commands.locale_str:
        return app_commands.locale_str(untranslated, name=name, file_location=file_location)

    return _locale_str
