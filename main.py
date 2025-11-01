import discord
import os
import random
import asyncio
from dotenv import load_dotenv

load_dotenv() #reads .env file
intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    status_text = "銀月別再gay了"
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(status_text)
        )
    print(f"Logged in as a bot {client.user}")
    print(f"Status text set to {status_text}")

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
        await message.channel.send(f"Rolling Dice")
        dice_sides = uMessage.lower().split()[2]
        await asyncio.sleep(1)
        await message.channel.send(f"You rolled: {random.randint(1, int(dice_sides))}")

client.run(token)
