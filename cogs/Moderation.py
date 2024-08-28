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

        # Send a response to the command user
        await ctx.send(f"Kicked User {member} for reason {reason}")

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

        # Send a response to the command user
        await ctx.send(f"User {member} has been banned for reason: {reason}")

        # Print to the console that the command has been run
        print(
            f"The 'ban' command has been run on {member} by {ctx.message.author} for reason {reason}"
        )

    # Unban Command
    @commands.hybrid_command(name="unban", description="Unban a member from the server")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: discord.User):
        # Unban the member from the guild
        await ctx.guild.unban(member)

        # Send a response to the command user
        await ctx.send(f"User {member} has been unbanned")

        # Print to the console that the command has been run
        print(f"The 'unban' command has been run on {member} by {ctx.message.author}")

    # Clear Command
    @commands.hybrid_command(
        name="clear", description="Clear a specified amount of messages"
    )
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        # Defer the response
        await ctx.defer()

        # Clear the specified amount of messages
        await ctx.channel.purge(limit=amount)

        # Send a response to the command user
        await ctx.send(f"Cleared {amount} messages")

        # Print to the console that the command has been run
        print(
            f"The 'clear' command has been run by {ctx.message.author} and cleared {amount} messages"
        )

    # Userinfo Command
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

        # Print to the console that the command has been run
        print(f"The 'userinfo' command was run by {ctx.message.author} on {member}")


async def setup(client):
    await client.add_cog(Moderation(client))
