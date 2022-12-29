import discord
from discord.ext import commands
import os
from datetime import datetime, timedelta


class Schedule(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command(
        name = "schedule",
        guild_ids=[os.getenv('TEAM_GUILD')],
        description = "Generates one week of a team schedule.")
        
    async def schedule(self, ctx):
        d = datetime.now()
        await ctx.response.send_message("Schedule for next seven days:")
        for i in range(7):
            #day of week
            day = d.strftime('%A')    
            await ctx.send(
                    'Availability: ' + day + 
                    ' ' + '<t:' + 
                    str(int(d.replace(day=d.day, hour=19, minute=0, second=0, microsecond=0).timestamp())) 
                    + '>')

            #to be implemented: reaction on each message
            '''
            await message.add_reaction(u"\U0001F44D")
            await message.add_reaction(u"\U0001F44E")
            await message.add_reaction(u"\U0000003F")
            '''
            d += timedelta(days=1)

def setup(bot):
    bot.add_cog(Schedule(bot))