from __future__ import annotations

import asyncio

import discord

__all__ = (
    "unpack_error",
    "defer_interaction",
    "send_respond",
    "edit_respond",
)


def unpack_error(e: BaseException) -> Exception:
    if hasattr(e, "original"):
        return unpack_error(e.original)
    return e


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
