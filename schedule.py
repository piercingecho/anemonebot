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
        description = "Generates one week of a team schedule."
        )
    @discord.option(
        "tourney",
        str,
        description = "Include Swim or Sink/Proving Grounds?",
        required = False,
        default = ''
    )
    async def schedule(self, ctx, tourney):
        d = datetime.now()
        await ctx.response.send_message("Schedule for next seven days:")
        
        #check for specific parameters
        if tourney is not None:
            if "sos" in tourney.lower():
                sosday = d 
                #add days so until wednesday (the date of SoS)
                sosday += timedelta(days = ((7 + -1 * d.weekday() + 2) % 7))
                await ctx.send('Swim or Sink: Wednesday ' + '<t:' + 
                    str(int(d.replace(day=sosday.day, hour=20, minute=0, second=0, microsecond=0).timestamp())) 
                    + '>')
            if "pg" in tourney.lower():
                pgday = d + timedelta(days= ((7 + -1 * d.weekday() + 4) % 7))
                await ctx.send('Proving Grounds: Friday ' + '<t:' + 
                    str(int(d.replace(day=pgday.day, hour=20, minute=0, second=0, microsecond=0).timestamp())) 
                    + '>')

        #general case
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
