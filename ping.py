import discord
from discord.ext import commands
import os


class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command(
        name = "ping",
        guild_ids=[os.getenv('TEAM_GUILD')],
        description = "Displays response time")
    async def ping(self, ctx):
        ping1 = f"{str(round(self.bot.latency * 1000))} ms"
        embed = discord.Embed(title = "**Pong!**", description = "**" + ping1 + "**", color = 0xafdafc)
        await ctx.response.send_message(embed = embed)

def setup(bot):
    bot.add_cog(Ping(bot))