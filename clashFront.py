
import discord
import os
from clashMain import messageHandler

# GetToken
with open('token.txt','r') as f:
    lines = f.readlines()
token = lines[0]
print("Token: {}".format(token))

client = discord.Client()

activity = discord.Game(name="doing something", type=3)

@client.event
async def on_ready():
    activity = discord.Game(name="Not getting 2nd place!", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("[INFO] clashScouter {} is ready!".format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not os.name == 'nt' and message.channel.id == 649304929613250560: #If you are on linux and its this channel (#Test on BotTestingGround), ignore it
        return
    if message.content.lower().startswith("\\"):
        returnText = messageHandler(message.content)
        await message.channel.send(f"{returnText}")

client.run(token)



