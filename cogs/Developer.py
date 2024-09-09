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
        await self.client.on_command_error(ctx, error)

    # Command to load a cog
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

        # Print to the console that the command has been run
        print(f"The 'loadcog' command was run by {ctx.message.author}")

    # Command to unload a cog
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

        # Print to the console that the command has been run
        print(
            f"The 'unloadcog' command was run by {ctx.message.author} on {cogname} cog"
        )

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
