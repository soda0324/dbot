import discord
import os
import random
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

@bot.event()
async def on_message(message):
    if message.content.startswith(",투표"):
        vote = message.content[4:].split("/")
        channel = message.channel
        await channel.send("투표를 시작합니다.")
        for i in range(0, len(vote)):
            lastsend = await channel.send("```" + vote[i] + "```")
            await lastsend.add_reaction('✅')
            await lastsend.add_reaction('❌') 

    if message.author == bot.user:
        return
    
    if message.content.startswith('!골라'):
        message.content = message.content.replace("!골라 ","")
        messagesplit = message.content.split(",")
        msg = random.choice(messagesplit)+'을 골랐습니다.'
        await message.channel.send(msg)

    await bot.process_commands(message)

     
bot.run(os.environ['token'])