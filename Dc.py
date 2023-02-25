import discord
from discord.ext import commands
from discord import app_commands
from discord.channel import *
import requests
import os
import os.path

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



@bot.command()
async def instagram(ctx, service, quantitys, links):
    if service == 'followers':
            if int(quantitys) >= 100:
                if int(quantitys) <= 300000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.003
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '9766', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 100:
                await ctx.send('Minimum quantity: 100 - Maximum: 300000')
                if int(quantitys) > 300000:
                    await ctx.send('Minimum quantity: 100 - Maximum: 300000')
    if service == 'likes':
            if int(quantitys) >= 10:
                if int(quantitys) <= 100000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0015
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '4790', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 10:
                await ctx.send('Minimum quantity: 10 - Maximum: 100000')
                if int(quantitys) > 100000:
                    await ctx.send('Minimum quantity: 10 - Maximum: 100000')
    else:    
        hp = """Command not found, maybe try using small letters  
        If you want help use /help instagram"""
        await ctx.send(hp)



@bot.command()
async def tiktok(ctx, service, quantitys, links):
    if service == 'views':
            if int(quantitys) >= 100:
                if int(quantitys) <= 1000000000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0001
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '4865', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 100:
                await ctx.send('Minimum quantity: 100 - Maximum: 1000000000')
                if int(quantitys) > 1000000000:
                    await ctx.send('Minimum quantity: 100 - Maximum: 1000000000')
    if service == 'followers':
            if int(quantitys) >= 10:
                if int(quantitys) <= 1000000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.006
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '5717', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 10:
                await ctx.send('Minimum quantity: 10 - Maximum: 1000000')
                if int(quantitys) > 1000000:
                    await ctx.send('Minimum quantity: 10 - Maximum: 1000000')
    if service == 'likes':
            if int(quantitys) >= 10:
                if int(quantitys) <= 100000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0025
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '5699', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 10:
                await ctx.send('Minimum quantity: 10 - Maximum: 100000')
                if int(quantitys) > 100000:
                    await ctx.send('Minimum quantity: 10 - Maximum: 100000')
    else:    
        hp = """Command not found, maybe try using small letters  
        If you want help use /help tiktok"""
        await ctx.send(hp)




@bot.command()
async def twitch(ctx, service, quantitys, links):
    if service == 'followers':
            if int(quantitys) >= 20:
                if int(quantitys) <= 200000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0025
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '5780', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 20:
                await ctx.send('Minimum quantity: 20 - Maximum: 200000')
                if int(quantitys) > 200000:
                    await ctx.send('Minimum quantity: 20 - Maximum: 200000')
    else:    
        hp = """Command not found, maybe try using small letters  
        If you want help use /help twitch"""
        await ctx.send(hp)





@bot.command()
async def twitter(ctx, service, quantitys, links):
    if service == 'followers':
            if int(quantitys) >= 200:
                if int(quantitys) <= 500000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0035
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '5249', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 200:
                await ctx.send('Minimum quantity: 200 - Maximum: 500000')
                if int(quantitys) > 500000:
                    await ctx.send('Minimum quantity: 200 - Maximum: 500000')
    if service == 'likes':
            if int(quantitys) >= 20:
                if int(quantitys) <= 20000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0035
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '7983', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 20:
                await ctx.send('Minimum quantity: 20 - Maximum: 20000')
                if int(quantitys) > 20000:
                    await ctx.send('Minimum quantity: 20 - Maximum: 20000')
    else:    
        hp = """Command not found, maybe try using small letters  
        If you want help use /help twitter"""
        await ctx.send(hp)



@bot.command()
async def telegram(ctx, service, quantitys, links):
    if service == 'members':
            if int(quantitys) >= 100:
                if int(quantitys) <= 100000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0025
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '7508', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 100:
                await ctx.send('Minimum quantity: 100 - Maximum: 100000')
                if int(quantitys) > 100000:
                    await ctx.send('Minimum quantity: 100 - Maximum: 100000')
    else:    
        hp = """Command not found, maybe try using small letters  
        If you want help use /help telegram"""
        await ctx.send(hp)


@bot.command()
async def youtube(ctx, service, quantitys, links):
    if service == 'views':
            if int(quantitys) >= 100:
                if int(quantitys) <= 500000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.0025
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '9236', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 100:
                await ctx.send('Minimum quantity: 100 - Maximum: 500000')
                if int(quantitys) > 500000:
                    await ctx.send('Minimum quantity: 100 - Maximum: 500000')
    if service == 'subscribers':
            if int(quantitys) >= 50:
                if int(quantitys) <= 3000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.010
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '5080', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 50:
                await ctx.send('Minimum quantity: 50 - Maximum: 3000')
                if int(quantitys) > 3000:
                    await ctx.send('Minimum quantity: 50 - Maximum: 3000')
    if service == 'likes':
            if int(quantitys) >= 10:
                if int(quantitys) <= 50000:
                    id=ctx.author.id
                    print(id)
                    txt=str(id)+'.txt'
                    file1 = open( str(txt),"r")
                    bal = file1.readline()
                    file1.close()
                    print(bal)
                    pay=int(quantitys)*0.003
                    print(pay)
                    res = float(bal) - pay
                    print(res)
                    if res < 0:
                        await ctx.send("Not Enought Balance! Open ticket to add balance!")
                    if res > 0:
                        r = requests.post('https://secsers.com/api/v2', data={"key": 'dc68bf146a22e76dbe0240b7be4f5194', "action" :'add', "service": '9811', "quantity": {quantitys}, "link": {links}} )
                        file1 = open( str(txt),"w")
                        file1.write(str(res))
                        file1.close()
                        await ctx.send("Your order was received")
            if int(quantitys) < 10:
                await ctx.send('Minimum quantity: 10 - Maximum: 50000')
                if int(quantitys) > 50000:
                    await ctx.send('Minimum quantity: 10 - Maximum: 50000')
    else:    
        hp = """Command not found, maybe try using small letters  
        If you want help use /help youtube"""
        await ctx.send(hp)




@bot.command()
async def help(ctx, service):
    if service == "instagram":
        hp = """/instagram service quantity link

services:

Instagram Followers 3$ Quantity: 100 - 300000 

Instagram Likes 1.5$ Quantity: 10 - 100000

Open Ticket to add Balance"""
        await ctx.send(hp)
    if service == "tiktok":
        hp = """/tiktok service quantity link

services:

Tiktok Followers 6$ Quantity: 100 - 1000000 

Tiktok Likes 2.5$ Quantity: 10 - 100000

Tiktok Views 0.1$ Quantity: 100 - 1000000000

Open Ticket to add Balance"""
        await ctx.send(hp)
    if service == "twitch":
        hp = """/twitch service quantity link
services:

Twitch Followers 2.5$ Quantity: 20 - 200000 

Open Ticket to add Balance"""
        await ctx.send(hp)
    if service == "telegram":
        hp = """/telegram service quantity link

services:

Telegram Members 2.5$ Quantity: 100 - 100000 

Open Ticket to add Balance"""
        await ctx.send(hp)
    if service == "youtube":
        hp = """/youtube service quantity link

services:

Youtube Subscribers 10$ Quantity: 50 - 3000 

Youtube Likes 3$ Quantity: 10 - 50000

Youtube Views 2.5$ Quantity: 100 - 500000

Open Ticket to add Balance"""
        await ctx.send(hp)
    if service == "twitter":
        hp = """/twitter service quantity link

services:

Twitter Followers 3.5$ Quantity: 200 - 500000

Twitter Likes 3.5$ Quantity: 20 - 20000

Open Ticket to add Balance"""
        await ctx.send(hp)
    if service == "":
        hp = """/help instagram
/help tiktok
/help youtube
/help twitter
/help twitch
/help telegram"""
        await ctx.send(hp)











@bot.command()
async def balance(ctx):
    id=ctx.author.id
    print(id)
    txt=str(id)+'.txt'
    f = os.path.isfile(txt)
    if f == True:
        file1 = open( str(txt),"r")
        bal = file1.readline()
        file1.close()
        print(bal)
        if float(bal) > 0.0001:
            bals="Your balance is: "+str(bal)
            await ctx.send(bals)
    if f == False:
        await ctx.send("Your balance is 0 Open ticket to add balance")


@bot.command()
async def bal(ctx):
    id=ctx.author.id
    print(id)
    txt=str(id)+'.txt'
    f = os.path.isfile(txt)
    if f == True:
        file1 = open( str(txt),"r")
        bal = file1.readline()
        file1.close()
        print(bal)
        if float(bal) > 0.0001:
            bals="Your balance is: "+str(bal)
            await ctx.send(bals)
    if f == False:
        s = '''Your balance is: 0
Open ticket to add balance'''
        await ctx.send(s)




@bot.command()
async def ad(ctx):
    ad = '''https://discord.gg/gxRAATEwSx

Cheap Social media boosting.
Just add balance and use command to get followers
Your own boosting panel in discord server.

INSTAGRAM
- 1K INSTAGRAM FOLLOWERS --> $3.00
- 1K INSTAGRAM LIKES --> $1.50
TIKTOK
- 1K TIKTOK FOLLOWERS --> $6.00
- 1K TIKTOK LIKES --> $2.50
- 1K TIKTOK VIEWS --> $0.10
YOUTUBE
- 1K YOUTUBE SUBSCRIBERS --> $10.00
- 1K YOUTUBE LIKES --> $3.00
- 1K YOUTUBE VIEWS --> $2.50
OTHER
- 1K TWITTER FOLLOWERS --> $3.50
- 1K TWITTER LIKES --> $3.50
- 1K TWITCH FOLLOWERS --> $2.50
- 1K TELEGRAM MEMBERS --> $2.50'''
    await ctx.send(ad)

















bot.run("MTA3NTUxMzM2MTk0MjQ2NjYyNg.GyqT0u.gwBLtsO8AGxaFXL0ekQSoeee88vQ8zmd-qVjrA")
