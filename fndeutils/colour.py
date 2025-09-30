from __future__ import annotations

import discord

__all__ = ["Colour"]


class Colour(discord.Colour):
    @classmethod
    def error(cls) -> discord.Colour:
        return cls.dark_red()

    @classmethod
    def success(cls) -> discord.Colour:
        return cls.green()

    @classmethod
    def deleted(cls) -> discord.Colour:
        return cls.dark_blue()

    @classmethod
    def info(cls) -> discord.Colour:
        return cls.from_rgb(255, 255, 255)

    @classmethod
    def warning(cls) -> discord.Colour:
        return cls.gold()
