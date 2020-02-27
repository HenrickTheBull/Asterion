import discord
from discord.ext import commands

client = discord.Client()

client.run()

@client.event
async def on_ready():
    print('The Stars Call For Me')

@client.event
async def on_message(message):
    if message.author == client.user:
        return