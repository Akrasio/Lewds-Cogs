import discord

from redbot.core.bot import Red
from redbot.core import checks, commands
from redbot.core.i18n import Translator, cog_i18n

import contextlib

from . import constants as sub
from .core import Core, nsfwcheck, noKey

_ = Translator("Nsfw", __file__)


@cog_i18n(_)
class Lewds(Core):
    """
    Send NSFW Content from Ahni API
    If `[prefix]help Lewds` or any other Nsfw commands are used in a non-nsfw channel,
    you will not be able to see the list of commands for this category.
    """
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["butt"])
    async def asspic(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some booty gifs from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Ass Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("ass", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["milks", "lactation"])
    async def milk(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some milk hentai pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Milk Hentai Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("milk", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["slimey", "slimes"])
    async def slime(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some Slime Girl pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Slime Girl Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("slime", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["furfutanari"])
    async def furfuta(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some furfuta pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Fur-Futa Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("furfuta", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["yiffgif"])
    async def furgif(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some furgifs pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Fur-Gif Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("furgif", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["femboys"])
    async def trap(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some trap/femboys pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Trap/Femboy Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("trap", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["athigh"])
    async def athighs(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some Anime Thigh pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Anime Thighs Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("athighs", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["tits"])
    async def boobs(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some boob pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Boob Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("boobs", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["foot"])
    async def feet(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some feet pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Feet Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("feet", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["futanari"])
    async def futa(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some futa pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Futa Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("futa", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lewdgif", "nsfwgif"])
    async def ngifs(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some NSFW Gifs from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("NSFW Gifs"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("gifs", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["apanties", "undies"])
    async def pantsu(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some Anime underpants pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Pantsu Pictures"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("pantsu", apiKey.get("api_key")),
            )
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["animeboobs"])
    async def hboobs(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some random anime boobs from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Anime Boobs"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("hboobs", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["hentie"])
    async def hentai(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some hentai pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Hentai Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("hentai", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["kinky"])
    async def kink(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some kink pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Kink Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("kink", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["thicc"])
    async def thighs(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some thighs pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Thigh Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("thighs", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lesbianh"])
    async def yuri(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some yuri pics from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Yuri Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("yuri", apiKey.get("api_key")),
            )
    
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["latexhentai"])
    async def latex(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some latex hentai from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Latex Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("latex", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["bondage"])
    async def bdsm(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some BDSM from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("BDSM Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("bdsm", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=[])
    async def bbw(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some BDSM from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("BBW Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("bbw", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["blowjob"])
    async def blow(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some blowjob from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Blowjob hentai Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("blow", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["jacko"])
    async def jackopose(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some jackopose from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Jack-o-Pose Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("jackopose", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["femboyirl"])
    async def irlfemboy(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some real femboys from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Femboy Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("irlfemb", apiKey.get("api_key")),
            )

    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["animefeet"])
    async def hfeet(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some lewd feet from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Lewd Feet Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("hfeet", apiKey.get("api_key")),
            )
        
    @noKey()
    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["nekos"])
    async def neko(self, ctx: commands.Context):
        apiKey = await ctx.bot.get_shared_api_tokens("lewds")
        """Show some lewd nekos from Ahni API."""
        await self._send_other_msg(
            ctx,
            name=_("Lewd Neko Image"),
            arg="result",
            source="Ahni API",
            url=sub.LEWDS_URL.format("neko", apiKey.get("api_key")),
            )
