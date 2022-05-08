# bot.py
import os
import discord
from random import randrange
import time
from dotenv import load_dotenv
import subprocess

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(' ')
    print('skidbot.py succesfully connected!')
    print(' ')
    print('chatlog:')
    print('----------------------------------')
    
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  print(message.author)
  print(msg)
  print('----------------------------------')
  if msg.startswith("[commands]"):
        await message.channel.send("command list \n \n[commands] - it's obvious, how did you get here? \n[test] - tests the bot - if online, responds with 'ok' \n[repeat] - repeats what you say \n[swear] - responds with 'fuck you' \n[deaththreat] - responds with a death threat - joke!!!!")
  if msg.startswith("[test]"):
        await message.channel.send('ok')
  if msg.startswith("[repeat]"):
        await message.channel.send(msg[8:])
  if msg.startswith("[swear]"):
        await message.channel.send('fuck you')
  if msg.startswith("[deaththreat]"):
        await message.channel.send('kill yourself (for legal reasons, this is a joke.)')
        


client.run(TOKEN)
