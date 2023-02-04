import discord
from discord.ext import commands


class hacker11(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Music commands"""
  
    def help_custom(self):
		      emoji = '<:astroz_music:1038617241425563668>'
		      label = "Music"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Music__(self, ctx: commands.Context):
        """`connect` , `disconnect` , `play` , `loop` , `stop` , `queue` , `pause` , `resume` , `skip`"""