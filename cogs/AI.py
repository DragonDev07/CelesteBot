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

    # `llama` Command
    # Prompts llama2-uncensored model using the given prompt
    @commands.hybrid_command(
        name="llama", description="Prompt llama2 Uncensored AI Model"
    )
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
            embed.set_footer(
                "Generated with llama2-uncensored AI Model in {result['time']} seconds"
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "llama")

    # `coder` Command
    # Prompts the deepseek-coder-v2 model using the given prompt
    @commands.hybrid_command(
        name="coder", description="Prompt deepseek-coder-v2 AI Model"
    )
    async def coder(self, ctx, prompt=None):
        # Defer the response
        await ctx.defer()

        # Check if prompt is none
        if prompt is None:
            # If it is, send an embed to the user to provide a prompt
            embed = discord.Embed(
                title=":x: Error",
                description="Please provide a prompt to ask deepseek-coder-v2",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
        else:
            # Prompt deepseek-coder-v2 AI
            result = ollama.generate(model="deepseek-coder-v2", prompt=prompt)
            response = result["response"]

            # Send an embed with the response
            embed = discord.Embed(
                title=f"{prompt}",
                description=f"{response}",
                color=discord.Color.green(),
            )
            embed.set_footer(
                "Generated with deepseek-coder-v2 AI Model in {result['time']} seconds"
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "coder")


async def setup(client):
    await client.add_cog(AI(client))
