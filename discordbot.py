import googletrans
from distutils.log import error
import discord
from discord.ext import commands
from pprint import pprint
import httplib2
import os
from apiclient import discovery
import random
import asynci
o
TOKEN = os.environ['TOKEN']
APIKey = os.environ['APIKEY']
SpreadsheetId = os.environ['SHEET_ID']
ReplySheetName = os.environ['REPLY_SHEET']
RoleSheetName = os.environ['ROLE_SHEET']
guildid = os.environ['GUILD_ID']
rolemessageid = os.environ['ROLE_MESSAGE_ID']

#Google API
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
service = discovery.build(
    'sheets',
    'v4',
    http=httplib2.Http(),
    discoveryServiceUrl=discoveryUrl,
    developerKey=APIKey)

reactRange = RoleSheetName + '!A2:B'
rangeName = ReplySheetName + '!A2:D'

intent=discord.Intents.all()
client = commands.Bot(command_prefix = "!",intents=intent)




# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')

#添加身分組
@client.event
async def on_raw_reaction_add(payload):
    if str(payload.message_id) == rolemessageid:
        guild = client.get_guild(int(guildid))
        result = service.spreadsheets().values().get(
        spreadsheetId=SpreadsheetId, range=reactRange).execute()
        values = result.get('values', [])
        if not values:
            return
        for row in values:
            if payload.emoji.name == row[0]:
                role = discord.utils.get(guild.roles, name=row[1])
                if not role == None:
                    await payload.member.add_roles(role)

#移除身分組
@client.event
async def on_raw_reaction_remove(payload):
    if str(payload.message_id) == rolemessageid:
        guild = client.get_guild(int(guildid))
        result = service.spreadsheets().values().get(
        spreadsheetId=SpreadsheetId, range=reactRange).execute()
        values = result.get('values', [])
        if not values:
            return
        for row in values:
            if payload.emoji.name == row[0]:
                role = discord.utils.get(guild.roles, name=row[1])
                member = discord.utils.get(guild.members, id=payload.user_id)
                if not role == None:
                    await payload.member.remove_roles(role)



# 收到訊息時呼叫
@client.command()
async def translate(ctx, *, message):
    # 送信者為Bot時無視
    if ctx.message.author == client.user:
        print("逼逼逼")
        return
    else:
        print("執行成功!")
        translator = googletrans.Translator()
        if translator.detect(message).lang == SRCLanguage or SRCLanguage == '' or SRCLanguage == 'zh-CN': #判斷text是其他語言則翻成中文
            pass
        else:
            print(message)
            print(translator.detect(message).lang) 
            if translator.detect(message).lang != "zh-TW":
                remessage = translator.translate(message, dest='zh-TW').text #翻成中文
                await ctx.reply(remessage)
            if translator.detect(message).lang != "en":
                remessageen = translator.translate(message, dest='en').text #翻成英文
                await ctx.reply(remessageen)
# Bot起動
client.run(TOKEN)
