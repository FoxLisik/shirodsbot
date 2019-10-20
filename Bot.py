import discord
import os

from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= "s!")



@Bot.command()
async def info(ctx):
    author = ctx.message.author
    await ctx.send("Этот бот в разроботке! Вы можете предложить свои идеи и высказать недовольство тут: https://discord.gg/ykdtjYY")

    
@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.Permissions.manage_guild.administrator:
        role = discord.utils.get(member.guild.roles, name='таймач😫')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

    

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
