import discord
import os
from discord import guild
from discord.channel import VoiceChannel
from discord.ext import commands
import youtube_dl
 
bot = commands.Bot(command_prefix=',')
 
@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online,  activity=discord.Game(name="노가다"))

@bot.command()
async def 청소(ctx, amount : int):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")

    VoiceChannel=discord.utils.get(ctx.guild.voice_channel)
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await VoiceChannel.connect()
    
    ydl_opts = {
        'foramt': 'bestaudio/best',
        'postprocessors': [{
            'ket': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquallity': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FfmpegPCMAudio("song.mp3"))

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_coonected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected tp a voice channel.")

'''
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def join(ctx):
    print(ctx.author.voice)
    print(ctx.author.voice.channel)
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connet()
    else:
        await ctx.send("음성채널 없음")
'''


     
bot.run(os.environ['token'])