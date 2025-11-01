import discord
import os
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv() #reads .env file
intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    status_text = "discord.py"
    channel = client.get_channel(1434044899325513738)
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(status_text)
        )
    print(f"Logged in as a bot {client.user}")
    print(f"Status text set to {status_text}")
    await channel.send(f"Bot {client.user} is online! :white_check_mark:")

@client.event
async def on_message(message):
    uName = str(message.author)
    uMessage = str(message.content)
    channel = str(message.channel.name)
    dice_sides = 0
    greetings = ["Hope you have a nice day!!", "Good luck on everything!", "I'm sure nothing can stop you today🔥🔥🔥.", "Spend your time wisely and I bet things will go smoothly~."]
    print(f"Message {uMessage} by {uName} on {channel}")
    if message.author == client.user:
        return
    if uMessage.lower() == "hello" or uMessage.lower() == "hi":
        await message.channel.send(f"Hi {message.author.mention}!\n{random.choice(greetings)}")
        return
    if uName == "ilovevtuber14." and "寶貝" in uMessage.lower():
        await message.channel.send(f"好了銀月別再gay了")
    if "!dice" in uMessage.lower():
        dice_sides = uMessage.lower().split()[1]
        await message.channel.send(f"Rolling Dice of {dice_sides}......")
        await asyncio.sleep(1)
        try:
            await message.channel.send(f"You rolled: {random.randint(1, int(dice_sides))}")
        except:
            await message.channel.send(f"Wait... TF is {dice_sides}?\nI suppose you didn't enter a valid number or format?\nThe format should be: !dice [number]")
    if "!echo" in uMessage.lower():
        echo_text = uMessage.split()[1]
        await message.delete()
        await message.channel.send(echo_text)
    if uMessage.lower() == "!weather":
        weather = os.popen("curl -s wttr.in/Taipei?0").read()
        await message.channel.send(f"The weather in Taipei is:\n```{weather}```")
    

@client.event
async def on_message_delete(message):
    channel = discord.utils.get(message.guild.channels, name="mod-logs")
    await channel.send(f"<:alastor_smile:1433856260377411645> Deleted<:delete295:1434047047073533972> Message by {message.author.mention} deleted in {message.channel.mention}: ```{message.content}```")






client.run(token)

