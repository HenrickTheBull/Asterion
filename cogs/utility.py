import discord
from discord.ext import commands
import textwrap

class Utility(commands.Cog):
    """Commands for utility."""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        '''Check Response Time'''
        ping = ctx.message
        pong = await ctx.send('**:ping_pong:** Pong!')
        delta = pong.created_at - ping.created_at
        delta = int(delta.total_seconds() * 1000)
        await pong.edit(content=f':ping_pong: Pong! ({delta} ms)\n*Discord WebSocket Latency: {round(self.client.latency, 5)} ms*')


def setup(client):
    client.add_cog(Utility(client))