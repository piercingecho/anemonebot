#importing files and discord library
#ensure that you first pip install py-cord
import os
import dotenv
import discord
from discord.ext import commands


#env variables
dotenv.load_dotenv()
print('loading DISCORD_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
print('loading TEAM_GUILD')
TEAM_GUILD = os.getenv('TEAM_GUILD')
CHANNEL_ID = os.getenv('TEAM_GUILD_GENERAL')


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)


@bot.slash_command(name="first_slash", guild_ids=[TEAM_GUILD]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")





#for loading/unloading cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

#for implementing each cog
for filename in os.listdir():
    if filename.endswith('cog.py'):
        bot.load_extension(f'{filename[:-3]}')

@bot.event
async def on_ready():
    print("Ready!")

bot.run(TOKEN)