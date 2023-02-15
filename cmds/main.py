import discord
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(self.bot.latency)

async def setup(bot):
  await bot.add_cog(Main(bot))
