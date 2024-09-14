import discord
from discord.ext import commands
from pytubefix import YouTube
import os
import asyncio
import time
from utils.helper_functions import send_command_log, send_generic_log


class Media(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cog_name = "Media"
        self.queues = {}

    # Log that the cog was loaded
    @commands.Cog.listener()
    async def on_ready(self):
        await send_generic_log("Loaded 'Media' cog")

    # Propagate the error to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.client.on_command_error(ctx, error)

    # `join` Command
    # Makes the bot join the user's voice channel
    @commands.hybrid_command(name="join", description="Join the voice channel")
    async def join(self, ctx):
        # Check if the author is in a voice channel
        if ctx.author.voice:
            # Get the voice channel of the author
            channel = ctx.message.author.voice.channel

            # Connect to the voice channel
            await channel.connect()

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Joined VC",
                description="Joined VC, Use /play <url> to play audio",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`join` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)
        else:
            # If the author is not in a voice channel, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="You must be in a voice channel to run this command!",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "join")

    # `leave` Command
    # Makes the bot leave the active voice channel
    @commands.hybrid_command(name="leave", description="Leave the voice channel")
    async def leave(self, ctx):
        # Check if the bot is in a voice channel
        if ctx.voice_client:
            # Disconnect from the voice channel
            await ctx.guild.voice_client.disconnect()

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Left VC",
                description="Left VC",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`leave` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)
        else:
            # If the bot is not in a voice channel, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I am not in a VC at the moment. Use /join to add me to one!",
                color=discord.Color.blurple(),
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "leave")

    # `volume` Command
    # Get or set the volume of the audio
    # Provides the current volume if no volume percentage is provided
    # Default volume is 100%
    # Volume percentage must be between 0 and 200
    @commands.hybrid_command(
        name="volume", description="Get or set the volume of the audio"
    )
    async def volume(self, ctx, percent: float = None):
        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        # Check if the bot is in a voice channel
        if not voice:
            # If the bot is not in a voice channel, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I'm not connected to a voice channel.",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
            return
        elif not voice.is_playing():
            # If the bot is not playing audio, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I'm not currently playing anything.",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
            return

        # Check if the percent is None
        if percent is None:
            # If the percent is None, send a response embed to the command user
            embed = discord.Embed(
                title="Volume",
                description=f"The current volume is {voice.source.volume * 100}%",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`volume` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)
        else:
            # Set the volume
            voice.source.volume = percent / 100

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Volume",
                description=f"Volume set to {percent}%",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`volume` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "volume")

    # `pause` Command
    # Pauses the currently playing audio
    @commands.hybrid_command(
        name="pause", description="Pause the currently playing audio"
    )
    async def pause(self, ctx):
        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        # Check if the bot is playing audio
        if voice.is_playing():
            # Pause the audio
            voice.pause()

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Paused Audio",
                description="Paused Audio",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`pause` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)
        else:
            # If the bot is not playing audio, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I am not playing anything at the moment",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "pause")

    # `resume` Command
    # Resumes the currently paused audio
    @commands.hybrid_command(
        name="resume", description="Resume the currently paused audio"
    )
    async def resume(self, ctx):
        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        # Check if the bot is paused
        if voice.is_paused():
            # Resume the audio
            voice.resume()

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Resumed Audio",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`resume` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)
        else:
            # If the bot is not paused, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="No audio is paused at the moment!",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "resume")

    # `skip` Command
    # Skips the currently playing audio to the next audio in the queue
    @commands.hybrid_command(
        name="skip", description="Skip the currently playing audio"
    )
    async def skip(self, ctx):
        # Defer the response
        await ctx.defer()

        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        if voice:
            # Stop the audio
            voice.stop()

            # End the song and play the next one
            await self.end_song(ctx, ctx.guild, "tmp/temp_audio.mp3")

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Skipped Audio",
                description="Skipped Audio",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`skip` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)
        else:
            # If the bot is not playing audio, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I am not playing anything at the moment",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "skip")

    # `stop` Command
    # Stops the currently playing audio and clears the queue
    @commands.hybrid_command(
        name="stop", description="Stop playing audio (cannot be resumed)"
    )
    async def stop(self, ctx):
        # Defer the response
        await ctx.defer()

        # Clear the queue
        self.queues[ctx.guild.id] = []

        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        # Check if the bot has a voice instance
        if voice:
            # Stop the audio
            voice.stop()

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Stopped Audio",
                description="Stopped Audio",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"`stop` command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)
        else:
            # If the bot is not playing audio, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I am not playing anything at the moment",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "stop")

    # `play` Command
    # Plays audio from a given YouTube URL
    @commands.hybrid_command(name="play", description="Play audio from a YouTube URL")
    async def play(self, ctx, url):
        # Defer the response
        await ctx.defer()

        # Get the guild ID
        guild_id = ctx.guild.id

        # Check if the guild ID is in the queues
        if guild_id not in self.queues:
            # If not, add it
            self.queues[guild_id] = []

        # Append the URL to the queue
        self.queues[guild_id].append(url)

        # Get the voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        # Check if the bot is connected to a voice channel
        if not voice:
            # If not, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I'm not connected to a voice channel. Use /join to add me to one!",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
            return

        # Check if the bot is playing audio
        if not voice.is_playing():
            await self.play_next(ctx)

        # Send a response embed to the command user
        embed = discord.Embed(
            title="Added to Queue",
            description=f"Added to queue: {url}",
            color=discord.Color.green(),
        )
        embed.set_footer(
            text=f"'play' command was run by {ctx.message.author}",
            icon_url=ctx.author.avatar,
        )

        await ctx.send(embed=embed)

        # Log that the command was run
        await send_command_log(self, ctx, "play")

    # Function that plays the next audio in the queue
    async def play_next(self, ctx):
        # Get the guild ID
        guild_id = ctx.guild.id

        # Check if the guild ID is in the queues and if there are any URLs in the queue
        if guild_id in self.queues and self.queues[guild_id]:
            # Get the first URL in the queue
            url = self.queues[guild_id].pop(0)

            # Get the guild
            guild = ctx.message.guild

            # Get the voice instance
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

            # Download the audio from the URL
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path="tmp", filename="temp_audio.mp3")

            # Play the audio
            path = "tmp/temp_audio.mp3"
            voice.play(
                discord.FFmpegPCMAudio(path),
                after=lambda e: self.end_song(ctx, guild, path),
            )

            # Set the volume of the audio
            voice.source = discord.PCMVolumeTransformer(voice.source, 1)

            # Send a response embed to the command user
            embed = discord.Embed(
                title="Playing Audio",
                description=f"Playing: {url}",
                color=discord.Color.green(),
            )
            embed.set_footer(
                text=f"'play' command was run by {ctx.message.author}",
                icon_url=ctx.author.avatar,
            )

            await ctx.send(embed=embed)

    # Function that ends the currently playing audio
    def end_song(self, ctx, guild, path):
        # Get the voice instance
        os.remove(path)

        # Sleep to prevent FFMPEG from crashing
        time.sleep(2)

        future = asyncio.run_coroutine_threadsafe(self.play_next(ctx), self.client.loop)
        try:
            future.result()
        except Exception as e:
            print(f"Error occurred while trying to play the next song: {e}")


async def setup(client):
    await client.add_cog(Media(client))
