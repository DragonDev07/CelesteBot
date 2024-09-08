import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Log that the Cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("The 'Moderation' cog has been loaded")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.bot.on_command_error(ctx, error)

    # Kick Command
    @commands.hybrid_command(name="kick", description="Kick a member from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
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

        # Print to the console that the command has been run
        print(
            f"The 'kick' command has been run on {member} by {ctx.message.author} for reason {reason}"
        )

    # Ban Command
    @commands.hybrid_command(name="ban", description="Ban a member from the server")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
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

        # Print to the console that the command has been run
        print(
            f"The 'ban' command has been run on {member} by {ctx.message.author} for reason {reason}"
        )

    # Clear Command
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

        # Print to the console that the command has been run
        print(
            f"The 'clear' command has been run by {ctx.message.author} and cleared {amount} messages"
        )


async def setup(client):
    await client.add_cog(Moderation(client))
