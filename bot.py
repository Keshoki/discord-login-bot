import discord
from discord.ext import commands
from random import randint

TOKEN = ""

client = commands.Bot(command_prefix="!!")

membercodes = {}
basic_role = "users"

@client.event
async def on_ready():
    print("I'm ready!")

@client.event
async def on_member_join(member):
    login_code = str(randint(10000000,99999999))
    membercodes[member.name+"#"+member.discriminator] = str(login_code)
    await member.send("send this code to #join: "+  login_code)

@client.event
async def on_message(message):
    try:
        if membercodes[str(message.author)] == str(message.content) and str(message.channel) == "join":
            role = discord.utils.get(message.author.guild.roles, name=basic_role)
            await message.author.add_roles(role)
            del membercodes[str(message.author)]
    except:
        pass

client.run(TOKEN)
