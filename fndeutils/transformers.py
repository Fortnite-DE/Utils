import asyncio
from contextlib import suppress
from typing import TYPE_CHECKING, List

import async_timeout
import discord
import fortnitepy
from discord import app_commands
from redbot.core import commands

from .errors import BotMissingCog, InvalidPlayerName

if TYPE_CHECKING:
    from redbot.core.bot import Red


class CustomEmojiTransformer(app_commands.Transformer):
    async def transform(self, interaction: discord.Interaction["Red"], value: str, /) -> discord.PartialEmoji:
        ctx = commands.Context.from_interaction(interaction)
        emoji = await commands.PartialEmojiConverter().convert(ctx, value)
        return emoji


class PlayerTransformer(app_commands.Transformer):
    async def autocomplete(self, interaction: discord.Interaction["Red"], current: str) -> List[app_commands.Choice]:
        return (await self._get_player_options(interaction, current))[:25]

    async def _get_player_options(
        self, interaction: discord.Interaction["Red"], current: str
    ) -> List[app_commands.Choice]:
        epic_cog = interaction.client.get_cog('Epic')
        if not epic_cog or len(epic_cog.clients) == 0:
            return [app_commands.Choice(name=current, value=current)]

        client = epic_cog.clients[0]

        options = []
        if client.is_display_name(current):
            players = None
            with suppress(asyncio.TimeoutError):
                async with async_timeout.timeout(2.5):
                    players = await client.search_users(current, fortnitepy.UserSearchPlatform.EPIC_GAMES)
            if players is None:
                return [app_commands.Choice(name=current, value=current)]
            options = self.fmt_options(current, players)
        elif client.is_id(current):
            player = await client.fetch_user(current)
            if player:
                options.append(app_commands.Choice(name=str(player), value=player.id))
        return options

    def fmt_options(
        self,
        current: str,
        players: List[fortnitepy.User],
    ) -> List[app_commands.Choice]:
        options = []
        for player in players:
            displayed_name = str(player)
            if current.lower() not in displayed_name.lower():
                external_name = None
                for external_auth in player.external_auths:
                    if not external_auth.external_display_name:
                        continue
                    if current.lower() in external_auth.external_display_name.lower():
                        external_auth_type = (
                            external_auth.type.replace('xbl', 'XBox').replace('psn', 'Playstation').capitalize()
                        )
                        external_name = f'{external_auth.external_display_name} ({external_auth_type})'
                if not external_name:
                    continue
                displayed_name = external_name
            options.append(app_commands.Choice(name=displayed_name, value=player.id))
        return options

    async def transform(self, interaction: discord.Interaction["Red"], value: str) -> fortnitepy.User:
        epic_cog = interaction.client.get_cog('Epic')
        if not epic_cog or len(epic_cog.clients) == 0:
            raise BotMissingCog(['Epic'])

        client = epic_cog.clients[0]

        if client.is_id(value):
            player = await client.fetch_user(value)
            if not player:
                raise fortnitepy.NotFound()
            return player

        if not client.is_display_name(value):
            raise InvalidPlayerName()

        players = [await client.fetch_user_by_display_name(value)]
        players = players[:15]
        if len(players) == 1:
            if not players[0]:
                raise fortnitepy.NotFound()
            return players[0]
