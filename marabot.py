import discord
import time
from discord.ext.commands import Bot

TOKEN = "MTAxOTYyMDc1NjQwMzAxNTcxMA.GCL0hZ.ni1Sgth1OfPJhUNDYjZ8ov0e5EA2LOKHyBD2QI"

intents = discord.Intents.all()

# !로 시작하면 명령어로 인식
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')
  

# !hello 명령어 처리
@bot.command()
async def 차돌(ctx):
  endt = time.time()
  waitt = endt-1663169956.9487429
  waitt = round(waitt,3)
  await ctx.reply(f'차돌짬뽕 안먹은지 {waitt}초째!!!')
  begint = time.time()

# !bye 명령어 처리
@bot.command()
async def 마라(ctx):
  begint = time.time()
  await ctx.reply(f'타이머 시작{begint}')

bot.run(TOKEN)