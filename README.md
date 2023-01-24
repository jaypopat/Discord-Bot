# Discord Crypto Bot
This is a simple Discord bot that uses the Discord API and Python's "requests" library to retrieve and display cryptocurrency prices from the CoinGecko API.

The bot also includes commands to display links to popular cryptocurrency exchanges such as Binance and Bitmart, as well as links to CoinGecko and CoinMarketCap.

The script requires a Discord bot token, which should be added to the BOT_TOKEN variable before running the script.

The bot utilizes the "on_message" event to listen for commands and the "on_ready" event to print the bot's name and ID to the console upon successful login.

To run the bot, you will need to have python3 and the following libraries installed:

discord
requests
To run the script, use the command:

python3 bot.py
You can also use repl.it to run the script without installing any library.

The bot supports the following commands:

- !binance : Send link of Binance
- !bitmart : Send link of Bitmart
- !cg : Send link of Coingecko
- !cmc : Send link of Coinmarketcap

The bot also supports the following commands for crypto prices:

- crypto name: Send current price of specific crypto in USD.
- Please note that the script utilizes a dictionary, "db", to store the current prices of each cryptocurrency. The prices are only updated when the script is run.

## An updated version of this is in the making which includes the features:
# Features
- Users can create their own portfolio by adding coins and their respective amounts
- Users can view their portfolio by typing the command !portfolio
- Users can see the current value of their portfolio in USD by typing the command !networth
- Users can add/remove coins from their portfolio
- Users can get the current price of any coin by typing the command !price [coin name]
- Users can get the links to popular crypto exchange websites like Binance, Bitmart, CoinGecko, CoinMarketCap by typing the command !binance, !bitmart, !cg, !cmc respectively

# The bot is operational but needs to be tested with several test cases and will be added to this repository in the next few weeks.
