import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['PING', 'PINGS', 'pings', 'Ping', 'Pings'])
    async def ping(self,ctx):
        await ctx.send(F'{round(bot.latency*1000)}ms')
        
def setup(bot):
    bot.add_cog(Main(bot))
