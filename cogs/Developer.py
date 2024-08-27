import discord
from discord.ext import commands


class Developer(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Log that the cog was loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("The 'Developer' cog has been loaded")

    # Propagate the error to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.bot.on_command_error(ctx, error)

    # ------ Command to load a cog ------ #
    @commands.command()
    @commands.is_owner()
    async def loadcog(self, ctx, cogname=None):
        if cogname is None:
            await ctx.send("Please provide a cog to load.")
            return
        try:
            cog = "cogs." + cogname
            await self.client.load_extension(cog)
        except Exception as e:
            await ctx.send(f"Loading cog {cogname} threw error {e}. Did not load cog.")
        else:
            await ctx.send("Loaded Cog!")
        print(f"The 'loadcog' command was run by {ctx.message.author}")

    # ------ Command to unload a cog ------ #
    @commands.command()
    @commands.is_owner()
    async def unloadcog(self, ctx, cogname=None):
        if cogname is None:
            await ctx.send("Please provide a cog to unload.")
            return
        try:
            cog = "cogs." + cogname
            await self.client.unload_extension(cog)
        except Exception as e:
            await ctx.send(
                f"Unloading cog {cogname} threw error {e}. Did not unload cog."
            )
        else:
            await ctx.send("Unloaded Cog!")
        print(f"The 'unloadcog' command was run by {ctx.message.author}")

    # ------ Command to sync slash commands ------ #
    @commands.hybrid_command()
    @commands.is_owner()
    async def reload(self, ctx):
        await ctx.bot.tree.sync()
        await ctx.send("Commands reloaded!")
        print(f"The 'reload' command was run by {ctx.message.author}")


async def setup(client):
    await client.add_cog(Developer(client))
