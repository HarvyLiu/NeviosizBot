import discord
import os
import random
from dotenv import load_dotenv

load_dotenv() #reads .env file
intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')
