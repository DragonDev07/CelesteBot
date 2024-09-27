import ollama
import discord
from discord.ext import commands
from utils.helper_functions import send_command_log, send_generic_log


class AI(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cog_name = "AI"

    # Log that the cog was loaded
    @commands.Cog.listener()
    async def on_ready(self):
        await send_generic_log("Loaded 'AI' cog")

    # Propagate the errors to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.client.on_command_error(ctx, error)

    # `llama3` Command
    # Prompts llama3 model using the given prompt
    @commands.hybrid_command(
        name="llama", description="Prompt llama2 Uncensored AI Model"
    )
    @commands.is_owner()
    async def llama(self, ctx, prompt=None):
        # Defer the response
        await ctx.defer()

        # Check if prompt is none
        if prompt is None:
            # If it is, send an embed to the user to provide a prompt
            embed = discord.Embed(
                title=":x: Error",
                description="Please provide a prompt to ask llama2",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
        else:
            # Prompt llama2 AI
            result = ollama.generate(model="llama2-uncensored", prompt=prompt)
            response = result["response"]

            # Send an embed with the response
            embed = discord.Embed(
                title=f"{prompt}",
                description=f"{response}",
                color=discord.Color.green(),
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "llama3")


async def setup(client):
    await client.add_cog(AI(client))
