import os
from pathlib import Path
from typing import Callable, TYPE_CHECKING

from discord import app_commands
from fortnite_api import GameLanguage
from redbot.core.i18n import get_locale

if TYPE_CHECKING:
    from redbot.core.bot import Red


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


async def get_command_mention(bot: "Red", name: str) -> str:
    name = name.lower()
    name_split = name.split(' ')
    if not name_split:
        return f'`/{name}`'
    commands = await bot.list_enabled_app_commands()
    for command_name, command_id in commands['slash'].items():
        if command_name != name_split[0]:
            continue
        return f'</{name}:{command_id}>'
    return f'`/{name}`'
