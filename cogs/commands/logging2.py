import discord
from discord.ext import commands


class hacker111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Logging commands"""
  
    def help_custom(self):
		      emoji = '<:icons_channel:1037941106672939008>'
		      label = "Logging"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Logging__(self, ctx: commands.Context):
        """`logging` , `logging channel` , `logging config` , `logging delete`"""