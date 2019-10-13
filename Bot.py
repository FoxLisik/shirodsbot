import discord
import os

from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= "!s")

@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send("q")

token = os.environ.get('BOT TOKEN')
