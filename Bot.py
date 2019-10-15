import discord
import os

from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= "!s")

@Bot.command()
async def info(ctx):
    author = ctx.message.author
    await ctx.send("Этот бот в разроботке! Вы можете предложить свои идеи и высказать недовольство тут: https://discord.gg/ykdtjYY")
    
@Bot.command()
async def USE CODE(ctx):
    author = ctx.message.author
    await ctx.send("SFZD")

@Bot.command()
async def Артем(ctx):
    author = ctx.message.author
    await ctx.send("ЕБЛАН БЛЯТЬ КОНЧЕНЫЙ")

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
