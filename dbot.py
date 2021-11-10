import discord
import os
import youtube_dl
from discord.ext import commands

 
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
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
    	await channel.connect()
    	await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@bot.command()
async def leave(ctx):
    await bot.voice_clients[0].disconnect()

     
bot.run(os.environ['token'])