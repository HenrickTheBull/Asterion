import discord
from discord.ext import commands
import textwrap

class Meta(commands.Cog):
    """- Commands relating to client info."""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def about(self, ctx):
        """- Tells you about the client."""
        await ctx.send(textwrap.dedent (f"""
            Hi there, I'm Asterion. I'm a bot created by HenrickTheBull#1102 for the Axis of Communities.
            I'm ever evolving, and ever breaking. My main function is a learning tool for Henrick and a moderation tool for AoC.
            """))



def setup(client):
    client.add_cog(Meta(client))
