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
    if uMessage.lower() == "!joke":
        joke = os.popen("curl -H 'Accept: text/plain' https://icanhazdadjoke.com/").read()
        await message.channel.send(f"{joke}")
    lyrics_sentences = [
    "If I had a dime every time someone tried, me and my pride, I'd be richer than I am right now.",
    "But I live a life so sublime, all the fire's on my side, watch it flicker in my hand like, \"Wow\".",
    "This world is mine and jumping up the ladder is nothing but a matter of time.",
    "Where treachery and treason are just another reason to rhyme, embark on some havoc and charge up the master of minds; it's the perfect crime.",
    "Like dust on the radio, one day that's what we'll all be in the wind.",
    "I live my life like my soul is on stereo, press play, become emulsified in sin.",
    "They say, \"Video killed the radio star last night,\" 33, like a deer in those flashing lights, let Mr. Vox know that I'm still around, yeah I'm back, and I'm beaming the radio demon's in town.",
    "Now, I wouldn't lie or deny that my eyes are on the prize, and I promise you, I'll stand my ground.",
    "But I'm not to fight all the lives that reside within these heights; don't you worry, love, you have my vow.",
    "This world is mine; the cretins will have a season and they will shine, but we can become a beacon for all the blind.",
    "A demon of my allegiance can burn the sky; this is so divine.",
    "They say, \"Video killed the radio star last night,\" 33, like a deer in those flashing lights, let Mr. Vox know that I'm still around, yeah I'm back, and I'm beaming the radio demon's in town.",
    "In town, demons in town, in town."]
    if uMessage.lower() == "!quote":
        await message.channel.send(random.choice(lyrics_sentences))
    

@client.event
async def on_message_delete(message):
    channel = discord.utils.get(message.guild.channels, name="mod-logs")
    await channel.send(f"<:alastor_smile:1433856260377411645> Deleted<:delete295:1434047047073533972> Message by {message.author.mention} deleted in {message.channel.mention}: ```{message.content}```")






client.run(token)

