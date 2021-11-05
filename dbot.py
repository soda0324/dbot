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

async def 핑(ctx):
    await ctx.send(f'```ping : {round(bot.latency * 1000)}ms```')

     
bot.run(os.environ['token'])