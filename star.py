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

# Reading JSON Settings File
with open("config.json", "r") as cjson:
    config = json.load(cjson)

client = commands.AutoShardedBot(command_prefix=config["prefix"])


@client.event
async def on_ready():
    print('The Stars Call For Me')
    print("Logged in as %s#%s" % (client.user.name, client.user.discriminator))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


client.run(config["token"])