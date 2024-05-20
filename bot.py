import discord
from discord.ext import commands
from dotenv import load_dotenv
from joke_gen import get_jokes
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



@bot.command()
async def dahekni(ctx, *, params: str = ""):
    # Default values
    category = "Any"
    language = "en"
    contains = None
    joke_type = None

    #parse params 
    if params : #if param not null
        param_list = params.split()#split the params into a list
        for param in param_list : #iterate over the list
            key, value = param.split("=")#split the key and value
            #checks type of key
            if key == "category":
                category = value
            elif key == "language":
                language = value
            elif key == "type":
                joke_type = value

    #print the params for debugging
    print(f"category: {category}, language: {language}, contains: {contains}, type: {joke_type}")
    



    #fetch the joke
    joke = get_jokes(category,language,contains, joke_type)
    await ctx.send(joke)


@bot.command()
async def anaHmar(ctx):
    """
    Provide information on how to use the joke command.
    """
    help_message = (
        "You can use the `!joke` command with the following options:\n"
        "`category`: Any, Programming, Miscellaneous, Dark\n"
        "`blacklist_flags`: nsfw, religious, political\n"
        "`type`: single, twopart\n\n"
        "'language': en, de, es, it, fr(LANGUAGES REMOVE THE ABILITY TO CHANGE THE CATEGORY)\n"
        "Example: `!dahekni category=Programming blacklist_flags=nsfw type=single`"
    )
    await ctx.send(help_message)

#bot cmd telling user the categories are programming misc dark pun spooky chrismas
@bot.command()
async def categories(ctx):
    await ctx.send("available categories are: Programming, Miscellaneous, Dark, Pun, Spooky, Christmas")



#run the bot
bot.run(TOKEN)