from __future__ import annotations

import asyncio
import os
from collections.abc import Callable
from pathlib import Path

import discord
from discord import app_commands
from fortnite_api import GameLanguage
from redbot.core.i18n import get_locale

__all__ = (
    "unpack_error",
    "get_game_language",
    "create_locale_str_factory",
    "defer_interaction",
    "send_respond",
    "edit_respond",
)


def unpack_error(e: BaseException) -> Exception:
    if hasattr(e, "original"):
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
        return app_commands.locale_str(
            untranslated, name=name, file_location=file_location
        )

    return _locale_str


async def defer_interaction(interaction: discord.Interaction):
    await asyncio.sleep(
        2 - (discord.utils.utcnow() - interaction.created_at).total_seconds()
    )
    if not interaction.response.is_done():
        await interaction.response.defer()


async def send_respond(interaction: discord.Interaction, **kwargs):
    if not interaction.response.is_done():
        try:
            return await interaction.response.send_message(**kwargs)
        except discord.HTTPException as e:
            if e.code != 40060:
                raise e
    await interaction.followup.send(**kwargs)


async def edit_respond(interaction: discord.Interaction, **kwargs):
    if not interaction.response.is_done():
        try:
            return await interaction.response.edit_message(**kwargs)
        except discord.HTTPException as e:
            if e.code != 40060:
                raise e
    await interaction.edit_original_response(**kwargs)
