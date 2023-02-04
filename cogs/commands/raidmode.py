from discord.ext import commands
from utils.Tools import *
import discord
from core import Cog, Astroz, Context

class Raidmode(Cog):
  """Enable/Disable Anti-raid in your server to be protected from unknown raids!"""
  def __init__(self, client: Astroz):
    self.client = client

  @commands.command(name="automod", aliases=["Automoderation"], help="Shows help about Automoderation feature of bot.")
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiraid(self, ctx):
    data = getConfig(ctx.guild.id)
    spam = data["antiSpam"]
    link = data["antiLink"]
    punish = data["punishment"]
    embed = discord.Embed(title="Astroz | Antiraid",
                          description="Raidmode Commands",color=0x00FFE4)  
    embed.add_field(name="<:ok_arrow:1024940412194005052> antispam on/off",
                    value=f"Enables/Disables antispam feature\nCurrently Its {spam}",
                    inline=False)  
    embed.add_field(name="<:ok_arrow:1024940412194005052> antilink on/off",
                    value=f"Enables/Disables antilink feature\nCurrently Its {link}",
                    inline=False)
    embed.add_field(name="<:ok_arrow:1024940412194005052> punishment kick/ban/none",
                    value=f"Sets Punishment For Anti-Nuke + Raidmode Feature\nCurrently Its {punish}",
                    inline=False)
    #embed.set_footer(text="Anti-Raid Features")
    await ctx.reply(embed=embed, mention_author=False)

  @commands.command(name="antispam", aliases=['anti-spam'], help="Enables or Disables anti spam feature")
  @blacklist_check()

  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antispam(self, ctx: Context, type: str):

        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner

        if ctx.author == owner:
            if onOroff == "on":
                if data["antiSpam"] is True:
                    hacker = discord.Embed(title="Astroz | Antiraid",
                          description=f"<:error:1018174714750976030> | Anti-Spam is already enabled for **`{ctx.guild.name}`**",color=0x00FFE4)  
                    await ctx.reply(embed=hacker, mention_author=False)
                else:
                    data["antiSpam"] = True
                    updateConfig(ctx.guild.id, data)
                    hacker1 = discord.Embed(title="Astroz | Antiraid",
                          description=f"<:GreenTick:1029990379623292938> | Successfully enabled anti-spam for **`{ctx.guild.name}`**",color=0x00FFE4)  
                    await ctx.reply(embed=hacker1, mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiSpam"] = False
                updateConfig(ctx.guild.id, data)
                hacker2 = discord.Embed(title="Astroz | Antiraid",
                          description=f"<:GreenTick:1029990379623292938> | Successfully disabled anti-spam for **`{ctx.guild.name}`**",color=0x00FFE4)  
                await ctx.reply(embed=hacker2, mention_author=False)
            else:
                hacker3 = discord.Embed(title="Astroz | Automoderation",
                          description=f"<:error:1018174714750976030> | Invalid Type.\nIt Should Be On/Off",color=0x00FFE4)  
                await ctx.reply(embed=hacker3, mention_author=False)

        else:
            hacker5 = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:error:1018174714750976030> | Only owner of the server can run this command")
            await ctx.reply(embed=hacker5, mention_author=False)

  @commands.command(aliases=['anti-link'], name="antilink", help="Enables or Disables antilink feature")
  @blacklist_check()

  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antilink(self, ctx: Context, type: str):

        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner

        if ctx.author == owner:
            if onOroff == "on":
                if data["antiLink"] is True:
                    hacker = discord.Embed(title="Astroz | Antiraid",
                          description=f"<:error:1018174714750976030> | Anti-link is already enabled for **`{ctx.guild.name}`**",color=0x00FFE4)  
                    await ctx.reply(embed=hacker, mention_author=False)
                else:
                    data["antiLink"] = True
                    updateConfig(ctx.guild.id, data)
                    hacker1 = discord.Embed(title="Astroz | Antiraid",
                          description=f"<:GreenTick:1029990379623292938> | Successfully enabled anti-link for **`{ctx.guild.name}`**",color=0x00FFE4)  
                    await ctx.reply(embed=hacker1, mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiLink"] = False
                updateConfig(ctx.guild.id, data)
                hacker2 = discord.Embed(title="Astroz | Antiraid",
                          description=f"<:GreenTick:1029990379623292938> | Successfully disabled anti-link for **`{ctx.guild.name}`**",color=0x00FFE4)  
                await ctx.reply(embed=hacker2, mention_author=False)
            else:
                hacker3 = discord.Embed(title="Astroz | Antiraid",
                          description=f"<:error:1018174714750976030> | Invalid Type.\nIt Should Be On/Off",color=0x00FFE4)  
                await ctx.reply(embed=hacker3, mention_author=False)

        else:
            hacker5 = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:error:1018174714750976030> | Only owner of the server can run this command")
            await ctx.reply(embed=hacker5, mention_author=False)