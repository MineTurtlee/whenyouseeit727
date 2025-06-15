import discord # install discord.py
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True  # Required for message content access

client = commands.Bot(command_prefix="!", intents=intents) # You can change prefix to whatever you want *change command prefix*

@client.event
async def on_ready():
    print(f"Bot is ready. Logged in as {client.user} (ID: {client.user.id})") # Login message 

@client.command() # A simple ping command 
async def ping(ctx):
    await ctx.send(f"Pong! Latency: {round(client.latency * 1000)}ms") 

# Load cogs from the cogs/ folder if needed
if __name__ == "__main__":
    for filename in os.listdir("./cogs"): 
        if filename.endswith(".py"): # This will load in all the files that end with .py
            client.load_extension(f"cogs.{filename[:-3]}")

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
client.run("YOUR_TOKEN_HERE")
