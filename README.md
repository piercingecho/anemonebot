# Discord Bot for Splatoon eSports

This is the source code for a discord bot initially made for a competitive team for the third-person shooter Splatoon 3, Anemone Spotted. It has various commands to streamline captaining for team-based games in general.

## Requirements and Directions for Setup
### Packages

You will need to download python and pip in their latest versions. Afterwards, type `pip install pycord` into the command prompt.

### Discord Token

You will need to create a Discord token, and then invite the token to the server that you will use it in. Use the following link for more guidelines: https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

### Directory setup

Take all files from this repository, and unzip them into a given directory.
Create a directory named "Cogs", and place every file not named 'bot.py' into that directory. Ensure the folder "Cogs" is in the same directory as "bot.py."

### .env setup

You will also need to create a .txt file with the following text exactly. On each line, replace the information to the right of the = with the data detailed within <>.

DISCORD_TOKEN = <token copy-pasted from discord dashboard, as described in the above link.>
TEAM_GUILD = <From discord developer mode, copy the ID of the guild that will utilize this bot. This is the same guild you invited it to earlier.>
TEAM_GUILD_GENERAL = <from discord developer mode, copy the ID of the text channel you want messages to new members to be sent.>

Afterwards, rename the extension from '.txt' to '.env' and place it in the same directory as bot.py.

## To Run the Program

In the command prompt of your device, change directory to where you unzipped the repository initially. For Windows, issue the command `python bot.py`. Alternatively, issue `python3 bot.py`. Leave the window open (or run using `nohup`) as you would like the bot's functionality to continue.

## Version Updates
1.1 - Planned for future. Will implement creating map lists for the game Splatoon 3, given a file of associated map pools.

1.0 - Initial version that gives reactable schedule messages based on day of week.
