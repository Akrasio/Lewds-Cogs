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
    Send NSFW Content from Ahni API
    If `[prefix]help Lewds` or any other Nsfw commands are used in a non-nsfw channel,
    you will not be able to see the list of commands for this category.
    """


    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["butts"])
    async def ass(self, ctx: commands.Context):
        """Show some booty gifs from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Ass Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("ass"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["milks", "lactation"])
    async def milk(self, ctx: commands.Context):
        """Show some milk hentai pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Milk Hentai Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("milk"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["slimey", "slimes"])
    async def slime(self, ctx: commands.Context):
        """Show some Slime Girl pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Slime Girl Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("slime"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["furfutanari"])
    async def furfuta(self, ctx: commands.Context):
        """Show some furfuta pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Fur-Futa Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("furfuta"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["yiffgif"])
    async def furgif(self, ctx: commands.Context):
        """Show some furgifs pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Fur-Gif Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("furgif"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["femboys"])
    async def trap(self, ctx: commands.Context):
        """Show some trap/femboys pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Trap/Femboy Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("trap"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["athigh"])
    async def athighs(self, ctx: commands.Context):
        """Show some Anime Thigh pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Anime Thighs Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("athighs"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["tits"])
    async def boobs(self, ctx: commands.Context):
        """Show some boob pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Boob Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("boobs"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["foot"])
    async def feet(self, ctx: commands.Context):
        """Show some feet pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Feet Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("feet"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["futanari"])
    async def futa(self, ctx: commands.Context):
        """Show some futa pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Futa Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("futa"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lewdgif", "nsfwgif"])
    async def ngifs(self, ctx: commands.Context):
        """Show some NSFW Gifs from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("NSFW Gifs"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("gifs"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["apanties", "undies"])
    async def pantsu(self, ctx: commands.Context):
        """Show some Anime underpants pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Pantsu Pictures"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("pantsu"),
            )
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["animeboobs"])
    async def hboobs(self, ctx: commands.Context):
        """Show some random anime boobs from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Anime Boobs"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("hboobs"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["hentie"])
    async def hentai(self, ctx: commands.Context):
        """Show some hentai pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Hentai Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("hentai"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["kinky"])
    async def kink(self, ctx: commands.Context):
        """Show some kink pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Kink Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("kink"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["thicc"])
    async def thighs(self, ctx: commands.Context):
        """Show some thighs pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Thigh Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("thighs"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lesbianh"])
    async def yuri(self, ctx: commands.Context):
        """Show some yuri pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Yuri Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("yuri"),
            )
    
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["latexhentai"])
    async def latex(self, ctx: commands.Context):
        """Show some latex hentai from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Latex Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("latex"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["bondage"])
    async def bdsm(self, ctx: commands.Context):
        """Show some BDSM from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("BDSM Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("bdsm"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=[])
    async def bbw(self, ctx: commands.Context):
        """Show some BDSM from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("BBW Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("bbw"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["blowjob"])
    async def blow(self, ctx: commands.Context):
        """Show some blowjob from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Blowjob hentai Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("blow"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["jacko"])
    async def jackopose(self, ctx: commands.Context):
        """Show some jackopose from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Jack-o-Pose Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("jackopose"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["femboyirl"])
    async def irlfemboy(self, ctx: commands.Context):
        """Show some real femboys from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Femboy Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("irlfemb"),
            )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["animefeet"])
    async def hfeet(self, ctx: commands.Context):
        """Show some lewd feet from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Lewd Feet Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("hfeet"),
            )
        
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["nekos"])
    async def neko(self, ctx: commands.Context):
        """Show some lewd nekos from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Lewd Neko Image"),
            source="Ahni API",
            url=sub.LEWDS_URL.format("neko"),
            )
