import discord
from discord.ext import commands
import os
from datetime import datetime
import threading
from dotenv import load_dotenv

# getting the token out of our env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
bot = commands.Bot(command_prefix="`")
