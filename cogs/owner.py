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




def setup(client):
    client.add_cog(Owner(client))