import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Log that the Cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("The 'Moderation' cog has been loaded")

    # Propagate the error to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.bot.on_command_error(ctx, error)

    # ------ Command to kick a member from the guild ------ #
    @commands.command(name="kick", description="Kicks a user from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked User {member} for reason {reason}")
        print(
            f"The 'kick' command has been run on {member} by {ctx.message.author} for reason {reason}"
        )

    # ------ Command to ban a member from the guild ------ #
    @commands.command(name="ban", description="Bans a user from the server")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(
            f"User {member} has been ejected into the abyss (banned) for reason {reason}"
        )
        print(
            f"The 'ban' command has been run on {member} by {ctx.message.author} for reason {reason}"
        )

    # ------ Command to clear given numbe of messages from channel ------ #
    @commands.command(
        name="clear", description="Clears a given number of messages from the channel"
    )
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared the last {amount} messages")
        print(
            f"The 'clear' command was run by {ctx.message.author} for amount {amount}"
        )

    # ------ Command to unban a member from the guild ------ #
    @commands.command(name="unban", description="Unbans a user from the server")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                print(f"The 'unban' command was run by {ctx.message.author} on {user}")

    # ------ Command to get information about a user in the guild ------ #
    @commands.command(name="userinfo", description="Get information about a user")
    async def userinfo(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title=f"{member}",
            description=f"Information about {member}",
            color=discord.Color.blue(),
        )
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)
        print(f"The 'userinfo' command was run by {ctx.message.author} on {member}")


async def setup(client):
    await client.add_cog(Moderation(client))
