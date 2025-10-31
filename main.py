import discord
import os
import random
from dotenv import load_dotenv

load_dotenv() #reads .env file
intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f"Logged in as a bot {client.user}")


