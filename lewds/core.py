import discord

from redbot.core.bot import Red
from redbot.core import commands
from redbot.core.i18n import Translator, cog_i18n
from redbot.core.utils.chat_formatting import bold, box, inline

import json
import asyncio
import aiohttp
from random import choice
from typing import Optional, List, Union

from .constants import LEWDS_URL

_ = Translator("lewds", __file__)


@cog_i18n(_)
class Core(commands.Cog):

    __author__ = ["Xanathero", "Xynnix"]
    __version__ = "0.0.3"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    def __init__(self, bot: Red):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """NSFW Image Cog for Lewds API"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    async def _get_others_imgs(self, ctx: commands.Context, url: str = None):
        """Get images from Lewd image APIs."""
        try:
            async with self.session.get(url) as resp:
                if resp.status != 200:
                    await self._api_errors_msg(ctx, error_code=resp.status)
                    return None
                try:
                    data = await resp.json(content_type=None)
                except json.decoder.JSONDecodeError as exception:
                    await self._api_errors_msg(ctx, error_code=exception)
                    return None
            data = dict(img=data)
            return data
        except aiohttp.client_exceptions.ClientConnectionError:
            await self._api_errors_msg(ctx, error_code="JSON decode failed")
            return None

    async def _api_errors_msg(self, ctx: commands.Context, error_code: int = None):
        """Error message when API calls fail."""
        return await ctx.send(
            _("Error when trying to contact image service, please try again later. ")
            + "(Code: {})".format(inline(str(error_code)))
        )

    async def _version_msg(self, ctx: commands.Context, version: str, authors: List[str]):
        """Cog version message."""
        msg = box(
            _("LEWDs cog version: {version}\nAuthors: {authors}").format(
                version=version, authors=", ".join(authors)
            ),
            lang="py",
        )
        return await ctx.send(msg)

    async def _make_embed_other(
        self, ctx: commands.Context, name: str, url: str, arg: str, source: str
    ):
        """Function to make the embed for Lewds APIs images."""
        try:
            data = await asyncio.wait_for(self._get_others_imgs(ctx, url=url), 3)
        except asyncio.TimeoutError:
            await ctx.send("Failed to get image. Please try again later. (Timeout error)")
            return
        if not data:
            return
        em = await self._embed(
            color=0x891193,
            title=(_("Here is your {name} image ...") + " \N{EYES}").format(name=name),
            description=bold(
                _("[Link if you don't see an image]({url})").format(url=data["img"][arg]),
                escape_formatting=False,
            ),
            image=data["img"][arg],
            footer=_("Requested by {req}   • From {source}").format(
                req=ctx.author.display_name, source=source
            ),
        )
        return em

    async def _maybe_embed(self, ctx: commands.Context, embed: Union[discord.Embed, str]):
        """
        Function to choose if type of the message is an embed or not
        and if not send a simple message.
        """
        try:
            if isinstance(embed, discord.Embed):
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed)
        except discord.HTTPException:
            return
            
    async def _send_other_msg(
        self, ctx: commands.Context, name: str, arg: str, source: str, url: str = None
    ):
        """Main function called in all others APIs commands."""
        embed = await self._make_embed_other(ctx, name, url, arg, source)
        return await self._maybe_embed(ctx, embed)

    @staticmethod
    async def _embed(
        color: Union[int, discord.Color] = None,
        title: str = None,
        description: str = None,
        image: str = None,
        footer: Optional[str] = None,
    ):
        em = discord.Embed(color=color, title=title, description=description)
        em.set_image(url=image)
        if footer:
            em.set_footer(text=footer)
        return em

# Based on the NSFW Check as well but modified for the api_key
def noKey():
    """Error if no API Key is stored"""
    async def predicate(ctx: commands.Context):
        lewds_key = await ctx.bot.get_shared_api_tokens("lewds")
        if lewds_key.get("api_key") is None:
            msg = _("The Lewds API key has not been set.")
            try:
                embed = discord.Embed(title="\N{LOCK} " + msg, color=0xAA0000)
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await ctx.send(msg)
            finally:
                return False
        else:
            return True

    return commands.check(predicate)

# nsfw check and such is from: https://github.com/PredaaA/predacogs 
def nsfwcheck():
    """
    Custom check that hide all commands used with it in the help formatter
    and block usage of them if used in a non-nsfw channel.
    """

    async def predicate(ctx: commands.Context):
        if not ctx.guild:
            return True
        if ctx.channel.is_nsfw():
            return True
        if ctx.invoked_with == "help" and not ctx.channel.is_nsfw():
            return False
        if ctx.invoked_with not in [k for k in ctx.bot.all_commands]:
            # For this weird issue with last version of discord.py (1.2.3) with non-existing commands.
            # So this check is only for dev version of Red.
            # https://discordapp.com/channels/133049272517001216/133251234164375552/598149067268292648 for reference.
            # It probably need to check in d.py to see what is happening, looks like an issue somewhere.
            # It will probably removed in the future, it's a temporary check.
            return False
        msg = _("You can't use this command in a non-NSFW channel !")
        try:
            embed = discord.Embed(title="\N{LOCK} " + msg, color=0xAA0000)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send(msg)
        finally:
            return False

    return commands.check(predicate)
