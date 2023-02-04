import discord
from discord.ext import commands


class hacker1111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""
  
    def help_custom(self):
		      emoji = '<:icons_join:1037940998162092062>'
		      label = "Welcome"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Welcome__(self, ctx: commands.Context):
        """`welcome` , `welcome enable` , `welcome  disable` , `welcome message` , `welcome channel` , `welcome test `"""