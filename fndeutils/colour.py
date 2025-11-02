from __future__ import annotations

from typing import Self

import discord

__all__ = ["Colour"]


class Colour(discord.Colour):
    @classmethod
    def error(cls) -> Self:
        return cls.dark_red()

    @classmethod
    def success(cls) -> Self:
        return cls.green()

    @classmethod
    def deleted(cls) -> Self:
        return cls.dark_blue()

    @classmethod
    def info(cls) -> Self:
        return cls.from_rgb(255, 255, 255)

    @classmethod
    def warning(cls) -> Self:
        return cls.gold()
