############MODULES#############
import discord
import requests
import aiohttp
import datetime
import random
from discord.ext import commands
from random import randint
from time import sleep
from utils.Tools import *
from core import Cog, Astroz, Context
#14
#snipe | editsnipe | tickle | kiss | hug | slap | pat | feed | pet | howgay | slots | penis | meme | cat





def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 

    @blacklist_check()
    @commands.command(help="Tickle mentioned user .",usage="Tickle <member>")
    async def tickle(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"`{ctx.author}` you must mention a user to do that!")
        else:
            r = requests.get("https://nekos.life/api/v2/img/tickle")
            res = r.json()
            embed = discord.Embed(
              timestamp=datetime.datetime.utcnow(),
              description=f"{ctx.author.mention} tickle {user.mention}",color=0x00FFE4
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)
    @blacklist_check()
    @commands.command(help="Kiss mentioned user .",usage="Kiss <member>")
    async def kiss(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"`{ctx.author}` you must mention a user to do that!")
        else:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()
            embed = discord.Embed(
              timestamp=datetime.datetime.utcnow(),
              description=f"{ctx.author.mention} kisses {user.mention}",color=0x00FFE4
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)


    @blacklist_check()            
    @commands.command(help="Hug mentioned user .",usage="Tickle <member>")
    async def hug(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"`{ctx.author}` you must mention a user to do that!")
        else:
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            embed = discord.Embed(
              timestamp=datetime.datetime.utcnow(),color=0x00FFE4,
              description=f"{ctx.author.mention} hugs {user.mention}",
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)

    @commands.command(help="Slap mentioned user .",usage="Slap <member>")
    @blacklist_check()
    async def slap(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"`{ctx.author}` you must mention a user to do that!")
        else:
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()
            embed = discord.Embed(
              timestamp=datetime.datetime.utcnow(),color=0x00FFE4,
              description=f"{ctx.author.mention} slapped {user.mention}",
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)

    @commands.command(help="Pat mentioned user .",usage="Pat <member>")
    @blacklist_check()
    async def pat(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"`{ctx.author}` you must mention a user to do that!")
        else:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()
            embed = discord.Embed(
              timestamp=datetime.datetime.utcnow(),
              description=f"{ctx.author.mention} pats {user.mention}",color=0x00FFE4
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")   
            await ctx.send(embed=embed)

    @commands.command(help="Feed mentioned user .",usage="Feed <member>")
    @blacklist_check()
    async def feed(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"`{ctx.author}` you must mention a user to do that!")
        else:
            r = requests.get("https://nekos.life/api/v2/img/feed")
            res = r.json()
            embed = discord.Embed(
              timestamp=datetime.datetime.utcnow(),
              description=f"{ctx.author.mention} feeds {user.mention}",color=0x00FFE4
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)

    @commands.command(usage="Pet <member>")
    @blacklist_check()
    async def pet(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"`{ctx.author}` you must mention a user to do that!")
        else:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()
            embed = discord.Embed(
              timestamp=datetime.datetime.utcnow(),
              description=f"{ctx.author.mention} pets {user.mention}",color=0x00FFE4
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)


      
    @commands.command(aliases=['gay'],help="check someone gay percentage",usage="Howgay <person>")
    @blacklist_check()
    async def howgay(self, ctx, *, person): 
        embed = discord.Embed(color=0x00FFE4)
        responses = ['50',
                  '75',
                  '25',
                  '1',
                  '3',
                  '5',
                  '10',
                  '65',
                  '60',
                  '85',
                  '30',
                  '40',
                  '45',
                  '80',
                  '100',
                  '150',
                  '1000']
        embed.description = f'**{person} is {random.choice(responses)}% Gay** :rainbow:'
        embed.set_footer(text=f'How gay are you? - {ctx.author.name}')
        await ctx.send(embed = embed)
    @howgay.error 
    async def howgay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="*You must mention someone to howgay!*")
            await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    async def slots(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"[ {a} {b} {c} ]\n{ctx.author.mention}"
        if (a == b == c):
            await ctx.send(embed=discord.Embed(title="Slot machine", description=f"{slotmachine} All Matching! You Won!",color=0x00FFE4))
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed(title="Slot machine", description=f"{slotmachine} 2 Matching! You Won!",color=0x00FFE4))
        else:
            await ctx.send(embed=discord.Embed(title="Slot machine", description=f"{slotmachine} No Matches! You Lost!",color=0x00FFE4))

    @commands.command(aliases = ['dick'],help="Check someone`s dick`s size .",usage="Dick [member]")
    @blacklist_check()
    async def penis(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        size = random.randint(1, 15)
        dong = ""
        for _i in range(0, size):
            dong += "="
        em = discord.Embed(title=f"**{user}'s** Dick size", description=f"8{dong}D",color=0x00FFE4)
        em.set_footer(text=f'whats {user} dick size?')
        await ctx.send(embed=em)

    @commands.command(help="give you a meme",usage="meme")
    @blacklist_check()
    async def meme(self, ctx):
        embed = discord.Embed(title="""Take some memes""",color=0x00FFE4)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                embed.set_footer(text=f'Random Meme:')
                #embed.set_footer(text=f'Random Meme:')
                await ctx.send(embed=embed)

    @commands.command(usage="cat")
    @blacklist_check()
    async def cat(self, ctx):
        embed = discord.Embed(title="""Here's a cat""",color=0x00FFE4)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                embed.set_image(url=res['file'])
                embed.set_footer(text=f'Random Cats:')
                await ctx.send(embed=embed)

    @commands.command(name="iplookup", aliases=['ip', 'ipl'],help="shows info about an ip",usage="Iplookup [ip]")
    @blacklist_check()
    async def iplookup(self, ctx, *, ip):
     async with aiohttp.ClientSession() as a:
       async with a.get(f"http://ipwhois.app/json/{ip}") as b:
         c = await b.json()
         try:
           coordj = ''.join(f"{c['latitude']}" + ", " + f"{c['longitude']}")
           embed = discord.Embed(
           title="IP: {}".format(ip),
						description=f"```txt\n\nLocation Info:\nIP: {ip}\nIP Type: {c['type']}\nCountry, Country code: {c['country']} ({c['country_code']})\nPhone Number Prefix: {c['country_phone']}\nRegion: {c['region']}\nCity: {c['city']}\nCapital: {c['country_capital']}\nLatitude: {c['latitude']}\nLongitude: {c['longitude']}\nLat/Long: {coordj} \n\nTimezone Info:\nTimezone: {c['timezone']}\nTimezone Name: {c['timezone_name']}\nTimezone (GMT): {c['timezone_gmt']}\nTimezone (GMT) offset: {c['timezone_gmtOffset']}\n\nContractor/Hosting Info:\nASN: {c['asn']}\nISP: {c['isp']}\nORG: {c['org']}\n\nCurrency:\nCurrency type: {c['currency']}\nCurrency Code: {c['currency_code']}\nCurrency Symbol: {c['currency_symbol']}\nCurrency rates: {c['currency_rates']}\nCurrency type (plural): {c['currency_plural']}```",
						color=0x00FFE4
					)
           embed.set_footer(text='Thanks For Using Astroz',icon_url="https://media.discordapp.net/attachments/1036538198236614676/1037664035186954270/blue_circle.jpg")
           await ctx.send(embed=embed)
         except KeyError:
          embed = discord.Embed(
						description="KeyError has occured, perhaps this is a bogon IP address, or invalid IP address?",
						color=0x00FFE4
					)
          await ctx.send(embed=embed)


