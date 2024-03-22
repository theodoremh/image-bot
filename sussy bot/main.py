import discord
from discord.ext import commands
import os
from second import detect
intents = discord.Intents.default()
intents.message_content = True
from second import detect

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def get_attachment(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            await attachments.saved("sussy/"+attachments.filename)
            
            await ctx.send(detect("sussy/"+attachments.filename))
            
    else:
        await ctx.send("Images not found!")
@bot.command()
async def animals(ctx):
    await ctx.send()




bot.run("MTE1MjIzMDEyODU1NDg2ODc3Ng.G4suEy.62uSB4XU-ZITUJxOl0IwnBqjYmtjzr0NZRHx8k")           