import discord
from discord.ext import commands
import textwrap
import urllib.parse
import random
import aiohttp

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['cat', 'randomcat', 'mitch'])
    async def neko(self, ctx):
        """Hey Mitch, wanna see a cat?"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                emojis = [':cat2: ', ':cat: ', ':heart_eyes_cat: ']
                await ctx.send(random.choice(emojis) + res['file'])

    @commands.command(aliases=['pooch', 'randomdog', 'kun'])
    async def dog(self, ctx):
        """Hey you, wanna see a dog?"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()
                emojis = [':dog:', ':service_dog:', ':guide_dog:']
                await ctx.send(random.choice(emojis) + res['message'])

    @commands.command(aliases=['redpanda', 'randdompanda', 'panpan', 'paradox'])
    async def rpanda(self, ctx):
        """Hey you, wanna see a Red Panda?"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/red_panda') as r:
                res = await r.json()
                emojis = [':game_die: ']
                await ctx.send(random.choice(emojis) + res['link'])


def setup(client):
    client.add_cog(fun(client))