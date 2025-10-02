from __future__ import annotations

from typing import TYPE_CHECKING, Any, Self

import discord
from redbot.core import commands
from redbot.core.i18n import Translator

from .colour import Colour

if TYPE_CHECKING:
    from redbot.core.bot import Red

__all__ = [
    "BaseView",
    "BasicResponseView",
    "InteractiveView",
    "PaginationView",
    "View",
    "Modal",
    "EmbedPaginationView",
]

_t = Translator("FndeUtils", __file__)

Page = list[discord.ui.Item]


class BaseView(discord.ui.LayoutView):
    async def on_error(
        self,
        interaction: discord.Interaction,
        error: Exception,
        item: discord.ui.Item[Self],
        /,
    ) -> None:
        interaction.client.dispatch(
            "error", "on_modal_interaction", self, interaction, error=error
        )


class BasicResponseView(BaseView):
    def __init__(
        self,
        title: str,
        text: str,
        colour: Colour | None = None,
        thumbnail: str | discord.File | discord.UnfurledMediaItem | None = None,
    ) -> None:
        super().__init__()
        child = discord.ui.TextDisplay(f"# {title}\n{text}")
        if thumbnail:
            child = discord.ui.Section(
                child,
                accessory=discord.ui.Thumbnail(thumbnail),
            )
        self.add_item(discord.ui.Container(child, accent_colour=colour))


class InteractiveView(BaseView):
    def __init__(
        self,
        ref: commands.Context | discord.Interaction | discord.Message,
        *,
        owner: discord.User | discord.Member | None = None,
        owner_only: bool = True,
        timeout: float | None = 300,
    ) -> None:
        super().__init__(timeout=timeout)
        ref_owner, messageable = None, None
        if isinstance(ref, commands.Context):
            ref_owner = ref.author
            messageable = ref.interaction or ref.message
        elif isinstance(ref, discord.Interaction):
            ref_owner = ref.user
            messageable = ref
        elif isinstance(ref, discord.Message):
            ref_owner = ref.author
            messageable = ref
        else:
            raise TypeError("ref must be a commands.Context or discord.Interaction")

        self.messageable: discord.Interaction | discord.Message = messageable
        self.owner: discord.User | discord.Member = owner or ref_owner
        self.owner_only: bool = owner_only

    async def interaction_check(self, interaction: discord.Interaction, /) -> bool:
        if self.owner_only and self.owner and interaction.user != self.owner:
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.description = _t("You are not authorized to interact with this menu.")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return False
        return True

    async def on_timeout(self) -> None:
        for item in self.walk_children():
            if item.is_dispatchable() and hasattr(item, "disabled"):
                item.disabled = True  # type: ignore[attr-defined]
        await self._edit_message(view=self)

    async def _edit_message(self, **kwargs) -> None:
        if isinstance(self.messageable, discord.Interaction):
            await self.messageable.edit_original_response(**kwargs)
        elif isinstance(self.messageable, discord.Message):
            await self.messageable.edit(**kwargs)


class PaginationView(InteractiveView):
    def __init__(
        self,
        pages: list[Page],
        ref: commands.Context,
        *,
        start_page: int = 0,
        **kwargs,
    ) -> None:
        super().__init__(ref, **kwargs)
        self.pages: list[Page] = pages
        self.current_page: int = start_page
        self._original_components = self.children.copy()

    @classmethod
    async def start(
        cls,
        pages: list[Page],
        ctx: commands.Context,
        *,
        edit: bool = False,
        ephemeral: bool = False,
        start_page: int = 0,
        **kwargs,
    ) -> Self:
        if len(pages) == 0:
            raise ValueError("No pages provided")
        if start_page < 0 or start_page >= len(pages):
            raise ValueError("start_page must be between 0 and the number of pages - 1")
        view = cls(pages, ctx, start_page=start_page, **kwargs)
        view._build_page()
        if edit:
            await view._edit_message(view=view, ephemeral=ephemeral)
        else:
            await ctx.send(view=view, ephemeral=ephemeral)
        return view

    navigation_row = discord.ui.ActionRow()

    @navigation_row.button(emoji="⏮️")
    async def first_page(self, interaction: discord.Interaction, _) -> None:
        self.current_page = 0
        self._build_page()
        await interaction.response.edit_message(view=self)

    @navigation_row.button(emoji="⬅️")
    async def prev_page(self, interaction: discord.Interaction, _) -> None:
        self.current_page -= 1
        self._build_page()
        await interaction.response.edit_message(view=self)

    @navigation_row.button(emoji="➡️")
    async def next_page(self, interaction: discord.Interaction, _) -> None:
        self.current_page += 1
        self._build_page()
        await interaction.response.edit_message(view=self)

    @navigation_row.button(emoji="⏭️")
    async def last_page(self, interaction: discord.Interaction, _) -> None:
        self.current_page = len(self.pages) - 1
        self._build_page()
        await interaction.response.edit_message(view=self)

    def _build_page(self) -> None:
        self.clear_items()
        for item in self.pages[self.current_page]:
            self.add_item(item)

        # No need for navigation buttons
        if len(self.pages) == 1:
            return

        for item in self._original_components:
            self.add_item(item)

        back_buttons = [self.first_page, self.prev_page]
        forward_buttons = [self.next_page, self.last_page]
        if self.current_page == 0:  # First page
            for button in back_buttons:
                button.disabled = True
            for button in forward_buttons:
                button.disabled = False
        elif self.current_page == len(self.pages) - 1:  # Last page
            for button in back_buttons:
                button.disabled = False
            for button in forward_buttons:
                button.disabled = True
        else:
            for button in back_buttons + forward_buttons:
                button.disabled = False


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


class EmbedPaginationView(View):
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
            await interaction.edit_original_response(embed=embeds[0], view=view)
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
