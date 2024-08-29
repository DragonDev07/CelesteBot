import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from pytubefix import YouTube
import os


class Media(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Log that this cog was loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("The 'Media' cog has been loaded")

    # Propagate the error to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.bot.on_command_error(ctx, error)

    # Command that makes the bot join the vc
    @commands.hybrid_command(name="join", description="Join the voice channel")
    async def join(self, ctx):
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

        # Print that the command was run
        print(f"The 'join' command was run by {ctx.message.author}")

    @commands.hybrid_command(name="leave", description="Leave the voice channel")
    async def leave(self, ctx):
        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

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

        # Print that the command was run
        print(f"The 'leave' command was run by {ctx.message.author}")

    # Command that pauses the current playing audio
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

        # Print that the command was run
        print(f"The 'pause' command was run by {ctx.message.author}")

    # Command that resumes paused audio
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

        # Print that the command was run
        print(f"The 'resume' command was run by {ctx.message.author}")

    # Command that playes given YouTube URL
    @commands.hybrid_command(name="play", description="Play audio from a YouTube URL")
    async def play(self, ctx, url):
        # Defer the response
        await ctx.defer()

        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        # Check if the bot is in a voice channel
        if not voice:
            # If the bot is not in a voice channel, send a response embed to the command user
            embed = discord.Embed(
                title="Error",
                description="I'm not connected to a voice channel. Use /join to add me to one!",
                color=discord.Color.red(),
            )

            await ctx.send(embed=embed)
            return

        # Get guild instance
        guild = ctx.message.guild

        # Get youtube video
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path="tmp", filename="temp_audio.mp3")

        # Play downloaded audio file
        path = "tmp/temp_audio.mp3"
        voice.play(discord.FFmpegPCMAudio(path), after=lambda x: end_song(guild, path))
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

        # Print that the command was run
        print(
            f"The `play` command was run by {ctx.message.author}, playing video {url}"
        )

    # Command that stops playing audio (deletes file, cannot be resumed)
    @commands.hybrid_command(
        name="stop", description="Stop playing audio (cannot be resumed)"
    )
    async def stop(self, ctx):
        # Defer the response
        await ctx.defer()

        # Get voice instance
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        # Pause the audio
        voice.pause()

        # End the song
        end_song(ctx.guild, "tmp/temp_audio.mp3")

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

        # Print that the command was run
        print(f"The 'stop' command was run by {ctx.message.author}")

    # Command to get or set volume of the audio
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
        if percent == None:
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

        # Print that the command was run
        print(
            f"The 'volume' command was run by {ctx.message.author} to set the volume to {percent}%"
        )


async def setup(client):
    await client.add_cog(Media(client))


def end_song(guild, path):
    os.remove(path)
