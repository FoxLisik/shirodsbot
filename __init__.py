import discord, configparser
from discord.ext import commands

config = configparser.ConfigParser() # Процесс объявления констант из файла config.ini
config.read('config.ini')
token = config['DEFAULT']['token']
Bot = commands.Bot(command_prefix= config['DEFAULT']['prefix'])

link = "https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8"   # Ссылка на приглашение бота на сервер (константа)