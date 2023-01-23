
# Crypto Portfolio Discord Bot


This is a simple Discord bot that allows users to create and manage their own crypto portfolio.

Features



# Features
- Users can create their own portfolio by adding coins and their respective amounts
- Users can view their portfolio by typing the command !portfolio
- Users can see the current value of their portfolio in USD by typing the command !networth
- Users can add/remove coins from their portfolio
- Users can get the current price of any coin by typing the command !price [coin name]
- Users can get the links to popular crypto exchange websites like Binance, Bitmart, CoinGecko, CoinMarketCap by typing the command !binance, !bitmart, !cg, !cmc respectively

# Getting started
To use this bot, you will need to have a Discord account and create a bot on the Discord Developer Portal. Once you have your bot's token, you can invite the bot to your server and begin using it.

You will also need to have Python and the discord.py library installed on your machine.




## Usage
Once the bot is added to your server, users can create their own portfolio by typing the command !add [coin name] [amount]. For example, !add BTC 2.5 will add 2.5 BTC to the user's portfolio.

Users can view their portfolio by typing the command !portfolio. This will display a list of all the coins in the user's portfolio and their respective amounts.

Users can see the current value of their portfolio in USD by typing the command !networth. This will display the total value of the user's portfolio in USD, calculated using the current prices of the coins.

Users can add/remove coins from their portfolio by using the command !add [coin name] [amount] and !remove [coin name] [amount] respectively.

Users can get the current price of any coin by typing the command !price [coin name]. For example, !price BTC will display the current price of Bitcoin in USD.

Users can get the links to popular crypto exchange websites like Binance, Bitmart, CoinGecko, CoinMarketCap by typing the command !binance, !bitmart, !cg, !cmc respectively.



## Note
The bot uses the CoinGecko API to get the prices of the coins. The API returns prices in USD, if you wish to use other currencies, you'll have to change the code accordingly.






# Additional Information
- The code uses the discord.py library to interact with the Discord API
- The bot is not persistent and will not save the user's portfolio after the bot is closed.
- The bot is case-sensitive for the crypto-currency names
- The bot does not validate if the coins entered by the user are valid or not.

# Conclusion
This bot is a simple tool that allows users to create and manage their own crypto portfolio in a Discord server. It's a great way to keep track of your crypto investments and stay updated with the latest prices.




