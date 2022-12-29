import discord
from discord.ext import commands
import os

class Memberjoin(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.guild=0
        self.channel=0

    @commands.Cog.listener()
    async def on_ready(self):
        print("memberjoin: ON")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("Hihihi")
        guild= self.bot.get_guild(int(os.getenv('TEAM_GUILD')))
        channel= self.bot.get_channel(int(os.getenv('TEAM_GUILD_GENERAL')))
        if channel is not None:
            await channel.send(f'{member.mention} spotted!')

def setup(bot):
    bot.add_cog(Memberjoin(bot))