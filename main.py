class ChatPacker():
    __version__ = 1


import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, pokepy
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands, 
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
from randomuser import RandomUser
from pythonping import ping as pyping


ctypes.windll.kernel32.SetConsoleTitleW(f'[Ioxide Chat Packer v{ChatPacker.__version__}] | Starting up..')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('pass')
prefix = config.get('prefix')
packer_bot = config.get('chat_packer')
anti_afk = config.get('anti_afk')


width = os.get_terminal_size().columns

def startprint():
    if packer_bot == True:
        packer = "Enabled"
    else:
        packer = "Disabled"

    if anti_afk == True:
        antiafk = "Enabled"
    else:
        antiafk = "Disabled"

    print(f'''{Fore.RESET}
                    {Fore.RED} ██▓ ▒█████  ▒██   ██▒ ██▓▓█████▄ ▓█████ 
                    {Fore.RED}▓██▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ██▌▓█   ▀ 
                    {Fore.RED}▒██▒▒██░  ██▒░░  █   ░▒██▒░██   █▌▒███   
                    {Fore.RED}░██░▒██   ██░ ░ █ █ ▒ ░██░░▓█▄   ▌▒▓█  ▄ 
                    {Fore.RED}░██░░ ████▓▒░▒██▒ ▒██▒░██░░▒████▓ ░▒████▒
                    {Fore.RED}░▓  ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓   ▒▒▓  ▒ ░░ ▒░ ░
                    {Fore.RED} ▒ ░  ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░
                    {Fore.RED} ▒ ░░ ░ ░ ▒   ░    ░   ▒ ░ ░ ░  ░    ░   
                    {Fore.RED} ░      ░ ░   ░    ░   ░     ░       ░  ░
                    {Fore.RED}                           ░             
                                    
                        {Fore.RED}Logged In As ==> {Fore.WHITE}{Ioxide.user.name}#{Ioxide.user.discriminator}{Fore.WHITE}
                        {Fore.RED}ID ==> {Fore.WHITE}{Ioxide.user.id}
                        {Fore.RED}Packer ==> {Fore.WHITE}{packer}
                        {Fore.RED}Anti-AFK ==> {Fore.WHITE}{antiafk}
                        {Fore.RED}Prefix ==> {Fore.WHITE}{prefix}
                        {Fore.RED}Version ==> {Fore.WHITE} v{ChatPacker.__version__}

                    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.WHITE}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Ioxide.run(token, bot=False, reconnect=True)
            os.system(f'title [ Ioxide Packing Tool ] - Version {ChatPacker.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.WHITE}[ERROR] {Fore.YELLOW}Sure this is a token? lol"+Fore.RESET)
            os.system('pause >NUL')

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

colorama.init()
Ioxide = discord.Client()
Ioxide = commands.Bot(
    description='Ioxide Packing Tool',
    command_prefix=prefix,
    self_bot=True
)
Ioxide.remove_command('help') 

@Ioxide.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Ioxide.event
async def on_message_edit(before, after):
    await Ioxide.process_commands(after)

@Ioxide.event
async def on_message(message):
    responses = ["what nigga", "shut up and focus son", "nigga im right here lmfao", "sybau and focus on gettin blazed","I got 2 dicks in my ass and u still cant pack me. fuck up nigga"]
    nums = [1, 1.3, 1.5, 2, 2.3, 2.6, 3, 3.8, 5, 4, 6, 7]
    ptime = random.choice(nums)
    ## Begin Long Annoying Anti-AFK Checking..
    if 'afk c' in message.content:
        if anti_afk == True:
                try:
                    randomResponses = random.choice(responses)
                    msg = randomResponses
                    time.sleep(ptime)
                    await message.channel.send(msg)
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)
    else:
        if 'AFK C' in message.content:
            if anti_afk == True:
                try:
                    randomResponses = random.choice(responses)
                    time.sleep(ptime)
                    msg = randomResponses
                    await message.channel.send(msg)
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)
    else:
                return
    await Ioxide.process_commands(message)

@Ioxide.event
async def on_connect():
    Clear()

    if packer_bot == True:
        packer = "Enabled"
    else:
        packer = "Disabled"

    if anti_afk == True:
        antiafk = "Enabled"
    else:
        antiafk = "Disabled"

    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Ioxide Packing Tool v{ChatPacker.__version__}] | Logged in as {Ioxide.user.name}')

@Ioxide.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send(' ```Starting Chat Clear...``` ')
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')
    await ctx.send(' ```Successfully Cleared Chat``` ')

@Ioxide.command()
async def help(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_Ioxide Help_",color= discord.Color(0x000000))
    em.add_field(name="_*Packing*_",value="Display Packing Utilities",inline=False)
    em.add_field(name="_*AFK*_",value="Display AFK Utilities",inline=False)
    em.add_field(name="_*AntiNeg*_",value="Display Anti-Negative Rep. Utilities",inline=False)
    em.add_field(name="_*Wizzing*_",value="Display Wizzing Utilities",inline=False)
    em.add_field(name="_*Trolling*_",value="Display Trolling Utilities",inline=False)
    em.set_image(url="https://media.giphy.com/media/uFcRawfvGxsJO/giphy.gif")
    em.set_footer(text="klioxide was here lol")
    await ctx.send(embed=em)

@Ioxide.command()
async def packing(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_Packing Help_",color= discord.Color(0x000000))
    em.add_field(name="_*Joke*_",value="Sends a random joke",inline=False)
    em.set_image(url="https://media.giphy.com/media/4Vqyoyw5uezzG/giphy.gif")
    em.set_footer(text="made by klioxide")
    await ctx.send(embed=em)

@Ioxide.command()
async def afk(ctx):
    await ctx.message.delete()
    em = dsicord.Embed(title="_AFK Help_",color= dsicord.Color(0x000000))
    em.add_field(name="_*AfkCheck*_",value="Starts an afk check",inline=False)
    em.set_image(url="https://media.giphy.com/media/SMVmV1TcnSUj6/giphy.gif")
    em.set_footer(text="dont fold lmfao")
    await ctx.send(embed=em)

@Ioxide.command()
async def antineg(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_Anti-Negative Help_",color= discord.Color(0x000000))
    em.add_field(name="_*ioxideK*_",value="Sends secret message ;)",inline=False)
    em.set_image(url="https://media.giphy.com/media/mKAc6ZZqeE4Ao/giphy.gif")
    await ctx.send(embed=em)

@Ioxide.command(aliases=['sayajoke','jokepack'])
async def joke(ctx):
    ## idfk how to do tables for the jokes or this would be cleaner
    jokes = ["Nigga you overdosed from adrenaline rushes nigga fuck is you sayin","Aye nigga the first time you rode a skateboard you started twisting yo spine back and forth thinking you was accelerating nigga you dumb as shit","That wasn't funny nigga that's why yo long lost pet jaguar was found in west virginia eating rat soup in a pawn shop nigga you ugly as shit","That's why all yo subscribers unsubbed from yo youtube channel the first time you did a face-cam because you was ugly as shit","you smell like shit boy you shower with orange juice smelly ass nigga","you have sex with indian cockaroaches goofy ass nigga","your tities built like doritos nasty ass nigga Mmmm doritos nacho titty ass nigga","When you sneeze you got no recoil boy you be sendin yo spit everywhere"]
    await ctx.message.delete()
    randomJoke = random.choice(jokes)
    msg = randomJoke
    await ctx.send(msg)

@Ioxide.command(aliases=['IoxideK','ioxidek','Ioxidek'])
async def IoxideK(ctx):
    await ctx.message.delete()
    msg = "i command u to fold to me https://cropper.watch.aetnd.com/public-content-aetn.video.aetnd.com/video-thumbnails/AETN-History_VMS/880/442/BRAND_H2_ACTA_111852_TVE_2398_060_20131025_V1_HD.jpg i command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to me"
    await ctx.send(msg)

@Ioxide.command(aliases=['check','afkc','checkafk'])
async def afkcheck(ctx):
    await ctx.message.delete()
    ## Start Check
    await ctx.send('afk check')
    time.sleep(0.8)
    await ctx.send('10')
    time.sleep(0.8)
    await ctx.send('9')
    time.sleep(0.8)
    await ctx.send('8')
    time.sleep(0.8)
    await ctx.send('7')
    time.sleep(0.8)
    await ctx.send('6')
    time.sleep(0.8)
    await ctx.send('5')
    time.sleep(0.8)
    await ctx.send('4')
    time.sleep(0.8)
    await ctx.send('3')
    time.sleep(0.8)
    await ctx.send('2')
    time.sleep(0.8)
    await ctx.send('1')
    time.sleep(0.8)
    await ctx.send('0')

if __name__ == '__main__':
    Init()

