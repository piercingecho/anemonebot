import discord
from discord.ext import commands
import os
import sys
# so that maplist can be imported from directory above
sys.path.append("..")
import maplist

class Generatemaplist(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command(
        name = "generatemaplist",
        guild_ids=[os.getenv('TEAM_GUILD')],
        description = "Displays response time")
    @discord.option(
        "mapfile",
        str,
        description = "Which maplist to use? (without .csv)",
        required = True,
        default = ''
    )
    @discord.option(
        "num_stages",
        str,
        description = "Number of maps to generate?",
        required = True,
        default = ''
    )
    async def generatemaplist(self, ctx, mapfile, num_stages):
        allstages = maplist.Maplist(mapfile)
        random_order = allstages.randomMaps(int(num_stages))
        s = ""
        i = 1
        for stagemode in random_order:
            s += f"Game {i}: {stagemode[0]} on {stagemode[1]}\n"
            i += 1
        await ctx.response.send_message(f"Maplist size {num_stages} from {mapfile}:")
        await ctx.send(s)


def setup(bot):
    bot.add_cog(Generatemaplist(bot))

def main():
    a = maplist.Maplist('allmaps')

if __name__ == '__main__':
    main()