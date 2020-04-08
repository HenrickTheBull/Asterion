import discord
from discord.ext import commands
import textwrap
import re
import os
import sys
import importlib



class Owner(commands.Cog):
    """- Commands for the owner only."""
    def __init__(self, client):
        self.client = client

    async def cog_check(self, ctx):
        return await self.client.is_owner(ctx.author)

    @commands.command(aliases=['quit', 'damnit'])
    async def quit_bot(self, context, message):
        """Stop the bot from running"""
        await message.channel.send('I am going to sleep. :zzz:')
        client.loop.stop()

    @commands.command(aliases=['restart', 'fuck'])
    async def restart_bot(self, context, message):
     """Restart the bot"""
     await message.channel.send('I am restarting, give me a second.')
     bot.restart = True
     client.loop.stop()


def setup(client):
    client.add_cog(Owner(client))