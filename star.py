#################################
# 
#  Main File for Asterion Discord Bot
#  Written by: Bryant Stafford
#  Email: bryant.stafford@outlook.com
#  Discord: HenrickTheBull#1102
#  
#  🌟🐂
#################################
import discord
from discord.ext import commands
import traceback
import json
import os
import asyncio
import aiohttp
import random

print('Loading Primary Config...')

# Reading JSON Settings File
with open("config.json", "r") as cjson:
    config = json.load(cjson)

print('Loading Bot...')

# Define Bot Client
client = commands.AutoShardedBot(command_prefix=config["prefix"])

# Login Message.
@client.event
async def on_ready():
    print('The Stars Call For Me.')
    print('Logged on as {0} (ID: {0.id})'.format(client.user))
    for cog in cogs:
        client.load_extension(cog)

# Ignore own Messages.
@client.event
async def on_message(message):
    if message.author == client.user:
        return


#Load Cog
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#Unload Cog
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

print('Loading Cogs...')
cogs = ['cogs.meta']

# Run The Bot Finally
client.run(config["token"])