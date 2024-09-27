import datetime
import discord


# Function to send a log
async def send_generic_log(info):
    # Get the current time
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the same log
    print(f"[{time}] | {info}")


# Function to send a log thats specific to a command
async def send_command_log(self, ctx, command, error=False):
    # Get the current time
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the guild, cog, and user
    guild = ctx.guild
    user = ctx.author
    cog = self.cog_name

    # Create an embed with the command information
    embed = discord.Embed(
        title=":white_check_mark: Command Run",
        color=discord.Color.green(),
    )
    embed.add_field(name=":hourglass: Time", value=time, inline=False)
    embed.add_field(
        name=":beach_umbrella: Guild",
        value=f"{guild.id}",
        inline=False,
    )
    embed.add_field(name=":gear: Cog", value=f"{cog}", inline=False)
    embed.add_field(name=":keyboard: Command", value=f"`/{command}`", inline=False)
    embed.set_footer(text=f"Command User: {user}", icon_url=user.avatar)

    # Send the embed
    await self.client.get_channel(1283459947350462584).send(embed=embed)

    # Print the same log
    print(f"[{time}] | {guild.id} | {cog} - {command} | {user}")
