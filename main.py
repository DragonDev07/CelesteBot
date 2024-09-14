import asyncio
import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.helper_functions import send_generic_log

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "cogs"))

# Load `.env` environment variables
load_dotenv()

# Get the token from the environment variables
TOKEN = os.environ.get("TOKEN")

# Declare Intents
intents = discord.Intents.all()
intents.message_content = True

# Create a Bot instance
client = commands.Bot(command_prefix=">", intents=intents, help_command=None)


# On Ready Event - Change bot's presence & print the bots username + it is ready
@client.event
async def on_ready():
    # Sync Commands
    _loaded_commands = await client.tree.sync()

    # Change bot's presence
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="/help")
    )

    # Log that the bot is online
    await send_generic_log(f"Logged in as {client.user}")


# On User Join Event
@client.event
async def on_member_join(member):
    # Create an embed with the welcome message
    embed = discord.Embed(
        title="Welcome!",
        description=f"Welcome to the server {member}!",
        color=discord.Color.green(),
    )
    embed.set_thumbnail(url=member.avatar)

    # Get the channel to send the welcome message
    channel = member.guild.system_channel

    if channel:
        # Send the welcome message
        await channel.send(embed=embed)

        # Log that a welcome message was sent
        await send_generic_log(f"{member.guild} | on_member_join() | {member}")
    else:
        print("Could not run `on_member_join()` - No system channel found")


# Error Handling
@client.event
async def on_command_error(ctx, error):
    print(f"Error, {error}")


# Function to load cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await load_cogs()

    if TOKEN:
        await client.start(TOKEN)
    else:
        print("No token found.")


# Run the bot
asyncio.run(main())
