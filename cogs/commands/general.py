import discord
from discord.ext import commands
from afks import afks
from discord.utils import get
import psutil
from psutil import Process, virtual_memory
from typing import Union, Optional
import time
import datetime
import random
import requests
import aiohttp
import re
from discord.ext.commands.errors import BadArgument
from discord.colour import Color
import hashlib
from utils.Tools import *
import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
import io
import textwrap
import datetime
import sys
from discord.ui import Button, View
import psutil
import time
import datetime
import platform


password = ['1838812`', '382131847', '231838924', '218318371', '3145413', '43791', '471747183813474', '123747019', '312312318']
def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.aiohttp = aiohttp.ClientSession()
        self._URL_REGEX = r'(?P<url><[^: >]+:\/[^ >]+>|(?:https?|steam):\/\/[^\s<]+[^<.,:;\"\'\]\s])'
        self.tasks = []
        self.dump_tasks = []
        self.sniped = {}
        self.afk = {}
        
        
    @commands.command(help="Changes your state to afk.",usage="Afk [reason]")
    @blacklist_check()
    async def afk(self, ctx, *, reason="I am afk."):
        member = ctx.author
        if member.id in afks.keys():
            afks.pop(member.id)
        else:
            try:
                await member.edit(nick = f"[AFK] {member.display_name}")
            except:
                pass
        afks[member.id] = reason
        embed = discord.Embed(
        description = f'{member.name} Your AFK is now set to {reason}',
        color = 0x00FFE4
      )
        embed.set_author(name=f"{member.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            embed = discord.Embed(
        description = f'{message.author.name}, I removed your AFK.',
        color = 0x00FFE4
      )
            embed.set_author(name=f"{message.author.name}")
            await message.channel.send(embed=embed)

        for id, reason in afks.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                embed = discord.Embed(
        description = f'{member.name} is AFK {reason}',
        color = 0x00FFE4
      )
                embed.set_author(name=f"{member.name}")
                await message.reply(embed=embed)

 
######################


    @commands.command(usage="Avatar [member]",
        name='avatar',
        aliases=['av', 'ab', 'ac', 'ah', 'pfp', 'avi', 'ico'],
        help="""Wanna steal someone's avatar here you go
Aliases"""
    )
    @blacklist_check()
    async def avatar(self, ctx, user: discord.Member = None):
        try:
          if user == None:
             user = ctx.author
          else:  
             user = await self.bot.fetch_user(user.id)
        except AttributeError:
            user = ctx.author
        webp = user.avatar.replace(format='webp')
        jpg = user.avatar.replace(format='jpg')
        png = user.avatar.replace(format='png')
        avemb = discord.Embed(
            color=0x00FFE4,
            title=f"{user}'s Avatar",description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
            if not user.avatar.is_animated()
            else f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({user.avatar.replace(format='gif')})"
        )
        avemb.set_image(url=user.avatar.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)


    @commands.command(
                      help="Shows the banner",
                      usage="banner")
    @blacklist_check()
    async def banner(self, ctx):
        if len(ctx.guild.banner_url) == 0:
            return await ctx.send(embed=discord.Embed(
                title="banner", description="There is no guild banner"),
                                  color=self.color)
        await ctx.send(embed=discord.Embed(title="**`%s`**'s server banner" %
                                           (ctx.guild.name),
                                           color=self.color).set_image(
                                               url=ctx.guild.banner_url))

    @commands.command(help="Shows the server icon",usage="Servericon")
    @blacklist_check()
    async def servericon(self, ctx):
        server = ctx.guild
        webp = server.icon.replace(format='webp')
        jpg = server.icon.replace(format='jpg')
        png = server.icon.replace(format='png')
        avemb = discord.Embed(
            color=0x00FFE4,
            title=f"{server}'s Icon",description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
            if not server.icon.is_animated()
            else f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({server.icon.replace(format='gif')})"
        )
        avemb.set_image(url=server.icon.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)



    @commands.command(
                      help="Get total member count of the server",
                      usage="membercount",
                      aliases=["mc"])
    @blacklist_check()
    async def membercount(self, ctx):
        online = 0
        offline = 0
        dnd = 0
        idle = 0
        bots = 0
        for member in ctx.guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.dnd:
                dnd += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.bot:
                bots += 1
        embed = discord.Embed(
            title=ctx.guild.name,
            description="Here is **`%s`**'s member information" %
            (ctx.guild.name),
            color=0x00FFE4)
        embed.add_field(name="*Online*", value="`%s`" % (online), inline=False)
        embed.add_field(name="*Offline*",
                        value="`%s`" % (offline),
                        inline=False)
        embed.add_field(name="*Idle*", value="`%s`" % (idle), inline=False)
        embed.add_field(name="*Do Not Disturb*",
                        value="`%s`" % (dnd),
                        inline=False)
        embed.add_field(name="*Bots*", value="`%s`" % (bots), inline=False)
        embed.add_field(name="*Total*",
                        value="`%s`" % (len(ctx.guild.members)),
                        inline=False)
        #embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
    @commands.command(usage="Poll [message]")
    @blacklist_check()
    async def poll(self, ctx,*,message):
      emp = discord.Embed(title=f"**Poll!**", description=f"{message}", color =  0x00FFE4)
      msg = await ctx.send(embed=emp)
      await msg.add_reaction("👍")
      await msg.add_reaction("👎")

    @commands.command(help="hack someone's discord account",usage="Hack <member>")
    @blacklist_check()
    async def hack(self, ctx, member: discord.Member):
      random_pass = random.choice(password)
      embed = discord.Embed(title=f"**Hacked!**", description=f"Username - {member.display_name}\n E-Mail - {member.display_name}@gmail.com\n Password - {member.display_name}@{random_pass}", color =  0x00FFE4)
      await ctx.send(embed=embed)

    @commands.command(usage="Token <member>")
    @blacklist_check()
    async def token(self, ctx, user: discord.Member = None):
        list = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
            '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        token = random.choices(list, k=59)
        if user is None:
            user = ctx.author
            await ctx.send(user.mention + "'s token is " + ''.join(token))
        else:
            await ctx.send(user.mention + "'s token is " + "".join(token))




    @commands.command(help="check users of astroz .")
    @blacklist_check()
    async def users(self, ctx):
      embed = discord.Embed(
        title=f"**Users:**", 
        description=f"**{len(set(self.bot.get_all_members()))} Users Of Astroz**",
        color = 0x00FFE4
      )
      await ctx.send(embed=embed)

    @commands.command(help="italicize the given text",usage="Italicize <message>")
    @blacklist_check()
    async def italicize(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('*' + message + '*')


    @commands.command(help="strike the given text",usage="Strike <message>")
    @blacklist_check()
    async def strike(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('~~' + message + '~~')


    @commands.command(help="quote the given text",usage="Quote <message>")
    @blacklist_check()
    async def quote(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('> ' + message)


    @commands.command(help="code the given text",usage="Code <message>")
    @blacklist_check()
    async def code(self, ctx, *, message):
        await ctx.send('`' + message + "`")


    @commands.command(help="bold the given text",usage="Bold <message>")
    @blacklist_check()
    async def bold(self, ctx, *, message):
        await ctx.send('**' + message + '**')


    @commands.command(help="censor the given text",usage="Censor <message>")
    @blacklist_check()
    async def censor(self, ctx, *, message):
        await ctx.send('||' + message + '||')


    @commands.command(help="underline the given text",usage="Underline <message>")
    @blacklist_check()
    async def underline(self, ctx, *, message):
        await ctx.send('__' + message + '__')



    @commands.command(usage="Gender <member>")
    @blacklist_check()
    async def gender(self, ctx, member: discord.Member):
      embed = discord.Embed(
        description=f"{member.mention}'s gender is None",
        color = discord.Colour.default()
      )
      await ctx.send(embed=embed)



    @commands.command(usage="Wizz")
    @blacklist_check()
    async def wizz(self, ctx):
      message6 = await ctx.send(f"`Wizzing {ctx.guild.name}, will take 22 seconds to complete`")
      message5 = await ctx.send(f"`Deleting {len(ctx.guild.roles)} Roles...`")
      message4 = await ctx.send(f"`Deleting {len(ctx.guild.channels)} Channels...`")
      message3 = await ctx.send(f"`Deleting Webhooks...`")
      message2 = await ctx.send(f"`Deleting emojis`")
      message1 = await ctx.send(f"`Installing Ban Wave..`")
      await message6.delete()
      await message5.delete()
      await message4.delete()
      await message3.delete()
      await message2.delete()
      await message1.delete()
      embed=discord.Embed(title="Astroz", description=f"**Successfully Wizzed {ctx.guild.name}**", color=0x00FFE4,timestamp=ctx.message.created_at)
      await ctx.reply(embed=embed)
    @commands.command(help="Gives a gif of pikachu",usage="Pikachu")
    @blacklist_check()
    async def pikachu(self, ctx):
      response = requests.get('https://some-random-api.ml/img/pikachu')
      data = response.json()
      embed = discord.Embed(
        title = 'Pikachu',
        description = 'Here is a gif of Pikachu.',
        color = 0x00FFE4
      )
      embed.set_image(url=data['link'])
      embed.set_footer(name="Made By ~ Hacker_xD#0001", icon_url="")
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)
    @commands.command( help="Shortens specified url with 3 different url shorteners",usage="Shorten <url>")
    @blacklist_check()
    async def shorten(self, ctx: commands.Context, *, url: str):
        async with ctx.typing():
            embed = discord.Embed(
                title="URL Shortener ({})".format(url))
            async with self.aiohttp.get("https://api.shrtco.de/v2/shorten?url={}".format(url)) as shrtco:
                async with self.aiohttp.get("https://clck.ru/--?url={}".format(url)) as clck:
                    async with self.aiohttp.get("http://tinyurl.com/api-create.php?url={}".format(url)) as tiny:
                        parse = await shrtco.json()
                        embed.add_field(name="Shortened URL (9qr.de)", value=parse["result"]["full_short_link2"], inline=False)
                        embed.add_field(name="Shortened URL (clck.ru)", value=await clck.text(), inline=False)
                        embed.add_field(name="Shortened URL (tinyurl.com)", value=await tiny.text(), inline=False)
        await ctx.reply(embed=embed, mention_author=True)
        
        
    @commands.command(description="Searches for specified phrase on urbandictionary.com", help="Don't know meaning of some words don't worry this will help",usage="Urban <phrase>")
    @blacklist_check()
    async def urban(self, ctx, *, phrase):
        async with self.aiohttp.get("http://api.urbandictionary.com/v0/define?term={}".format(phrase)) as urb:
            urban = await urb.json()
            try:
                embed = discord.Embed(
                    title=f"Term - \"{phrase}\"", color=0x00FFE4)
                embed.add_field(name="Definition",
                                value=urban['list'][0]['definition'].replace('[', '').replace(']', ''))
                embed.add_field(name="Example", value=urban['list'][0]['example'].replace(
                    '[', '').replace(']', ''))
                temp = await ctx.reply(embed=embed, mention_author=True)
                await asyncio.sleep(15)
                await temp.delete()
                await ctx.message.delete()
            except:
                pass
    @commands.command(name="rickroll",help="Detects if provided url is a rick-roll",usage="Rickroll <url>")
    @blacklist_check()
    async def _rr(self, ctx: commands.Context, *, url: str):
        if not re.match(self._URL_REGEX, url):
            raise BadArgument("Invalid URL")

        phrases = ["rickroll", "rick roll", "rick astley", "never gonna give you up"]
        source = str(await (await self.aiohttp.get(url, allow_redirects=True)).content.read()).lower()
        rickRoll = bool(
            (re.findall('|'.join(phrases), source, re.MULTILINE | re.IGNORECASE)))
        await ctx.reply(embed=discord.Embed(
            title="Rick Roll {} in webpage".format(
                "was found" if rickRoll is True else "was not found"),
            color=Color.red() if rickRoll is True else Color.green(),
        ), mention_author=True)

    @commands.command(name="hash",help="Hashes provided text with provided algorithm")
    @blacklist_check()
    async def _hash(self, ctx, algorithm: str, *, message):
        algos: dict[str, str] = {
            "md5": hashlib.md5(bytes(message.encode("utf-8"))).hexdigest(),
            "sha1": hashlib.sha1(bytes(message.encode("utf-8"))).hexdigest(),
            "sha224": hashlib.sha224(bytes(message.encode("utf-8"))).hexdigest(),
            "sha3_224": hashlib.sha3_224(bytes(message.encode("utf-8"))).hexdigest(),
            "sha256": hashlib.sha256(bytes(message.encode("utf-8"))).hexdigest(),
            "sha3_256": hashlib.sha3_256(bytes(message.encode("utf-8"))).hexdigest(),
            "sha384": hashlib.sha384(bytes(message.encode("utf-8"))).hexdigest(),
            "sha3_384": hashlib.sha3_384(bytes(message.encode("utf-8"))).hexdigest(),
            "sha512": hashlib.sha512(bytes(message.encode("utf-8"))).hexdigest(),
            "sha3_512": hashlib.sha3_512(bytes(message.encode("utf-8"))).hexdigest(),
            "blake2b": hashlib.blake2b(bytes(message.encode("utf-8"))).hexdigest(),
            "blake2s": hashlib.blake2s(bytes(message.encode("utf-8"))).hexdigest()
        }
        embed = discord.Embed(color=Color.green(),
                              title="Hashed \"{}\"".format(message))
        if algorithm.lower() not in list(algos.keys()):
            for algo in list(algos.keys()):
                hashValue = algos[algo]
                embed.add_field(name=algo, value="```{}```".format(hashValue))
        else:
            embed.add_field(name=algorithm, value="```{}```".format(
                algos[algorithm.lower()]), inline=False)
        await ctx.reply(embed=embed, mention_author=True)



    @commands.Cog.listener()
    async def on_message_delete(self, message): 
        if message.guild == None: 
            return
        if message.author.bot: 
            return
        if not message.content: 
            return 
        self.sniped[message.channel.id] = message
         #@commands.command(aliases=['sb'])
    @commands.guild_only()
    @commands.has_permissions(view_audit_log=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @blacklist_check()
    @commands.group(name="snipe", help="Snipes the most recent deleted message", usage="snipe")
    async def snipe(self, ctx):
        message = self.sniped.get(ctx.channel.id)
        if message == None:
            return await ctx.send(embed=discord.Embed(title="Snipe", description="There are no recently deleted messages", color=0x00FFE4))
        embed = discord.Embed(title="Sniped Message sent by %s" % (message.author), description=message.content, color=0x00FFE4, timestamp=message.created_at)
        await ctx.send(embed=embed)

 

    @commands.command( help="Gives a role to all members", usage="roleall <role>", aliases=["role-all", "rall"])
    @blacklist_check()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def roleall(self, ctx, *, role: discord.Role):
        if ctx.guild.id in self.tasks:
            return await ctx.send(embed=discord.Embed(title="roleall", description="There is a roleall task already running, please wait for it to finish", color=0x00FFE4))
        await ctx.message.add_reaction("<:GreenTick:1029990379623292938>")
        num = 0
        failed = 0
        for user in list(ctx.guild.members):
            try:
                await user.add_roles(role)
                num += 1
            except Exception:
                failed += 1
        await ctx.send(embed=discord.Embed(title="roleall", description="<:GreenTick:1029990379623292938> | Successfully added **`%s`** to **`%s`** users, failed to add it to **`%s`** users" % (role.name, num, failed), color=0x00FFE4))



    @commands.group(name="jail", help="Jails a user", usage="jail <user>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def jail(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="jailed")
        if not role:
            await ctx.guild.create_role(name="jailed")

        jail = discord.utils.get(ctx.guild.text_channels, name="jail")
        if not jail:
            try:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
                }            
                jail = await ctx.guild.create_text_channel("jail", overwrites=overwrites)
                await ctx.send(embed=discord.Embed(title="jail", description="Your server has no jail channel, I created one for you %s" % (jail.mention), color=0x00FFE4))
            except discord.Forbidden:
                return await ctx.send(embed=discord.Embed(title="jail", help="Please give me permissions, I am unable to create the jailed channel", color=0x00FFE4))

        for channel in ctx.guild.channels:
            if channel.name == "jail":
                perms = channel.overwrites_for(member)
                perms.send_messages = True
                perms.read_messages = True
                await channel.set_permissions(member, overwrite=perms)
            else:
                perms = channel.overwrites_for(member)
                perms.send_messages = False
                perms.read_messages = False
                perms.view_channel = False
                await channel.set_permissions(member, overwrite=perms)

        role = discord.utils.get(ctx.guild.roles, name="jailed")
        await member.add_roles(role)

        await jail.send(content=member.mention, embed=discord.Embed(title="jail", description="Please live out your jail sentence until the court lets you free.", color=0x00FFE4))
        await ctx.send(embed=discord.Embed(title="jail", description="Successfully jailed **`%s`**" % (member.name), color=0x00FFE4))
        await member.send(embed=discord.Embed(title="jail", description="You have been jailed in **`%s`** by **`%s`**" % (ctx.guild.name, ctx.author.name), color=0x00FFE4))

    @commands.group(name="unjail", help="Unjails a user", usage="unjail <user>",  aliases=["free"])
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def unjail(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="jailed")
        for channel in ctx.guild.channels:
            if channel.name == "jail":
                perms = channel.overwrites_for(member)
                perms.send_messages = None
                perms.read_messages = None
                await channel.set_permissions(member, overwrite=perms)
            else:
                perms = channel.overwrites_for(member)
                perms.send_messages = None
                perms.read_messages = None
                perms.view_channel = None
                await channel.set_permissions(member, overwrite=perms)

        await member.remove_roles(role)
        await ctx.send(embed=discord.Embed(title="unjail", description="Successfully unjailed **`%s`**" % (member.name), color=self.color))
        await member.send(embed=discord.Embed(title="unjail", description="you have been unjailed in **`%s`** by **`%s`**" % (ctx.guild.name, ctx.author.name), color=0x00FFE4))

    @commands.group(name="cleanup", help="deletes the bots messages", aliases=["purgebots"], usage="cleanup <amount>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def cleanup(self, ctx, amount: int):
        msg = await ctx.send("cleaning...")
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                if message.id == msg.id:
                    pass
                else:
                    await message.delete()
            except:
                pass
        await msg.edit(content="cleaned up 👍")




