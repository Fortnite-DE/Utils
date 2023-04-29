from typing import List

import discord


class PaginationView(discord.ui.View):
    def __init__(self, embeds: List[discord.Embed], start_page: int = 0, **kwargs):
        super(PaginationView, self).__init__(**kwargs)
        self.embeds: List[discord.Embed] = embeds
        self.current_page: int = start_page

    @classmethod
    async def start(
            cls,
            interaction: discord.Interaction,
            embeds: List[discord.Embed],
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
            self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        self.current_page = 0
        self._update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page], view=self
        )

    @discord.ui.button(emoji="⬅️")
    async def prev_page(
            self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        self.current_page -= 1
        self._update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page], view=self
        )

    @discord.ui.button(emoji="➡️")
    async def next_page(
            self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        self.current_page += 1
        self._update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page], view=self
        )

    @discord.ui.button(emoji="⏭️")
    async def last_page(
            self, button: discord.ui.Button, interaction: discord.Interaction
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
