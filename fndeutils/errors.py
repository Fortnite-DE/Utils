from __future__ import annotations

from redbot.core import commands

__all__ = [
    "BotMissingCog",
    "InvalidPlayerName",
]


class BotMissingCog(commands.CheckFailure):
    def __init__(self, missing_cogs: list[str], *args):
        self.missing_cogs = missing_cogs

        if len(missing_cogs) > 2:
            fmt = "{}, and {}".format(", ".join(missing_cogs[:-1]), missing_cogs[-1])
        else:
            fmt = " and ".join(missing_cogs)
        message = f"Bot requires {fmt} cog(s) to run this command."
        super().__init__(message, *args)


class InvalidPlayerName(Exception):
    pass
