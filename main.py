import discord
import requests
from replit import db




# getting crypto data
def getCryptoPrices(crypto):
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
  r = requests.get(url=URL)
  data = r.json()

  # putting the cryptocurrencies and their prices in db
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
    #print(client.user.id)
    print('------')

# called whether there is a message in the chat
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Hi'):
    await message.channel.send('Hi Jay')

  # send crypto price directly 
  if message.content.lower() in db.keys():
    await message.channel.send(f'The current price of {message.content} is: {getCryptoPrices(message.content.lower())} USD')

  # list all the available coins
  if message.content.startswith('$list'):
    cryptoSupportedList = [key for key in db.keys()]
    await message.channel.send(cryptoSupportedList)



  # setting mutliple price alerts
  if message.content.startswith('$set '):
    messageList = message.content.split(' ')
    cryptoConcerned = messageList[1]

    priceTargets = []
    for i in range(len(messageList) - 2):
      priceTargets.append(int(messageList[2 + i]))


BOT_TOKEN = 'XXXXXX'
client.run(BOT_TOKEN)