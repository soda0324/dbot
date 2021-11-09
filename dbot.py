import discord
import os
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