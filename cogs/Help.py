import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Log that the cog has been laoded
    @commands.Cog.listener()
    async def on_ready(self):
        print("The 'Help' cog has been loaded")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.bot.on_command_error(ctx, error)

    # Help command which lists all cogs, commands, prefixes, etc.
    @commands.hybrid_command(
        name="help", description="List all cogs, commands, prefixes, etc."
    )
    async def help(self, ctx):
        # Defer the response
        await ctx.defer()

        # Create an embed
        embed = discord.Embed(title="Help", color=discord.Color.blurple())
        embed.add_field(
            name="Moderation Commands",
            value="• /kick <member> <optional: reason> - Kicks a given member, requires the user to have the KICK_MEMBER permission to run\n• /ban <member> <optional: reason> - Bans a given member, requires the user to have the BAN_MEMBER permission to run\n• /unban <member> - Unbans a given member, requires the user to have the BAN_MEMBER permission\n• /clear <amount> - Clears a given amount of messages, requires the MANAGE_MESSAGES permission to run\n• /userinfo <member> - Displays information about a given member",
            inline=False,
        )
        embed.add_field(
            name="Media Commands",
            value="• /join - Joins the voice channel of the user\n• /leave - Leaves the voice channel of the user\n• /play <url> - Plays a given youtube URL\n• /pause - Pauses the current song\n• /resume - Resumes the current song\n• /stop - Stops the current song\n• /volume <optional: percentage> - Changes the volume of the bot, if no percentage is given, it will display the current volume",
        )
        embed.add_field(
            name="Cogs (DEBUG INFO FOR DEVELOPERS)",
            value="• Developer\n• Moderation\n• Help",
            inline=False,
        )
        embed.footer(
            name="Created w/ ❤️ by",
            value="Teo Welton (@furthestdrop)",
            inline=True,
        )

        # Send the embed
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Help(client))
