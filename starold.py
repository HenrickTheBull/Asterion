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
import logging
from pathlib import Path

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
    await load_all_extensions(client)


async def load_all_extensions(client):
    """
    Attempts to load all .cog files in /cogs/ as cog extensions
    """
    await client.wait_until_ready()
    await asyncio.sleep(1)  # ensure that on_ready has completed and finished printing
    cogs = [x.stem for x in Path('cogs').glob('*.py')]
    for extension in cogs:
        try:
            client.load_extension(f'cogs.{extension}')
            print(f'Loaded {extension}')
        except Exception as e:
            error = f'{extension}\n {type(e).__name__} : {e}'
            print(f'Failed to load extension {error}')
        print('-' * 10)

# Run The Bot Finally
client.run(config["token"])
