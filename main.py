#imports time tracker
from datetime import datetime
#imports token retriever
import os
#imports discord library
import discord

#finds out current time: NY Timezone
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#stores token value & bot
my_secret = os.environ['TOKEN']

#creating an instance of client
client = discord.Client()

#registers the event
@client.event
#called for checking bot log-in
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
#received a message
async def on_message(message):
  #bot should only respond to non-author
  if message.author == client.user:
    return

  #handles message system
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
    await message.channel.send('The current time is' + current_time)
    
  if message.content.startswith('$goodnight'):
    await message.channel.send('GoodNight, Sleeptight!')

  if message.content.startswith('$goodmorning'):
    await message.channel.send('GoodMorning, Bright & Early!')

#retrieves token
client.run(my_secret)