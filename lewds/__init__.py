from redbot.core.bot import Red
from .lewds import Lewds

__red_end_user_data_statement__ = (
    "This cog requires a set apikey from an external image api for returning data."
)

def setup(bot):
    bot.add_cog(Lewds(bot))
