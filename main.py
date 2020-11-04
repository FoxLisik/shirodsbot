#https://discordapp.com/api/oauth2/authorize?client_id=632903118014775317&permissions=8&scope=bot
#

import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= '!')

@Bot.event
async def hello(ctx):
    author = ctx.message.author
    await Bot.send('Привет')

# RUN
Bot = MyClient()
Bot.run(TOKEN)

