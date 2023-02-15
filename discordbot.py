import os
import discord
import typing
import googletrans
import re
from discord.ext import commands
from threading import Thread
from flask import Flask, render_template
intent = discord.Intents.all()
intent.message_content = True
app = Flask(__name__, template_folder="Templates")
theRegex = re.compile("(http(s){0,}:\/\/){0,}discord\.gg")


def run():
    app.run(host='0.0.0.0', port=10000, use_reloader=False, debug=True)


def stay():
    thread = Thread(target=run)
    thread.start()


class Bot(commands.Bot):
    def __init__(self):        
        for Filename in os.listdir('./cmds'):
            if Filename.endswith('.py'):
                self.load_extension(F'cmds.{Filename[-3]}')
        super().__init__(command_prefix="~", intents=discord.Intents.all(), help_command=None)


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, message):
        print("Hello")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not (theRegex.match(message.content) == None):
            await message.delete()
        print("onMessage")

    @commands.Cog.listener()
    async def on_ready(self):
        print('目前登入身份：', bot.user)
        game = discord.Game('EK的電腦')
        # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
        await self.bot.change_presence(status=discord.Status.online, activity=game)
    
    @commands.command()
    async def translate(ctx, *, message: typing.Optional[str] = None):
        print("translate")
        if message is None:
            await ctx.reply(self,"請輸入要翻譯的內容")
            return
        if ctx.message.author == bot.user:
            print("逼逼逼")
            return
        else:
            print("執行成功!")
            translator = googletrans.Translator()
            if translator.detect(message).lang == 'zh-CN':  # 判斷text是其他語言則翻成中文
                pass
            print(translator.detect(message).lang)
            if translator.detect(message).lang != "zh-TW":
                remessage = translator.translate(
                    message, dest='zh-TW').text  # 翻成中文
                await ctx.reply(remessage)
            if translator.detect(message).lang != "en":
                remessageen = translator.translate(message, dest='en').text  # 翻成英文
                await ctx.reply(remessageen)
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


    @commands.command(aliases=['PING', 'PINGS', 'pings', 'Ping', 'Pings'])
    async def ping(self,ctx):
        await ctx.send(F'{round(bot.latency*1000)}ms')


        

    @commands.command()
    async def help(self,ctx):
        await ctx.send(f"尚在製作中...")


@app.route('/')
def index():
    return render_template('index.html')


SRCLanguage = "zh-TW"

# 收到訊息時呼叫

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    bot = Bot()
    stay()
