import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Get token from `.env` file
TOKEN = os.environ.get("TOKEN")

# Declare Intents
intents = discord.Intents.all()
intents.message_content = True

# Create Client
client = commands.Bot(command_prefix=">", intents=intents)


# On Ready Event - Change bot's presence & print the bots username + it is ready
@client.event
async def on_ready():
    # Sync Commands
    loaded_commands = await client.tree.sync()

    # Print bot is online
    print(f"{client.user} is now online.")


# Error Handling
@client.event
async def on_command_error(ctx, error):
    print(f"Error, {error}")


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await load_cogs()
    await client.start(TOKEN)


asyncio.run(main())
