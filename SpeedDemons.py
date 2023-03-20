# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:16:14 2023

@author: Owner
"""
import discord
import os
import random
from dotenv import load_dotenv
import nest_asyncio
nest_asyncio.apply()

load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
TOKEN = os.getenv('TOKEN') 


import asyncio



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

 
@client.event
async def on_message(message):
    #membername = str(member_list[message.author])
    username = str(message.author.display_name)
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    #if message.author == client.user:
        #return
  
    if channel == "test" or channel=="general-chat":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
    if channel == "test":
        if user_message.lower() == "tell me a joke":
            jokes = [" Can someone please shed more\
            light on how my lamp got stolen?",
                     "Why is she called llene? She\
                     stands on equal legs.",
                     "What do you call a gazelle in a \
                     lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))
 
client.run(TOKEN)    

