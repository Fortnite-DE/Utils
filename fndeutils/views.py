from __future__ import annotations

from typing import TYPE_CHECKING, Any

import discord
from redbot.core.i18n import Translator

if TYPE_CHECKING:
    from redbot.core.bot import Red

_ = Translator("FndeUtils", __file__)


class View(discord.ui.View):
    def __init__(
        self,
        interaction: discord.Interaction | None = None,
        *,
        owner: discord.abc.User | None = None,
        owner_only: bool = True,
        timeout: float | None = 300.0,
    ):
        super().__init__(timeout=timeout)
        self._enabled: bool = interaction is not None
        self.interaction: discord.Interaction | None = interaction
        self.owner: discord.User | None = owner or (
            interaction.user if interaction else None
        )
        self.owner_only: bool = owner_only

    async def on_timeout(self) -> None:
        if not self._enabled:
            return
        for item in self.children:
            if item.is_dispatchable():
                self.remove_item(item)
        await self.interaction.edit_original_response(view=self)

    async def interaction_check(self, interaction: discord.Interaction[Red], /) -> bool:
        if self.owner_only and self.owner and interaction.user != self.owner:
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.description = _("You are not authorized to interact with this menu.")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return False
        return True

    async def on_error(
        self,
        interaction: discord.Interaction[Red],
        error: Exception,
        item: discord.ui.Item[Any],
        /,
    ) -> None:
        interaction.client.dispatch(
            "error", "on_view_interaction", self, item, interaction, error=error
        )


class Modal(discord.ui.Modal):
    async def on_error(
        self, interaction: discord.Interaction, error: Exception, /
    ) -> None:
        interaction.client.dispatch(
            "error", "on_modal_interaction", self, interaction, error=error
        )


class PaginationView(View):
    def __init__(self, embeds: list[discord.Embed], start_page: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.embeds: list[discord.Embed] = embeds
        self.current_page: int = start_page

    @classmethod
    async def start(
        cls,
        interaction: discord.Interaction,
        embeds: list[discord.Embed],
        *,
        start_page: int = 0,
        edit: bool = False,
        ephemeral: bool = False,
        **kwargs,
    ):
        if len(embeds) == 0:
            raise ValueError("No embeds provided")
        view = cls(embeds, start_page, **kwargs) if len(embeds) > 1 else None
        if view:
            if start_page == 0:
                view.first_page.disabled = True
                view.prev_page.disabled = True
            elif start_page == len(embeds) - 1:
                view.next_page.disabled = True
                view.last_page.disabled = True
        if edit:
            await interaction.edit_original_message(embed=embeds[0], view=view)
        else:
            kwargs = dict(embed=embeds[0], ephemeral=ephemeral)
            if view:
                kwargs["view"] = view
            respond = (
                interaction.followup.send
                if interaction.response.is_done()
                else interaction.response.send_message
            )
            await respond(**kwargs)
        return view

    @discord.ui.button(emoji="⏮️")
    async def first_page(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.current_page = 0
        self._update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page], view=self
        )

    @discord.ui.button(emoji="⬅️")
    async def prev_page(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.current_page -= 1
        self._update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page], view=self
        )

    @discord.ui.button(emoji="➡️")
    async def next_page(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.current_page += 1
        self._update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page], view=self
        )

    @discord.ui.button(emoji="⏭️")
    async def last_page(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.current_page = len(self.embeds) - 1
        self._update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page], view=self
        )

    def _update_buttons(self):
        if self.current_page == 0:
            self.first_page.disabled = True
            self.prev_page.disabled = True
            self.last_page.disabled = False
            self.next_page.disabled = False
        elif self.current_page == len(self.embeds) - 1:
            self.first_page.disabled = False
            self.prev_page.disabled = False
            self.last_page.disabled = True
            self.next_page.disabled = True
        else:
            self.first_page.disabled = False
            self.prev_page.disabled = False
            self.last_page.disabled = False
            self.next_page.disabled = False
