from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from typing import Optional
class Owner(commands.Cog):
  def __init__(self, client):
    self.client = client

#https://cdn.discordapp.com/avatars/974984890959425566/7fedaa654af7ec62b211033852e048d0.webp?size=2048
  @commands.command(name="restart", help="Restarts the bot.")
  @commands.is_owner()
  async def _restart(self, ctx: Context):
    await ctx.reply("Restarting!")
    restart_program()


  @commands.command(name="sync", help="Syncs all database.")
  @commands.is_owner()
  async def _sync(self, ctx: Context):
    await ctx.reply("Syncing...", mention_author=False)
    with open('anti.json', 'r') as f:
      data = json.load(f)
    for guild in self.client.guilds:
      if str(guild.id) not in data['guild']:
        data['guilds'][str(guild.id)] = 'on'
        with open('anti.json', 'w') as f:
          json.dump(data, f, indent=4)
      else:
        pass
    with open('config.json', 'r') as f:
      data = json.load(f)
    for op in data["guilds"]:
      g = self.client.get_guild(int(op))
      if not g:
        data["guilds"].pop(str(op))
        with open('config.json', 'w') as f:
          json.dump(data, f, indent=4)
  @commands.group(name="blacklist", help="let's you add someone in blacklist", aliases=["bl"])
  @commands.is_owner()
  async def blacklist(self, ctx):
    if ctx.invoked_subcommand is None:
      with open("blacklist.json") as file:
                blacklist = json.load(file)
                embed = discord.Embed(
                title=f"There are currently {len(blacklist['ids'])} blacklisted IDs",
                description=f"{', '.join(str(id) for id in blacklist['ids'])}",
                color=0x00FFE4
            )
                #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
                await ctx.reply(embed=embed, mention_author=False)

  @blacklist.command(name="add")
  @commands.is_owner()
  async def blacklist_add(self, ctx, member: discord.Member):
    try:
      with open('blacklist.json', 'r') as bl:
        blacklist = json.load(bl)
        if str(member.id) in blacklist["ids"]:
          embed = discord.Embed(title="Error!", description=f"{member.name} is already blacklisted", color=0x00FFE4)
          await ctx.reply(embed=embed, mention_author=False)
        else:
          add_user_to_blacklist(member.id)
          embed = discord.Embed(title="Blacklisted", description=f"<:GreenTick:1029990379623292938> | Successfully Blacklisted {member.name}", color=0x00FFE4)
          with open("blacklist.json") as file:
              blacklist = json.load(file)
              embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
              await ctx.reply(embed=embed, mention_author=False)
    except:
              embed = discord.Embed(
                title="Error!",
                description=f"**An Error Occurred**",
                color=0x00FFE4
            )
              #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
              await ctx.reply(embed=embed, mention_author=False)

  @blacklist.command(
        name="remove"
    )
  @commands.is_owner()
  async def blacklist_remove(self, ctx, member: discord.Member = None):
    try:
      remove_user_from_blacklist(member.id)
      embed = discord.Embed(
                title="User removed from blacklist",
                description=f"<:GreenTick:1029990379623292938> | **{member.name}** has been successfully removed from the blacklist",
                color=0x00FFE4
            )
      with open("blacklist.json") as file:
        blacklist = json.load(file)
        embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
        await ctx.reply(embed=embed, mention_author=False)
    except:
        embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=0x00FFE4
            )
       # embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
        await ctx.reply(embed=embed, mention_author=False)

  @commands.group(name="np", help="Allows you to add someone in no prefix list (owner only command)")
  @commands.is_owner()
  async def _np(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_np.command(name="add", help="Add user to no prefix")
  @commands.is_owner()
  async def np_add(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id in np:
      embed = discord.Embed(
                title="Astroz",
                description=f"**The User You Provided Already In My No Prefix**",
                color=0x00FFE4
       )
      #embed.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed)
    else:
      data["np"].append(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed1 = discord.Embed(
                title="Astroz",
                description="<:GreenTick:1029990379623292938> | Successfully **Added {} to no prefix!**".format(user),
                color=0x00FFE4
       )
      #embed1.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed1)

  @_np.command(name="remove", help="Remove user from no prefix")
  @commands.is_owner()
  async def np_remove(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id not in np:
      embed = discord.Embed(
                title="Astroz",
                description="**{} is not in no prefix!**".format(user),
                color=0x00FFE4
       )
      #embed.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed)
    else:
      data["np"].remove(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed2 = discord.Embed(
                title="Astroz",
                description="<:GreenTick:1029990379623292938> | **Removed {} from no prefix!**".format(user),
                color=0x00FFE4
       )
      #embed2.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed2.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed2)

  @commands.group(name="bdg", help="Allows owner to add badges for a user")
  @commands.is_owner()
  async def _badge(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_badge.command(name="add", aliases=["give"], help="Add some badges to a user.")
  @commands.is_owner()
  async def badge_add(self, ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["own", "owner", "king"]:
      idk = "**<:RC_OWNER:1025209930719969382>ㆍOwner**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed2 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `Owner` Badge To {member}**",
                color=0x00FFE4
       )
      embed2.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      embed2.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed2)
    elif badge.lower() in ["staff", "support staff"]:
      idk = "**<:jr_staff:1025210867987521557>ㆍStaff**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed3 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `Staff` Badge To {member}**",
                color=0x00FFE4
       )
      #embed3.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed3.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/bs_3VGr3ycmBOMyol10UUzmEYUfeT5V9QS6eGN03TcM/%3Fsize%3D512/https/cdn.discordapp.com/avatars/1027761449436708885/f60993b941bcca6a0f9c51d3eda9c55e.png") 
      await ctx.reply(embed=embed3)
    elif badge.lower() in ["partner"]:
      idk = "**<a:_partner:1025211207566753914>ㆍPartner**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed4 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `Partner` Badge To {member}**",
                color=0x00FFE4
       )
      #embed4.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed4.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed4)
    elif badge.lower() in ["sponsor"]:
      idk = "**<:astroz_spo:1025212082532122685>ㆍSponsor**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed5 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `Sponsor` Badge To {member}**",
                color=0x00FFE4
       )
      #embed5.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed5.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed5)
    elif badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
      idk = "**<:RC_FRIENDS:1025209342674346097>ㆍOwner`s Friends**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed1 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `Owner's Friend` Badge To {member}**",
                color=0x00FFE4
       )
      #embed1.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
     # embed1.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed1)
    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "**<a:early:1002225237292744784>ㆍEarly Supporter**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed6 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `Early Supporter` Badge To {member}**",
                color=0x00FFE4
       )
      #embed6.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed6.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed6)

    elif badge.lower() in ["vip"]:
      idk = "**<a:durex_vip:1025212603909296129>ㆍVip**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed7 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `VIP` Badge To {member}**",
                color=0x00FFE4
       )
      #embed7.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed7.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed7)

    elif badge.lower() in ["bug", "hunter"]:
      idk = "**<a:astroz_1212:1002017580569084037>ㆍBug Hunter**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `Bug Hunter` Badge To {member}**",
                color=0x00FFE4
       )
      #embed8.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed8.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed8)
    elif badge.lower() in ["all"]:
      idk = "**<:RC_OWNER:1025209930719969382>ㆍOwner\n<:jr_staff:1025210867987521557>ㆍStaff\n<a:_partner:1025211207566753914>ㆍPartner\n<:astroz_spo:1025212082532122685>ㆍSponsor\n<:RC_FRIENDS:1025209342674346097>ㆍOwner`s Friends\n<a:early:1002225237292744784>ㆍEarly Supporter\n<a:durex_vip:1025212603909296129>ㆍVip\n<a:astroz_1212:1002017580569084037>ㆍBug Hunter**"
      ok.append(idk)
      makebadges(member.id, ok)
      embedall = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Added `All` Badges To {member}**",
                color=0x00FFE4
       )
      #embedall.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
     # embedall.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embedall)
    else:
      hacker = discord.Embed(
                title="Astroz",
                description="**Invalid Badge**",
                color=0x00FFE4
       )
      #hacker.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #hacker.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=hacker)

  @_badge.command(name="remove", help="Remove badges from a user.", aliases=["re"])
  @commands.is_owner()
  async def badge_remove(self, ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["own", "owner", "king"]:
      idk = "**<:RC_OWNER:1025209930719969382>ㆍOwner**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed2 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Owner` Badge To {member}**",
                color=0x00FFE4
       )
      #embed2.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed2.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed2)

    elif badge.lower() in ["staff", "support staff"]:
      idk = "**<:jr_staff:1025210867987521557>ㆍStaff**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed3 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Staff` Badge To {member}**",
                color=0x00FFE4
       )
      #embed3.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed3.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed3)

    elif badge.lower() in ["partner"]:
      idk = "**<a:_partner:1025211207566753914>ㆍPartner**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed4 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Partner` Badge To {member}**",
                color=0x00FFE4
       )
      #embed4.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed4.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed4)

    elif badge.lower() in ["sponsor"]:
      idk = "**<:astroz_spo:1025212082532122685>ㆍSponsor**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed5 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Sponsor` Badge To {member}**",
                color=0x00FFE4
       )
      #embed5.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed5.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed5)

    elif badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
      idk = "<:friends:993857133852495962> Owner's Friend"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed1 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Owner's Friend` Badge To {member}**",
                color=0x886ad1
       )
      #embed1.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed1.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed1)

    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "**<a:early:1002225237292744784>ㆍEarly Supporter**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed6 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Early Supporter` Badge To {member}**",
                color=0x00FFE4
       )
      #embed6.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed6.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed6)

    elif badge.lower() in ["vip"]:
      idk = "**<a:durex_vip:1025212603909296129>ㆍVip**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed7 = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `VIP` Badge To {member}**",
                color=0x00FFE4
       )
      #embed7.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed7.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed7)

    elif badge.lower() in ["bug", "hunter"]:
      idk = "**<a:astroz_1212:1002017580569084037>ㆍBug Hunter**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
                title="Astroz",
                description=f"**Successfully Removed `Bug Hunter` Badge To {member}**",
                color=0x00FFE4
       )
      #embed8.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed8.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed8)
      await ctx.reply(f"<:GreenTick:1029990379623292938> | Successfully Removed `Bug Hunter` Badge From **{member}**")
    elif badge.lower() in ["all"]:
      idk = "**<:RC_OWNER:1025209930719969382>ㆍOwner\n<:jr_staff:1025210867987521557>ㆍStaff\n<a:_partner:1025211207566753914>ㆍPartner\n<:astroz_spo:1025212082532122685>ㆍSponsor\n<:RC_FRIENDS:1025209342674346097>ㆍOwner`s Friends\n<a:early:1002225237292744784>ㆍEarly Supporter\n<a:durex_vip:1025212603909296129>ㆍVip\n<a:astroz_1212:1002017580569084037>ㆍBug Hunter**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embedall = discord.Embed(
                title="Astroz",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `All` Badges From {member}**",
                color=0x00FFE4
       )
      #embedall.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embedall.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embedall)
    else:
      hacker = discord.Embed(
                title="Astroz",
                description="**Invalid Badge**",
                color=0x00FFE4
       )
      #hacker.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #hacker.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=hacker)

  
  @commands.command(name="syncs", help="Syncs Slash Commands.")
  @commands.is_owner()
  async def _sync(self, ctx) -> None:
      fmt = await ctx.bot.tree.sync(guild=ctx.guild)
      await ctx.send(
          f"Synced {len(fmt)} commands to the current guild."
        )
      channel = await ctx.message.author.create_dm()
      await channel.send('Hacker_xD Was Here')
      return



  @commands.command(help="Make the bot say something in a given channel.")
  @commands.is_owner()
  async def say(self, ctx: commands.Context, channel_id: int, *, message):
      channel = self.bot.get_channel(channel_id)
      guild = channel.guild
      channel = await ctx.message.author.create_dm()
      await ctx.send(f"Sending message to **{guild}** <#{channel.id}>\n> {message}")
      await channel.send(message)
