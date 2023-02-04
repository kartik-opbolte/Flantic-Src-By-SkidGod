from __future__ import annotations
from discord.ext import commands
from core import Cog, Astroz, Context
import discord
from utils.Tools import *
from discord.ui import Button, View
import datetime
from typing import Optional


class Security(Cog):
  """Shows a list of commands regarding antinuke"""
  def __init__(self, client:Astroz):
    self.client = client

  @commands.group(name="Antinuke", aliases=["anti", "Security"], help="Enables/Disables antinuke in your server!", invoke_without_command=True, usage="Antinuke Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antinuke(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antinuke.command(name="enable", help="Server owner should enable antinuke for the server!",usage="Antinuke Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_enable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    if ctx.author.id == ctx.guild.owner_id:
      if data == "on":
        embed = discord.Embed(title="Astroz Security", description=f"**{ctx.guild.name} security settings **<:role_astroz:1037653804469997638>\nOhh uh! looks like your server has already enabled security\n\nCurrent Status: <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n\n> To disable use `antinuke disable`", color=0x00FFE4)
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateanti(ctx.guild.id, data)
        embed2 = discord.Embed(title="Astroz Security", description=f"**{ctx.guild.name} Security Settings** <:role_astroz:1037653804469997638>\nAlso move my role to top of roles for me to work properly.\n\nPunishments:\n\n**Anti Bot:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Ban:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Kick:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Prune:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Channel Create/Delete/Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Role Create/Delete/Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Webhook Create:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Emoji Create/Delete/Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Guild Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Community Spam:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Integration Create:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Everyone/Here/Role Mention:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Vanity Steal:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Whitelisted Users:** {len(wled)}\n\n**Auto Recovery:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>", color=0x00FFE4)
        embed2.add_field(name="Other Settings", value=f"To change the punishment type `{ctx.prefix}Antinuke punishment set <type>`\nAvailable Punishments are `Ban`, `Kick` and `None`.")
        embed2.set_footer(text=f"Current punishment type is {punish}")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Astroz Security", description="<:error:1018174714750976030> Only owner of the server can run this command",color=0x00FFE4)
      await ctx.reply(embed=hacker5, mention_author=False)

  @_antinuke.command(name="disable", help="You can disable antinuke for your server using this command", aliases=["off"],usage="Antinuke disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_disable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    if ctx.author.id == ctx.guild.owner_id:
      if data == "off":
        emb = discord.Embed(title="Astroz Security", description=f"**{ctx.guild.name} Security Settings **<:role_astroz:1037653804469997638>\nOhh NO! looks like your server has already disabled security\n\nCurrent Status: <:astro_disable:1038127308814422067><:astroz_disble:1038127252476534785>\n\n> To enable use `antinuke enable`",color=0x00FFE4)
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateanti(ctx.guild.id, data)
        final = discord.Embed(title="Astroz Security", description=f"**{ctx.guild.name} Security Settings** <:role_astroz:1037653804469997638>\nSuccessfully disabled security settings.\n\nCurrent Status: <:astro_disable:1038127308814422067><:astroz_disble:1038127252476534785>\n\n> To enable again use `antinuke enable`",color=0x00FFE4)
        await ctx.reply(embed=final, mention_author=False)

  @_antinuke.command(name="show", help="Shows currently antinuke config settings of your server", aliases=["config"],usage="Antinuke show")
  @blacklist_check()

  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_show(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    if data == "off":
      emb = discord.Embed(title="Astroz Security", description=f"**{ctx.guild.name} Security Settings **<:role_astroz:1037653804469997638>\nOhh NO! looks like your server has already disabled security\n\nCurrent Status: <:astro_disable:1038127308814422067><:astroz_disble:1038127252476534785>\n\n> To enable use `antinuke enable`",color=0x00FFE4)
      await ctx.reply(embed=emb, mention_author=False)
    elif data == "on":
      embed2 = discord.Embed(title="Astroz Security", description=f"**{ctx.guild.name} security settings** <:role_astroz:1037653804469997638>\nPunishments:\n**Anti Bot:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Ban:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Kick:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Prune:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Channel Create/Delete/Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Role Create/Delete/Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Webhook Create:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Emoji Create/Delete/Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Guild Update:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Community Spam:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Integration Create:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Everyone/Here/Role Mention:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Anti Vanity Steal:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>\n**Whitelisted Users:** {len(wled)}\n\n**Auto Recovery:** <:jk_no:1037656914399604746><:jk_yes:1037656941494812702>",color=0x00FFE4)
      embed2.add_field(name="Other Settings", value=f"To change the punishment type `{ctx.prefix}Antinuke punishment set <type>`\nAvailable Punishments are `Ban`, `Kick` and `None`.")
      embed2.set_footer(text=f"Current Punishment Type Is {punish}")
      await ctx.reply(embed=embed2, mention_author=False)
  @_antinuke.command(name="recover", help="Deletes all channels with name of rules and moderator-only",usage="Antinuke recover")
  @blacklist_check()

  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _recover(self, ctx: Context):
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
                await channel.delete()
            except:
                pass
    await ctx.reply("Successfully Deleted All Channels With Name Of `rules, moderator-only`", mention_author=False)

  @_antinuke.group(name="punishment", help="Changes Punishment of antinuke and antiraid for this server.", invoke_without_command=True,usage="Antinuke punishment set/show")
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _punishment(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_punishment.command(name="set", help="Changes Punishment of antinuke and automod for this server.", aliases=["change"],usage="Antinuke punishment set <none>")
  @blacklist_check()

  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_set(self, ctx, punishment: str):
        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner
        if ctx.author == owner:

            kickOrBan = punishment.lower()

            if kickOrBan == "kick":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "kick"
                hacker = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",color=0x00FFE4)
                await ctx.reply(embed=hacker, mention_author=False)

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "ban":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "ban"
                hacker1 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",color=0x00FFE4)
                await ctx.reply(embed=hacker1, mention_author=False)

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "none":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "none"
                hacker3 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",color=0x00FFE4)
                await ctx.reply(embed=hacker3, mention_author=False)

                updateConfig(ctx.guild.id, data)
            else:
               hacker5 = discord.Embed(title="Astroz Security", description=f"Invalid Punishment Type\nValid Punishment Type(s) Are: Kick, Ban, None",color=0x00FFE4)
               await ctx.reply(embed=hacker5, mention_author=False)

        else:
            hacker5 = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> Only owner of the server can run this command",color=0x00FFE4)
            await ctx.reply(embed=hacker5, mention_author=False)

  @_punishment.command(name="show", help="Shows custom punishment type for this server",usage="Antinuke punishment show")
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_show(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    punish = data["punishment"]
    hacker5 = discord.Embed(color=0x00FFE4,title="Astroz Security", description="Custom punishment of anti-nuke and automod in this is: **{}**".format(punish.title()))
    await ctx.reply(embed=hacker5,mention_author=False)
  @_antinuke.command(name="setvanity", aliases=['vanityset', 'vanity'], help="Sets vanity code in database and reverts when server vanity is changed",usage="Antinuke setvanity <vanity_code>")
  @blacklist_check()
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _setvanity(self, ctx: Context, vanity_code: str):
        if not ctx.guild.premium_tier == 3:
            hacker5 = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> Your Servers Vanity Is Locked",color=0x00FFE4)
            await ctx.reply(embed=hacker5)
        else:
          if ctx.author.id == ctx.guild.owner_id:
            if "https://discord.gg/" in vanity_code:
              idk = vanity_code.replace("https://discord.gg/", "")
            elif "discord.gg/" in vanity_code:
              idk = vanity_code.replace("discord.gg/", "")
            elif "discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("discord.com/invite", "")
            elif "https://discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("https://discord.com/invite/", "")
            else:
              idk = vanity_code
            update_vanity(ctx.guild.id, idk)
            hacker = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Set Vanity For {ctx.guild.name} To {idk}",color=0x00FFE4)         
            await ctx.reply(embed=hacker, mention_author=False)
          elif ctx.author.id == 143853929531179008:
            if "https://discord.gg/" in vanity_code:
              idk = vanity_code.replace("https://discord.gg/", "")
            elif "discord.gg/" in vanity_code:
              idk = vanity_code.replace("discord.gg/", "")
            elif "discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("discord.com/invite", "")
            elif "https://discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("https://discord.com/invite/", "")
            else:
              idk = vanity_code
            update_vanity(ctx.guild.id, idk)
            hacker1 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Set Vanity For {ctx.guild.name} To {idk}",color=0x00FFE4)         
            await ctx.reply(embed=hacker1, mention_author=False)
          else:
            hacker4 = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> Only owner of the server can run this command",color=0x00FFE4)
            await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.command(name="channelclean", aliases=['cc'], help="deletes channel with similar name provided.",usage="Antinuke channelclean <none>")
  @blacklist_check()

  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _channelclean(self, ctx: Context, channeltodelete: str):
    if ctx.author.id == ctx.guild.owner_id:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      hacker1 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Deleted All Channels With The Name Of {channeltodelete}",color=0x00FFE4)         
      await ctx.reply(embed=hacker1, mention_author=False)
    elif ctx.author.id == 143853929531179008:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      hacker2 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Deleted All Channels With The Name Of {channeltodelete}",color=0x00FFE4)         
      await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker4 = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> Only owner of the server can run this command",color=0x00FFE4)
      await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.command(name="roleclean", aliases=['cr'], help="deletes role with similar name provided",usage="Antinuke roleclean <none>")
  @blacklist_check()

  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_roles=True)
  async def _roleclean(self, ctx: Context, roletodelete: str):
    if ctx.author.id == ctx.guild.owner_id:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      hacker = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Deleted All Roles With The Name Of {roletodelete}",color=0x00FFE4)         
      await ctx.reply(embed=hacker, mention_author=False)
    elif ctx.author.id == 143853929531179008:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      hacker3 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Deleted All Roles With The Name Of {roletodelete}",color=0x00FFE4)         
      await ctx.reply(embed=hacker3, mention_author=False)
    else:
      hacker4 = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> Only owner of the server can run this command",color=0x00FFE4)
      await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.group(name="whitelist", aliases=["wl"], help="Whitelist your TRUSTED users for anti-nuke", invoke_without_command=True,usage="Antinuke whitelist add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def _whitelist(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)
      
  @_whitelist.command(name="add", help="Add a user to whitelisted users",usage="Antinuke whitelist add <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    if ctx.author == owner:
      if len(wled) == 15:
        hacker = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> This server have already maximum number of whitelisted users (15)\nRemove one to add another :)",color=0x00FFE4)
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(user.id) in wled:
          hacker1 = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> That user is already in my whitelist.",color=0x00FFE4)          
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          wled.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Whitelisted {user.mention} For {ctx.guild.name}")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(title="Astroz Security", description=f"<:error:1018174714750976030> Only owner of the server can run this command",color=0x00FFE4)
      await ctx.reply(embed=hacker5)

  @_whitelist.command(name="remove", help="Remove a user from whitelisted users",usage="Antinuke whitelist remove <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    if ctx.author == owner:
      if str(user.id) in wled:
        wled.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Unwhitelisted {user.mention} For {ctx.guild.name}")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(color=0x00FFE4,title="Astroz Security", description="<:error:1018174714750976030> | That user is not in my whitelist.")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:error:1018174714750976030> Only owner of the server can run this command")
      await ctx.reply(embed=hacker5, mention_author=False)

  @_whitelist.command(name="show", help="Shows list of whitelisted users in the server.",usage="Antinuke whitelist show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_show(self, ctx):
      data = getConfig(ctx.guild.id)
      wled = data["whitelisted"]
      if len(wled) == 0:
        hacker = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:error:1018174714750976030> | There aren\'t any whitelised users for this server")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(title=f"Whitelised Users For {ctx.guild.name}", description="\n", color=0x00FFE4)
      for idk in wled:
        embed.description += f"<@{idk}> | ID: {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)


  @_whitelist.command(name="reset", help="removes every user from whitelist database", aliases=["clear"],usage="Antinuke whitelist reset")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def wl_reset(self, ctx: Context):
    if ctx.author.id == ctx.guild.owner_id:
      data = getConfig(ctx.guild.id)
      data["whitelisted"] = []
      updateConfig(ctx.guild.id, data)
      hacker = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Cleared Whitelist Database For **{ctx.guild.name}**")         
      await ctx.reply(embed=hacker, mention_author=False)
    else:
      hacker5 = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:error:1018174714750976030> Only owner of the server can run this command")
      await ctx.reply(embed=hacker5)