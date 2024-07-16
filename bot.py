import discord
from discord.ext import commands
import os
from datetime import datetime
import threading
from dotenv import load_dotenv

# getting the token out of our env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#new intents needed
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('https://x.com') or message.content.startswith('https://twitter.com'):
        fix = message.content.replace('x.com', 'fxtwitter.com')
        
        name = message.author.nick
        if name is None:
            name = message.author.global_name
        msg = f'{fix} \nFrom: {name}'
        await message.delete()
        await message.channel.send(msg)
        

bot.run(TOKEN)