import discord
from discord.ext import commands


client = discord.Client()
bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print('We have logged is as {0.user}'.format(client))


@bot.command()
async def ping(message):
    await message.send("Pong!")


bot.run('NjYzNTE3ODgwNzkyMzgzNTAy.XhJrqw.KQqZJ0ktm3_Y2gxR1zeyu5w9nYk')
