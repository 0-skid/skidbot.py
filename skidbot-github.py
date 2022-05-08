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
  if msg.startswith("[commands]" or "[commandlist]"):
        await message.channel.send("command list \n \n[commands] or [commandlist] - it's obvious, how did you get here? \n[test] - tests the bot - if online, responds with 'ok' \n[repeat] - repeats what you say \n[swear] - responds with 'fuck you' \n[deaththreat] - responds with a death threat - joke!!!! \n[25] - \n[thej] - sends a link to a random video from the j")
  if msg.startswith("[test]"):
        await message.channel.send('ok')
  if msg.startswith("[repeat]"):
        await message.channel.send(msg[8:])
  if msg.startswith("[swear]"):
        await message.channel.send('fuck you')
  if msg.startswith("[deaththreat]"):
        await message.channel.send('kill yourself (for legal reasons, this is a joke.)')        
  if msg.startswith("[25]"):
        await message.channel.send('+') 
  if msg.startswith("[thej]"):
        food = (randrange(7))
        if food == 0:
                await message.channel.send('https://www.youtube.com/watch?v=S6kXxR6J2lo')
        if food == 1:
                await message.channel.send('https://www.youtube.com/watch?v=WeGEEUM8AZU&t=25s')
        if food == 2:
                await message.channel.send('https://www.youtube.com/watch?v=AbxexjQe5a4')
        if food == 3:
                await message.channel.send('https://www.youtube.com/watch?v=7JRoEPhdZ-g')
        if food == 4:
                await message.channel.send('https://www.youtube.com/watch?v=JbTK8XOT3rg')
        if food == 5:
                await message.channel.send('https://www.youtube.com/watch?v=Bq98kMg6pFw')
        if food == 6:
                await message.channel.send('https://www.youtube.com/watch?v=ownNqUYb5LU&t=8s')
        


client.run(TOKEN)