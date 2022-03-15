import discord
import requests
import json




TOKEN = "ODM1MjYwNzIyMTUyOTk2OTA2.YIM3Kg.8usVftwAVwVjqXSmkt1mEqg2bFs"

client = discord.Client()



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>info cg'):
        await message.channel.send('https://www.coingecko.com/')
    if message.content.startswith('>info cmc'):
        await message.channel.send('https://coinmarketcap.com/')
    if message.content.startswith('>info coin'):
        await message.channel.send('Type the abbreviation of the coin')
        if message.content.startswith('eth'):
            browser = webdriver.Chrome()
            browser.get('https://www.coingecko.com/en/coins/ethereum')
            price = browser.find_element_by_id('price')
            price.text
#You will get the price of RM 89.39
#store it into a data frame
#import numpy as np
#import pandas as pd
#df = pd.DataFrame([["Product A", price.text]], columns=["Product","Price"])
            print(price)


             
       


       
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    #print(client.user.id)
    print('------')

client.run(TOKEN)


from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.coingecko.com/en/coins/ethereum')
price = browser.find_element_by_id('price')
price.text
#You will get the price of RM 89.39
#store it into a data frame
#import numpy as np
#import pandas as pd
#df = pd.DataFrame([["Product A", price.text]], columns=["Product","Price"])
print(price)


#Repeat the step for Product Page 2
#browser.get('https://<Competitor-Website>/ProductPage2')
#price = browser.find_element_by_id('price')
#Put in the product B price into the table
#df2 = pd.DataFrame([["Product B", price.text]], columns=["Product","Price"])
#df.append(df2)