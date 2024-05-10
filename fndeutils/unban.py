import discord
from typing import Optional


TIME_AFTER_BAN = 7 * 24 * 60 * 60  # 7 Tage
TIME_AFTER_TRY = 180 * 24 * 60 * 60  # 180 Tage
VOTE_TIME = 7 * 24 * 60 * 60  # 7 Tage
VOTE_OVERTIME = 14 * 24 * 60 * 60  # 14 Tage
TIME_ON_UNBAN_SERVER = 2 * 24 * 60 * 60  # 2 Tage


def generate_google_form_link(user: Optional[discord.User] = None) -> str:
    return (
        (
            "https://docs.google.com/forms/d/e/1FAIpQLSf7tmKSzGPJhCtE--QHuQy950BB-siueoR0Wi9DhL9oO4JbTQ/viewform"
            f"?&entry.1499245679={user}&entry.387590345={user.id}"
        )
        if user
        else "https://fn-discord.de/entbannung"
)
