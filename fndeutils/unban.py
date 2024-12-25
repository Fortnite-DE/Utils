import re
from typing import Optional

import discord

TIME_AFTER_BAN = 7 * 24 * 60 * 60  # 7 Tage
TIME_AFTER_TRY = 180 * 24 * 60 * 60  # 180 Tage
VOTE_TIME = 7 * 24 * 60 * 60  # 7 Tage
VOTE_OVERTIME = 14 * 24 * 60 * 60  # 14 Tage
TIME_ON_UNBAN_SERVER = 2 * 24 * 60 * 60  # 2 Tage


def generate_google_form_link(ban_entry: Optional[discord.BanEntry] = None) -> str:
    if not ban_entry:
        return "https://fn-discord.de/entbannung"

    reason = ""
    if ban_entry.reason:
        reason: str = ban_entry.reason

        reason_match = re.search(r"(?:Grund|Reason): (.+)", reason)
        if reason_match:
            reason = reason_match.group(1)
        else:
            new_search = re.search(r":mod:(.*?):reason:(.*)", reason)
            if new_search:
                ### siehe ban_appeals/ban_appeals.py L543
                # mod = self.server.fn_server.get_member(int(new_search.group(1)))
                # if mod:
                #     request.manually_decided = mod
                reason = new_search.group(2)

    reason = reason.replace(" ", "%20")

    return (
        "https://docs.google.com/forms/d/e/1FAIpQLSf7tmKSzGPJhCtE--QHuQy950BB-siueoR0Wi9DhL9oO4JbTQ/viewform"
        f"?&entry.1499245679={ban_entry.user}&entry.387590345={ban_entry.user.id}"
        f"{f'&entry.573671189={reason}'}"
    )
