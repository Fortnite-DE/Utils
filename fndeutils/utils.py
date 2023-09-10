from fortnite_api import GameLanguage
from redbot.core.i18n import get_locale


def unpack_error(e: Exception) -> Exception:
    if hasattr(e, 'original'):
        return unpack_error(e.original)
    return e


def get_game_locale() -> GameLanguage:
    code = get_locale()
    try:
        gl = GameLanguage(code)
    except ValueError:
        try:
            gl = GameLanguage(code[:2])
        except ValueError:
            gl = GameLanguage.ENGLISH
    return gl
