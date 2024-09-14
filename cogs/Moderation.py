import discord
from discord.ext import commands
from utils.helper_functions import send_command_log, send_generic_log


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cog_name = "Moderation"

    # Log that the Cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        await send_generic_log("Loaded 'Moderation' cog")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.client.on_command_error(ctx, error)

    # `kick` Command
    # Kicks a given member from the server
    @commands.hybrid_command(name="kick", description="Kick a member from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        # Kick the member from the guild
        await ctx.guild.kick(member, reason=reason)

        # Create an embed with the kick information
        embed = discord.Embed(
            title="Member Kicked",
            description=f"User {member} has been kicked for reason: {reason}",
            color=discord.Color.red(),
        )
        embed.set_footer(
            text=f"Kicked by {ctx.message.author}", icon_url=ctx.author.avatar
        )

        # Send the embed as a response
        await ctx.send(embed=embed)

        # Log that the command has been run
        await send_command_log(self, ctx, "kick")

    # `ban` Command
    # Bans a given member from the server
    @commands.hybrid_command(name="ban", description="Ban a member from the server")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        # Ban the member from the guild
        await ctx.guild.ban(member, reason=reason)

        # Create an embed with the ban information
        embed = discord.Embed(
            title=":hammer: Member Banned",
            description=f"User {member} has been banned for reason: {reason}",
            color=discord.Color.red(),
        )
        embed.set_footer(
            text=f"Banned by {ctx.message.author}", icon_url=ctx.author.avatar
        )

        # Send the embed as a response
        await ctx.send(embed=embed)

        # Log that the command has been run
        await send_command_log(self, ctx, "ban")

    # `clear` Command
    # Clears a specified number of messages from the channels
    @commands.hybrid_command(
        name="clear", description="Clear a specified amount of messages"
    )
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        # Defer the response
        await ctx.defer()

        # Clear the specified amount of messages
        await ctx.channel.purge(limit=amount + 1)

        # Create an embed with the clear information
        embed = discord.Embed(
            title=":wastebasket: Messages Cleared",
            description=f"Cleared {amount} messages",
            color=discord.Color.green(),
        )
        embed.set_footer(
            text=f"`clear` command run by {ctx.message.author} for {amount} messages",
            icon_url=ctx.author.avatar,
        )

        # Send a response to the command user
        await ctx.send(embed=embed)

        # Log that the command has been run
        await send_command_log(self, ctx, "clear")


async def setup(client):
    await client.add_cog(Moderation(client))
