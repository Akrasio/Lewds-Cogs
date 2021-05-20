from redbot.core.bot import Red
from .weverse import Weverse

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)

def setup(bot):
    bot.add_cog(Weverse(bot))
