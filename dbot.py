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
    
@bot.event()
async def on_message(message):
    if message.content.startswith(",골라"):
        vote = message.content[4:].split("/")
        await bot.send_message(message.channel, vote[0])
        for i in range(1, len(vote)):
            choose = await bot.send_message(message.channel, vote[i])
            await bot.add_reaction('👍')
    

     
bot.run(os.environ['token'])