import discord
import requests
from replit import db

# getting crypto data
def getCryptoPrices(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
  r = requests.get(url=URL)
  data = r.json()

  for i in range(len(data)):
    db[data[i]['id']] = data[i]['current_price']

  if crypto in db.keys():
    return db[crypto]
  else:
    return None

# instantiate a discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# called whether there is a message in the chat
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!binance'):
    await message.channel.send('https://www.binance.com/en')
  if message.content.startswith('!bitmart'):
    await message.channel.send('https://www.bitmart.com/')
  if message.content.startswith('!cg'):
    await message.channel.send('https://www.coingecko.com/')
  if message.content.startswith('!cmc'):
    await message.channel.send('https://coinmarketcap.com/')

  if message.content.lower() in db.keys():
    await message.channel.send(f'The current price of {message.content} is {getCryptoPrices(message.content.lower())} USD')
  
BOT_TOKEN = 'XXXXXXXXXXXXXXXX'
client.run(BOT_TOKEN)
