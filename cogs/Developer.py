import discord
from discord.ext import commands


class Developer(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Log that the cog was loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("The 'Developer' cog has been loaded")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.bot.on_command_error(ctx, error)

    # Command to load a cog
    @commands.hybrid_command(name="load", description="Load a cog")
    @commands.is_owner()
    async def loadcog(self, ctx, cogname: str = None):
        # Check if cogname is None
        if cogname is None:
            # If it is, send a message to the command user to provide a cog
            await ctx.send("Please provide a cog to load.")
            return
        try:
            # Load the cog
            cog = "cogs." + cogname
            await self.client.load_extension(cog)
        except Exception as e:
            # If an error occurs, send a message to the command user
            await ctx.send(f"Loading cog {cogname} threw error {e}. Did not load cog.")
        else:
            # If the cog is loaded successfully, send a message to the command user
            await ctx.send("Loaded Cog!")

        # Print to the console that the command has been run
        print(f"The 'loadcog' command was run by {ctx.message.author}")

    # Command to unload a cog
    @commands.hybrid_command(name="unloadcog", description="Unloads a cog from the bot")
    @commands.is_owner()
    async def unloadcog(self, ctx, *, cogname: str = None):
        # Check if cogname is None
        if cogname is None:
            # If it is, send a message to the command user to provide a cog
            await ctx.send("Please provide a cog to unload.")
            return
        try:
            # Unload the cog
            cog = "cogs." + cogname
            await self.client.unload_extension(cog)
        except Exception as e:
            # If an error occurs, send a message to the command user
            await ctx.send(
                f"Unloading cog {cogname} threw error {e}. Did not unload cog."
            )
        else:
            # If the cog is unloaded successfully, send a message to the command user
            await ctx.send("Unloaded Cog!")

        # Print to the console that the command has been run
        print(f"The 'unloadcog' command was run by {ctx.message.author}")

    # Command to reload all commands
    @commands.hybrid_command(name="reload", description="Reloads all commands")
    @commands.is_owner()
    async def reload(self, ctx):
        # Defer the response
        await ctx.defer()

        # Reload all commands
        await ctx.bot.tree.sync()

        # Send a message to the command user
        await ctx.send("Commands reloaded!")

        # Print to the console that the command has been run
        print(f"The 'reload' command was run by {ctx.message.author}")


async def setup(client):
    await client.add_cog(Developer(client))
