import discord
from discord.ext import commands
from utils.helper_functions import send_command_log, send_generic_log


class Developer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cog_name = "Developer"

    # Log that the cog was loaded
    @commands.Cog.listener()
    async def on_ready(self):
        await send_generic_log("Loaded 'Developer' cog")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.client.on_command_error(ctx, error)

    # `loadcog` Command
    # Loads a given cog
    # Can only be run by the bot owner
    @commands.hybrid_command(name="loadcog", description="Load a cog")
    @commands.is_owner()
    async def loadcog(self, ctx, cogname=None):
        # Check if cogname is None
        if cogname is None:
            # If it is, send a embed to the command user to provide a cog
            embed = discord.Embed(
                title="Error",
                description="Please provide the name of a cog to load (see /help)",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
            return

        # Try to load the cog
        try:
            # Load the cog
            cog = "cogs." + cogname
            await self.client.load_extension(cog)
        except Exception as e:
            # If an error occurs, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description=f"Loading cog {cogname} threw error {e}\nDid not load cog.",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
        else:
            # If the cog is loaded successfully, send an embed message to the command user
            embed = discord.Embed(
                title="Cog Loaded",
                description=f"The cog {cogname} has been successfully loaded.",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`loadcog` command was run by {ctx.message.author} on the {cogname} cog",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "loadcog")

    # `unloadcog` Command
    # Unloads a given cog
    # Can only be run by the bot owner
    @commands.hybrid_command(name="unloadcog", description="Unloads a cog from the bot")
    @commands.is_owner()
    async def unloadcog(self, ctx, *, cogname=None):
        # Check if cogname is None
        if cogname is None:
            # If it is, send a embed to the command user to provide a cog
            embed = discord.Embed(
                title="Error",
                description="Please provide the name of a cog to unload (see /help)",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
            return

        # Try to unload the cog
        try:
            # Unload the cog
            cog = "cogs." + cogname
            await self.client.unload_extension(cog)
        except Exception as e:
            # # If an error occurs, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description=f"Unloading cog {cogname} threw error {e}\nDid not unload cog.",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
        else:
            # If the cog is unloaded successfully, send a embed to the command user
            embed = discord.Embed(
                title="Cog Unloaded",
                description=f"The cog {cogname} has been successfully unloaded.",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`unloadcog` command was run by {ctx.message.author} on the {cogname} cog",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "unloadcog")

    # `reload` Command
    # Re-registers all application commands
    # Can only be run by the bot owner
    @commands.hybrid_command(name="reload", description="Reloads all commands")
    @commands.is_owner()
    async def reload(self, ctx):
        # Defer the response
        await ctx.defer()

        # Reload all commands
        await ctx.bot.tree.sync()

        # Send a message to the command user
        await ctx.send("Commands reloaded!")

        # Log that the command was run
        await send_command_log(self, ctx, "reload")


async def setup(client):
    await client.add_cog(Developer(client))
