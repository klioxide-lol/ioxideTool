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
anti_neg = config.get('anti_neg')

width = os.get_terminal_size().columns

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def startprint():
    if packer_bot == True:
        packer = "Enabled"
    else:
        packer = "Disabled"

    if anti_afk == True:
        antiafk = "Enabled"
    else:
        antiafk = "Disabled"

    if anti_neg == True:
        antineg = "Enabled"
    else:
        antineg = "Disabled"

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
                        {Fore.RED}Anti-Negative ==> {Fore.WHITE}{antineg}
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
    elif 'AFK C' in message.content:
        if anti_afk == True:
            try:
                randomResponses = random.choice(responses)
                time.sleep(ptime)
                msg = randomResponses
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)

    elif 'AFK c' in message.content:
        if anti_afk == True:
            try:
                randomResponses = random.choice(responses)
                time.sleep(ptime)
                msg = randomResponses
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)
        return

    elif 'ioxideK' in message.content:
        if anti_neg == True:
            try:
                msg = "i command u to fold to me https://cropper.watch.aetnd.com/public-content-aetn.video.aetnd.com/video-thumbnails/AETN-History_VMS/880/442/BRAND_H2_ACTA_111852_TVE_2398_060_20131025_V1_HD.jpg i command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to me"
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)

    elif 'ioxidek' in message.content:
        if anti_neg == True:
            try:
                msg = "i command u to fold to me https://cropper.watch.aetnd.com/public-content-aetn.video.aetnd.com/video-thumbnails/AETN-History_VMS/880/442/BRAND_H2_ACTA_111852_TVE_2398_060_20131025_V1_HD.jpg i command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to me"
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)

    elif 'IoxideK' in message.content:
        if anti_neg == True:
            try:
                msg = "i command u to fold to me https://cropper.watch.aetnd.com/public-content-aetn.video.aetnd.com/video-thumbnails/AETN-History_VMS/880/442/BRAND_H2_ACTA_111852_TVE_2398_060_20131025_V1_HD.jpg i command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to mei command u to fold to me"
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)

    elif 'demonicK' in message.content:
        if anti_neg == True:
            try:
                msg = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1KzlBBJEmKwmG2Bm8QGmhRcpZZnJk1I44EQ&usqp=CAU  Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn. NaYoggoth ah 'fhalma shagg fm'latgh 'fhalma ch', hai sll'ha Azathoth uh'e y-shugg nach' vulgtlagln hlirgh 'fhalma 'aior vulgtlagln. Ph'Azathoth ee nilgh'ri athg Tsathoggua nilgh'ri ebunma shogg goka, lloig ehyenyth ngebunma cwgah'n r'luh wgah'n f'nglui Tsathoggua, ep shugg Yoggoth geb ooboshuoth shagg nguh'e. Gnaiih nnnzhro cshogg ph'vulgtm syha'h nog Tsathoggua shagg f'ron, mg throd y-shogg hafh'drn grah'n cnog n'ghaog Hastur ebunma, Nyarlathotep orr'e kn'a uaaah ehye zhro lloig. Ron k'yarnak hafh'drn y-ftaghu n'gha nglui cgoka fm'latgh, hupadgh llll kn'a athg y-zhro wgah'n f'k'yarnak nglui, nas'uhn mg hupadgh cshagg namnahn' h'athgPh'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn. NaYoggoth ah 'fhalma shagg fm'latgh 'fhalma ch', hai sll'ha Azathoth uh'e y-shugg nach' vulgtlagln hlirgh 'fhalma 'aior vulgtlagln. Ph'Azathoth ee nilgh'ri athg Tsathoggua nilgh'ri ebunma shogg goka, lloig ehyenyth ngebunma cwgah'n r'luh wgah'n f'nglui Tsathoggua, ep shugg Yoggoth geb ooboshuoth shagg nguh'e. Gnaiih nnnzhro cshogg ph'vulgtm syha'h nog Tsathoggua shagg f'ron, mg throd y-shogg hafh'drn grah'n cnog n'ghaog Hastur ebunma, Nyarlathotep orr'e kn'a uaaah ehye zhro lloig. Ron k'yarnak hafh'drn y-fta https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFrZiOeD3dEQuVSQc2FuG3eWN6g_Sr7NswzQ&usqp=CAU"
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)

    elif 'DemonicK' in message.content:
        if anti_neg == True:
            try:
                msg = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1KzlBBJEmKwmG2Bm8QGmhRcpZZnJk1I44EQ&usqp=CAU  Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn. NaYoggoth ah 'fhalma shagg fm'latgh 'fhalma ch', hai sll'ha Azathoth uh'e y-shugg nach' vulgtlagln hlirgh 'fhalma 'aior vulgtlagln. Ph'Azathoth ee nilgh'ri athg Tsathoggua nilgh'ri ebunma shogg goka, lloig ehyenyth ngebunma cwgah'n r'luh wgah'n f'nglui Tsathoggua, ep shugg Yoggoth geb ooboshuoth shagg nguh'e. Gnaiih nnnzhro cshogg ph'vulgtm syha'h nog Tsathoggua shagg f'ron, mg throd y-shogg hafh'drn grah'n cnog n'ghaog Hastur ebunma, Nyarlathotep orr'e kn'a uaaah ehye zhro lloig. Ron k'yarnak hafh'drn y-ftaghu n'gha nglui cgoka fm'latgh, hupadgh llll kn'a athg y-zhro wgah'n f'k'yarnak nglui, nas'uhn mg hupadgh cshagg namnahn' h'athgPh'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn. NaYoggoth ah 'fhalma shagg fm'latgh 'fhalma ch', hai sll'ha Azathoth uh'e y-shugg nach' vulgtlagln hlirgh 'fhalma 'aior vulgtlagln. Ph'Azathoth ee nilgh'ri athg Tsathoggua nilgh'ri ebunma shogg goka, lloig ehyenyth ngebunma cwgah'n r'luh wgah'n f'nglui Tsathoggua, ep shugg Yoggoth geb ooboshuoth shagg nguh'e. Gnaiih nnnzhro cshogg ph'vulgtm syha'h nog Tsathoggua shagg f'ron, mg throd y-shogg hafh'drn grah'n cnog n'ghaog Hastur ebunma, Nyarlathotep orr'e kn'a uaaah ehye zhro lloig. Ron k'yarnak hafh'drn y-fta https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFrZiOeD3dEQuVSQc2FuG3eWN6g_Sr7NswzQ&usqp=CAU"
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)

    elif 'demonick' in message.content:
        if anti_neg == True:
            try:
                msg = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1KzlBBJEmKwmG2Bm8QGmhRcpZZnJk1I44EQ&usqp=CAU  Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn. NaYoggoth ah 'fhalma shagg fm'latgh 'fhalma ch', hai sll'ha Azathoth uh'e y-shugg nach' vulgtlagln hlirgh 'fhalma 'aior vulgtlagln. Ph'Azathoth ee nilgh'ri athg Tsathoggua nilgh'ri ebunma shogg goka, lloig ehyenyth ngebunma cwgah'n r'luh wgah'n f'nglui Tsathoggua, ep shugg Yoggoth geb ooboshuoth shagg nguh'e. Gnaiih nnnzhro cshogg ph'vulgtm syha'h nog Tsathoggua shagg f'ron, mg throd y-shogg hafh'drn grah'n cnog n'ghaog Hastur ebunma, Nyarlathotep orr'e kn'a uaaah ehye zhro lloig. Ron k'yarnak hafh'drn y-ftaghu n'gha nglui cgoka fm'latgh, hupadgh llll kn'a athg y-zhro wgah'n f'k'yarnak nglui, nas'uhn mg hupadgh cshagg namnahn' h'athgPh'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn. NaYoggoth ah 'fhalma shagg fm'latgh 'fhalma ch', hai sll'ha Azathoth uh'e y-shugg nach' vulgtlagln hlirgh 'fhalma 'aior vulgtlagln. Ph'Azathoth ee nilgh'ri athg Tsathoggua nilgh'ri ebunma shogg goka, lloig ehyenyth ngebunma cwgah'n r'luh wgah'n f'nglui Tsathoggua, ep shugg Yoggoth geb ooboshuoth shagg nguh'e. Gnaiih nnnzhro cshogg ph'vulgtm syha'h nog Tsathoggua shagg f'ron, mg throd y-shogg hafh'drn grah'n cnog n'ghaog Hastur ebunma, Nyarlathotep orr'e kn'a uaaah ehye zhro lloig. Ron k'yarnak hafh'drn y-fta https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFrZiOeD3dEQuVSQc2FuG3eWN6g_Sr7NswzQ&usqp=CAU"
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)


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
    em = discord.Embed(title="_Ioxide Packing Tool_",color= discord.Color(0x000000))
    em.add_field(name="_*Packing*_",value="Display Packing Utilities",inline=False)
    em.add_field(name="_*AFK*_",value="Display AFK Utilities",inline=False)
    em.add_field(name="_*AntiNeg*_",value="Display Anti-Negative Rep. Utilities",inline=False)
    em.add_field(name="_*Wizzing*_",value="Display Wizzing Utilities",inline=False)
    em.add_field(name="_*Trolling*_",value="Display Trolling Utilities",inline=False)
    em.add_field(name="_*NSFW*_",value="Display NSFW Utilities",inline=False)
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
    em = discord.Embed(title="_AFK Help_",color= discord.Color(0x000000))
    em.add_field(name="_*AfkCheck*_",value="Starts an afk check",inline=False)
    em.set_image(url="https://media.giphy.com/media/SMVmV1TcnSUj6/giphy.gif")
    em.set_footer(text="dont fold lmfao")
    await ctx.send(embed=em)

@Ioxide.command()
async def antineg(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_*Anti-Negative Help*_",color= discord.Color(0x000000))
    em.set_image(url="https://media.giphy.com/media/mKAc6ZZqeE4Ao/giphy.gif")
    await ctx.send(embed=em)

@Ioxide.command()
async def wizzing(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_*Wizzing Help*_",color= discord.Color(0x000000))
    em.add_field(name="_**Destroy**_",value="Fucks a servers channels and roles",inline=False)
    em.set_image(url="https://media.giphy.com/media/pVwsBrZyxOlfa/giphy.gif")
    em.set_footer(text="Dont let this happen to u lol")
    await ctx.send(embed=em)

@Ioxide.command()
async def trolling(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_*Trolling Help*_",color= discord.Color(0x000000))
    em.add_field(name="_**rainbow**_",value="Makes the role you specified rainbow",inline=False)
    em.add_field(name="_**troll**_",value="Sends a random troll message xd LOL0lL0L",inline=False)
    em.set_image(url="https://media.giphy.com/media/tyttpHlrsqdQC08orGE/giphy.gif")
    em.set_footer(text="slang these nuts across yo face nigga LOL")
    await ctx.send(embed=em)

@Ioxide.command()
async def nsfw(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_*NSFW Help*_",color= discord.Color(0x000000))
    em.add_field(name="_**fuck**_",value="has monkey sex with user",inline=False)
    em.add_field(name="_**anal**_",value="does nigga anal with user",inline=False)
    em.add_field(name="_**boobs**_",value="plays with those melons",inline=False)
    em.add_field(name="_**cum**_",value="turn someone into a twinkie",inline=False)
    em.add_field(name="_**kiss**_",value="and now.. le kiss",inline=False)
    em.add_field(name="_**head**_",value="makes u get gwap gwap 12000 from a user",inline=False)
    em.set_image(url="https://media.giphy.com/media/10ToEKrp3s99Fm/giphy.gif")
    em.set_footer(text="monkey ape nigga sex")
    await ctx.send(embed=em)

@Ioxide.command(aliases=['rainbowrole'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(1)
        except:
            break

@Ioxide.command()
async def troll(ctx):
    await ctx.message.delete()
    troll1 = "nigga thats why ceed hoed u bitch ass nigga"
    troll2 = "remember when slang violated you?"
    troll3 = "bro ceeday said he bitched ur ass on rec LOL"
    troll4 = "bro why did the nigga named work bitch you? LOOOL"
    troll5 = "how did rydon flame u he dont even pack lol"

    trolls = [troll1, troll2, troll3, troll4, troll5]

    trollresponse1 = "ceed deez nuts across yo face BITCH ASS NIGGA"
    trollresponse2 = "slang deez nuts across yo face stupid ass nigga"
    trollresponse3 = "ceedayz nuts down yo throat ugly ass nigga"
    trollresponse4 = "work this dick down ur mouth FAGGOT ASS NIGGA"
    trollresponse5 = "rydon on this dick WEIRD ASS NIGGA LLLL"

    randomTroll = random.choice(trolls)

    if randomTroll == troll1:
        await ctx.send(troll1)
        time.sleep(4)
        await ctx.send(trollresponse1)
    elif randomTroll == troll2:
        await ctx.send(troll2)
        time.sleep(2)
        await ctx.send(trollresponse2)
    elif randomTroll == troll3:
        await ctx.send(troll3)
        time.sleep(4)
        await ctx.send(trollresponse3)
    elif randomTroll == troll4:
        await ctx.send(troll4)
        time.sleep(4)
        await ctx.send(trollresponse4)
    elif randomTroll == troll5:
        await ctx.send(troll5)
        time.sleep(4)
        await ctx.send(trollresponse5)
    else:
        return

@Ioxide.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "ioxideW"
        name = " "
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)

@Ioxide.command(aliases=['911'])
async def swat(ctx, user): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(description=user + ' has been swatted', colour=discord.Colour(0x000000))
    em.set_image(url="https://i.imgur.com/j1fjEwj.gif")
    await ctx.send(embed=em)

@Ioxide.command(aliases=['sayajoke','jokepack'])
async def joke(ctx):
    ## idfk how to do tables for the jokes or this would be cleaner
    jokes = ["Nigga you overdosed from adrenaline rushes nigga fuck is you sayin","Aye nigga the first time you rode a skateboard you started twisting yo spine back and forth thinking you was accelerating nigga you dumb as shit","That wasn't funny nigga that's why yo long lost pet jaguar was found in west virginia eating rat soup in a pawn shop nigga you ugly as shit","That's why all yo subscribers unsubbed from yo youtube channel the first time you did a face-cam because you was ugly as shit","you smell like shit boy you shower with orange juice smelly ass nigga","you have sex with indian cockaroaches goofy ass nigga","your tities built like doritos nasty ass nigga Mmmm doritos nacho titty ass nigga","When you sneeze you got no recoil boy you be sendin yo spit everywhere"]
    await ctx.message.delete()
    randomJoke = random.choice(jokes)
    msg = randomJoke
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

@Ioxide.command(aliases=['serverdestroy','ruinserver','doafredo'])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="get fucked by ioxide LOL",
            reason="cuz ioxideW nigga",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="ioxide nuked u lol")
    for _i in range(250):
        await ctx.guild.create_role(name="ioxideW", color=RandomColor())

## Nsfw Commands Here
@Ioxide.command()
async def fuck(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel): # makes it work in gcs (finally got it i was so retarded LOL)
        r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel): # makes it work in dms
            r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
            res = r.json()
            em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+recipients, color= discord.Color(0x000000))
            em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@Ioxide.command()
async def cum(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/cum")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**came inside**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/cum")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**came inside**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@Ioxide.command()
async def head(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/blowjob")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**got head from**_ '+ recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/blowjob")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**got head from**_ '+ recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def spank(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/spank")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**spanked**_ '+ recipients+"'s _**fat ass**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/spank")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**spanked**_ '+ recipients+"'s _**fat ass**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def boobs(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**played with**_ '+ recipients +"'s _**boobs**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**played with**_ '+ recipients +"'s _**boobs**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def pussy(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/pussy")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+ recipients +"'s _**wet pussy**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/pussy")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+ recipients +"'s _**wet pussy**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def kiss(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**kissed**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**kissed**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@Ioxide.command()
async def anal(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/anal")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**gave**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/anal")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**gave**_ '+recipients+' _**anal**_ ', color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em) 

if __name__ == '__main__':
    Init()

