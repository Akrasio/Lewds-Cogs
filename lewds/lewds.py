import discord

from redbot.core import checks, commands
from redbot.core.i18n import Translator, cog_i18n

import contextlib

from . import constants as sub
from .core import Core, nsfwcheck

_ = Translator("Nsfw", __file__)


@cog_i18n(_)
class Lewds(Core):
    """
    Send NSFW Content from Lewds.Fun

    If `[prefix]help Lewds` or any other Nsfw commands are used in a non-nsfw channel,
    you will not be able to see the list of commands for this category.
    """


    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["butts"])
    async def ass(self, ctx: commands.Context):
        """Show some booty gifs from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Ass Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("ass"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["milks", "lactation"])
    async def milk(self, ctx: commands.Context):
        """Show some milk hentai pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Milk Hentai Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("milk"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["slimey", "slimes"])
    async def slime(self, ctx: commands.Context):
        """Show some Slime Girl pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Slime Girl Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("slime"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["furfutanari"])
    async def furfuta(self, ctx: commands.Context):
        """Show some furfuta pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Fur-Futa Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("furfuta"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["yiffgif"])
    async def furgif(self, ctx: commands.Context):
        """Show some furgifs pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Fur-Gif Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("furgif"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["femboys"])
    async def trap(self, ctx: commands.Context):
        """Show some trap/femboys pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Trap/Femboy Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("trap"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["athigh"])
    async def athighs(self, ctx: commands.Context):
        """Show some Anime Thigh pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Anime Thighs Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("athighs"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["athigh"])
    async def athighs(self, ctx: commands.Context):
        """Show some Anime Thigh pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Anime Thighs Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("athighs"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["tits"])
    async def boobs(self, ctx: commands.Context):
        """Show some boob pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Boob Image"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("boobs"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["foot"])
    async def feet(self, ctx: commands.Context):
        """Show some feet pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Feet Image"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("feet"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["futanari"])
    async def futa(self, ctx: commands.Context):
        """Show some futa pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Futa Image"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("futa"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lewdgif", "nsfwgif"])
    async def ngifs(self, ctx: commands.Context):
        """Show some NSFW Gifs from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("NSFW Gifs"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("gifs"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["apanties", "undies"])
    async def pantsu(self, ctx: commands.Context):
        """Show some Anime underpants pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Pantsu Pictures"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("pantsu"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["animeboobs"])
    async def hboobs(self, ctx: commands.Context):
        """Show some random anime boobs from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Anime Boobs"),
            arg="result",
            source="Lewds API",
            url=sub.LEWDS_URL.format("hboobs"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["hentie"])
    async def hentai(self, ctx: commands.Context):
        """Show some hentai pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Hentai Image"),
            arg="result",
            source="MxsicXYZ API",
            url=sub.LEWDS_URL.format("hentai"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["kinky"])
    async def kink(self, ctx: commands.Context):
        """Show some kink pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Kink Image"),
            arg="result",
            source="MxsicXYZ API",
            url=sub.LEWDS_URL.format("kink"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["thicc"])
    async def thighs(self, ctx: commands.Context):
        """Show some thighs pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Thigh Image"),
            arg="result",
            source="MxsicXYZ API",
            url=sub.LEWDS_URL.format("thighs"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lesbianh"])
    async def yuri(self, ctx: commands.Context):
        """Show some yuri pics from Lewds API."""
        await self._send_other_msg(
            ctx,
            name=_("Yuri Image"),
            arg="result",
            source="MxsicXYZ API",
            url=sub.LEWDS_URL.format("yuri"),
            )
