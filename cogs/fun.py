import discord
from discord.ext import commands
import textwrap
import urllib.parse
import random
import aiohttp

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['cat', 'randomcat'])
    async def neko(self, ctx):
        '''Hey Mitch, wanna see a cat?'''
        #http://discordpy.readthedocs.io/en/latest/faq.html#what-does-blocking-mean
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                emojis = [':cat2: ', ':cat: ', ':heart_eyes_cat: ']
                await ctx.send(random.choice(emojis) + res['file'])


def setup(client):
    client.add_cog(fun(client))