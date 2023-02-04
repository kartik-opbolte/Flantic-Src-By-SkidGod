import discord
from discord.ext import commands


class hacker11111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Raidmode commands"""
  
    def help_custom(self):
		      emoji = '<:icons_kick:1037941060955017267>'
		      label = "Raidmode"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Raidmode__(self, ctx: commands.Context):
        """`automod` , `antispam` , `antilink`"""