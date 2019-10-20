import discord
import os

from discord.ext import commands
from discord.ext.commands import Bot


Bot = commands.Bot(command_prefix= "s!")


@Bot.event()
async def on_ready():
    print('shiro online')
    
@Bot.command()
async def info(ctx):
    author = ctx.message.author
    await ctx.send("Этот бот в разроботке! Вы можете предложить свои идеи и высказать недовольство тут: https://discord.gg/ykdtjYY")

@Bot.command()
async def ping(ctx):
    await ctx.send('Ping = {round(Bot.latency * 1000)}ms!')


token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
