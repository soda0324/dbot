import discord
import os
from discord.ext import commands
 
bot = commands.Bot(command_prefix=',')
 
@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online,  activity=discord.Game(name="게임"))

@bot.command()
async def 청소(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="채팅청소", description="총 " + amount + " 채팅 제거", color = 0x000000) 
    await ctx.send(embed=embed)
    

     
bot.run(os.environ['token'])