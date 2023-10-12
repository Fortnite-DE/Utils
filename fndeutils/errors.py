from typing import List

from redbot.core.commands import commands


class BotMissingCog(commands.CheckFailure):
    def __init__(self, missing_cogs: List[str], *args):
        self.missing_cogs = missing_cogs

        if len(missing_cogs) > 2:
            fmt = '{}, and {}'.format(', '.join(missing_cogs[:-1]), missing_cogs[-1])
        else:
            fmt = ' and '.join(missing_cogs)
        message = 'Bot requires {} cog(s) to run this command.'.format(fmt)
        super().__init__(message, *args)


class InvalidPlayerName(Exception):
    pass
