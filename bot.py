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
        if message.content.startswith('https://x.com'):
            fix = message.content.replace('x.com', 'vxtwitter.com')
        else:
            fix = message.content.replace('twitter.com', 'vxtwitter.com')
        
        user = message.author

        # Create a webhook in the same channel
        webhook = await message.channel.create_webhook(name=user.display_name)
        
        # Use the webhook to send the message with the user's name and avatar
        await webhook.send(fix, username=user.display_name, avatar_url=user.avatar.url)
        await message.delete()

        # Delete the webhook to clean up (optional)
        await webhook.delete()


    if message.content.startswith('https://tiktok.com') or message.content.startswith('https://www.tiktok.com'):
        fix = message.content.replace('tiktok.com', 'vxtiktok.com')
        user = message.author
        # Create a webhook in the same channel
        webhook = await message.channel.create_webhook(name=user.display_name)
        
        # Use the webhook to send the message with the user's name and avatar
        await webhook.send(fix, username=user.display_name, avatar_url=user.avatar.url)
        await message.delete()

        # Delete the webhook to clean up (optional)
        await webhook.delete()


    if message.content.startswith('https://instagram.com') or message.content.startswith('https://www.instagram.com'):
        ext = message.content.split("instagram.com", 1)[1]
        fix = 'https://d.ddinstagram.com' + ext
        user = message.author
        # Create a webhook in the same channel
        webhook = await message.channel.create_webhook(name=user.display_name)
        
        # Use the webhook to send the message with the user's name and avatar
        await webhook.send(fix, username=user.display_name, avatar_url=user.avatar.url)
        await message.delete()

        # Delete the webhook to clean up (optional)
        await webhook.delete()



    if message.content.startswith('https://reddit.com') or message.content.startswith('https://www.reddit.com'):
        fix = message.content.replace('reddit.com', 'rxddit.com')
        user = message.author
        # Create a webhook in the same channel
        webhook = await message.channel.create_webhook(name=user.display_name)
        
        # Use the webhook to send the message with the user's name and avatar
        await webhook.send(fix, username=user.display_name, avatar_url=user.avatar.url)
        await message.delete()

        # Delete the webhook to clean up (optional)
        await webhook.delete()


    # Check for the command !resend
    if message.content.startswith("!resend"):
        user = message.author
        content = message.content[8:]  # Extract the message after "!resend "

        # Create a webhook in the same channel
        webhook = await message.channel.create_webhook(name=user.display_name)
        
        # Use the webhook to send the message with the user's name and avatar
        await webhook.send(content, username=user.display_name, avatar_url=user.avatar.url)
        
        # Delete the webhook to clean up (optional)
        await webhook.delete()


bot.run(TOKEN)