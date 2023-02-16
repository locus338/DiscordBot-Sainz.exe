import discord
import typing
import googletrans
import re
from discord.ext import commands
from core.classes import Cog_Extension
from discord.ext import commands
from threading import Thread
from flask import Flask, render_template
intent = discord.Intents.all()
intent.message_content = True
app = Flask(__name__, template_folder="Templates")
theRegex = re.compile("(http(s){0,}:\/\/){0,}discord\.gg")

class React(commands.Cog):
  def __init__(self, bot):
      self.bot = bot  
    
    @commands.command()
    async def hello(self, message):
        print("Hello")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        # 判斷反映貼圖給予相對應身分組
        if payload.message_id == 1072171521193300021:   
            if str(payload.emoji) == '✅':
                print("有進來")
                guild = bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                role = guild.get_role(1072098531910881290)  # 取得伺服器內指定的身分組
                payload.member.add_roles(role)  # 給予該成員身分組

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        if payload.message_id == 1072171521193300021:
            if str(payload.emoji) == '✅':
                # 取得伺服器
                guild = bot.get_guild(payload.guild_id)
                user = await guild.fetch_member(payload.user_id)
                await user.remove_roles(guild.get_role(1072098531910881290))


async def setup(bot):
  await bot.add_cog(React(bot))
