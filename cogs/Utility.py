import discord
from discord.ext import commands
from utils.helper_functions import send_command_log, send_generic_log


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cog_name = "Utility"

    # Log that the Cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        await send_generic_log("Loaded 'Utility' cog")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.client.on_command_error(ctx, error)

    # `userinfo` Command
    # Gets information about a given user
    #
    # Provided Information:
    #   - User ID
    #   - Date and Time of Server Join
    #   - Date and Time of Account Creation
    #   - Roles
    #   - Avatar
    @commands.hybrid_command(
        name="userinfo", description="Get information about a specified user"
    )
    async def userinfo(self, ctx, member: discord.Member):
        # Create an embed with the user's information
        embed = discord.Embed(
            title=f"{member}",
            color=discord.Color.blue(),
        )
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(
            name="Joined Server",
            value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"),
            inline=False,
        )
        embed.add_field(
            name="Created Account",
            value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            inline=False,
        )
        roles = ", ".join([role.name for role in member.roles])
        embed.add_field(name="Roles", value=roles, inline=False)
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

        # Send the embed
        await ctx.send(embed=embed)

        # Send a log that the command has been run
        await send_command_log(self, ctx, "userinfo")

    # `serverinfo` Command
    # Gets information about the server
    #
    # Provided Information:
    #   - Server Icon
    #   - Server Creation Date and Time
    #   - Server Owner
    #   - Number of members
    #   - Number of roles
    #   - Number of channels
    @commands.hybrid_command(
        name="serverinfo", description="Get information about the server"
    )
    async def serverinfo(self, ctx):
        # Create an embed with the server's information
        embed = discord.Embed(
            title=f"{ctx.guild.name}",
            color=discord.Color.blue(),
        )
        embed.add_field(name="ID", value=ctx.guild.id, inline=False)
        embed.add_field(
            name="Created",
            value=ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            inline=False,
        )
        embed.add_field(name="Owner", value=ctx.guild.owner, inline=False)
        embed.add_field(
            name="Number of Members", value=ctx.guild.member_count, inline=False
        )
        embed.add_field(
            name="Number of Roles", value=len(ctx.guild.roles), inline=False
        )
        embed.add_field(
            name="Number of Channels", value=len(ctx.guild.channels), inline=False
        )
        embed.set_thumbnail(url=ctx.guild.icon)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

        # Send the embed
        await ctx.send(embed=embed)

        # Send a log that the command has been run
        await send_command_log(self, ctx, "serverinfo")

    # `ping` Command
    # Command to get the bot's latency
    @commands.hybrid_command(name="ping", description="Get the bot's latency")
    async def ping(self, ctx):
        # Get the bot's latency
        latency = round(self.client.latency * 1000)

        # Send the latency as a response
        await ctx.send(f":ping_pong: Pong! {latency}ms")

        # Send a log that the command has been run
        await send_command_log(self, ctx, "ping")


async def setup(client):
    await client.add_cog(Utility(client))
