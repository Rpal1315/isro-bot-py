import discord
from discord.ext import commands
import datetime
import pytz
import os
from flask import Flask
from threading import Thread
import random
import time
app = Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"

Thread(target=app.run, args=("0.0.0.0", 8080)).start()

bot = commands.Bot(command_prefix='c!')
bot.remove_command('help')
client = discord.Client

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name='ISRO Server')
    )
    print('ISRO bot is online')

@bot.command()
async def punch(ctx, in_or_out=None):
	if in_or_out == 'in':
		await bot.get_channel(920195410310606908).send(
		    f'{ctx.author.mention} online.')
	elif in_or_out == 'out':
		await bot.get_channel(920195410310606908).send(
		    f'{ctx.author.mention} offline')
	else:
		await ctx.send(
		    'Not a valid option. Please type in either on/off or online/offline.'
		)
@bot.command()
async def chklst(ctx, mis=None):
	if mis == "G2" or mis == "g2":
		embed = discord.Embed(
			title = "Gaganyaan Checklist",
			color = 0x00e0ff)
		embed.add_field(name = "1.", value = "Fuel Pump  ---  IDLE", inline = False)
		embed.add_field(name = "2",value = "Trajectory  ---  CHECKED", inline = False)
		embed.add_field(name = "3",value = "Monitor Status --- MANUAL", inline = False)
		embed.add_field(name = "4",value = "Onboard Computer Status --- ONLINE", inline = False)
		embed.add_field(name = "5",value = "Comms  ---  ONLINE",inline = False)

		await ctx.send(embed=embed)
@bot.command()
async def help(ctx):
		embed = discord.Embed(
			title = "Help. I was created by Qatari3",
			color = 0x00e0ff
		)
		embed.add_field(name = "c!help", value = "This command")
		embed.add_field(name = "c!punch <in/out>", value = "Use this command to punch in or out")
		embed.add_field(name = "c!chklst <mission-code>", value = "This command gives the checklist. Codes for missions are available in the server")

		await ctx.send(embed = embed)

my_secret = os.environ['BOT_TOKEN']
bot.run(my_secret)
