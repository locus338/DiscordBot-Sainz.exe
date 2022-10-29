import os
import typing
import googletrans
import discord
from discord.ext import commands

token = os.getenv("TOKEN")


SRCLanguage = "zh-TW"


intent = discord.Intents.all()
client = commands.Bot(command_prefix="~", intents=intent)


# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')


# 收到訊息時呼叫
@client.command(aliases=['trans', 't'])
async def translate(ctx, *, message: typing.Optional[str] = None):
    if message is None:
        await ctx.reply("請輸入要翻譯的內容")
        return

    # 送信者為Bot時無視
    if ctx.message.author == client.user:
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

client.run(token)
