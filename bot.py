import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


#load env variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')




#define intents
intents = discord.Intents.default()
intents.message_content = True #make bot able to read messages

# create bot instance
bot = commands.Bot(command_prefix='!',intents=intents)


#event that triggers when bot is ready
@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')


#basic command example
@bot.command()
async def hello(ctx):
    await ctx.send('bela3')

#run the bot
bot.run(TOKEN)