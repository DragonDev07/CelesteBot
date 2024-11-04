import requests
import json
import discord
import datetime
import pytz
from discord.ext import commands, tasks
from utils.helper_functions import send_command_log, send_generic_log


class Jitpack(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cog_name = "Jitpack"
        self.total_downloads = 1838
        self.update_downloads.start()

    # Log that the cog was loaded
    @commands.Cog.listener()
    async def on_ready(self):
        await send_generic_log("Loaded 'Jitpack' cog")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.client.on_command_error(ctx, error)

    @commands.hybrid_command(
        name="downloads", description="Get the total downloads for MeepMeep"
    )
    async def downloads(self, ctx):
        # Return total_downloads value in an embed
        embed = discord.Embed(
            title="MeepMeep Downloads",
            description=f"Total Downloads: {self.total_downloads}",
            color=discord.Color.green(),
        )
        embed.set_footer(
            text=f"`join` command was run by {ctx.message.author}",
            icon_url=ctx.author.avatar,
        )

        await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "downloads")

    @tasks.loop(
        time=(datetime.time(hour=21, minute=55, tzinfo=pytz.timezone("America/Denver")))
    )
    async def update_downloads(self):
        now = datetime.datetime.now(pytz.timezone("America/Denver"))
        # Check if its sunday
        if now.weekday() != 6:
            return

        # Update the total dowloads
        weekly_downloads = await self.fetch_downloads()
        self.total_downloads += weekly_downloads

        # Create an Embed containing the total downloads, and the weekly downloads that were added
        embed = discord.Embed(
            title="MeepMeep Downloads",
            description=f"Total Downloads: {self.total_downloads}",
            color=discord.Color.green(),
        )
        embed.add_field(name="Weekly Downloads", value=weekly_downloads)
        embed.set_footer(text=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Send the Embed to the #meepmeep-downloads channel
        await self.client.get_channel(1298670280322846771).send(embed=embed)

    # Ensure the bot is ready before starting the loop
    @update_downloads.before_loop
    async def before_update_downloads(self):
        await self.client.wait_until_ready()

    # Helper function to get downloads from Jitpack's API
    async def fetch_downloads(self):
        # Fetch downloads from url
        url = "https://jitpack.io/api/downloads/com.github.rh-robotics/meepmeep"
        response = requests.get(url)

        # Extract the "week" downloads from the response if it was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Extract "week" downloads
            downloads = data.get("week", 0)

            # Print the download information
            send_generic_log(f"Weekly downloads for MeepMeep: {downloads}")
            return downloads
        else:
            send_generic_log(
                f"Failed to retrieve data. Status code: {response.status_code}"
            )
            return -10000000000000000


async def setup(client):
    await client.add_cog(Jitpack(client))
