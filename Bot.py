import discord
import os

from discord.ext import commands
from discord.ext.commands import Bot


Bot = commands.Bot(command_prefix= "s!")
    
@Bot.command()
async def test(ctx):
    author = ctx.message.author
    await ctx.send("test")

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
