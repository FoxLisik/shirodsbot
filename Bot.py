from __init__ import *

# Простой бот которы нужен только для примера либо же для "фундамента"

@Bot.event
async def on_ready():
    print("online")

@Bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.message.author.mention}")

Bot.run(token)