import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import get

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)
status = cycle([
    "Me eating cookies",
    "Watching paint dry",
    "Watching Chillys hosted channel",
    "I wish i was a real bot",
    "Waffles sound amazing right now...",
    "OBS Studio <3",
    "Listening to Jazz",
    "Sipping my coffee",
])
client.remove_command("help")
#something = open("F:\\Documents\\Chillbotpy\\cogs\\commands.py")

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.online)
    print(f"{client.user} is online")
    async for guild in client.fetch_guilds(limit=150):
        print(f"Logged into " + guild.name)

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name="Spuds")
    role2 = get(member.guild.roles, name="Streamers")
    await member.add_roles(role,role2)
#    await member.add_roles(role2)

@tasks.loop(minutes=3)
async def change_status():
    await client.change_presence(
        activity=discord.Streaming(
            name=next(status), url="https://www.twitch.tv/mr_chillington"))

@client.command()
async def l(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    print(f"{extension} loaded")

@client.command()
async def u(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"{extension} unloaded")

@client.command()
async def r(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    print(f"{extension} reloaded")

for fielname in os.listdir("./cogs"):
    if fielname.endswith(".py"):
        client.load_extension(f"cogs.{fielname[:-3]}")

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "."
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def commandspy(ctx):
    with open("./cogs/commands.py","r") as f:
      await ctx.send(f"```py\n{f.read()}\n```")

@client.command()
async def modpy(ctx):
    with open("./cogs/mod.py","r") as f:
      await ctx.send(f"```py\n{f.read()}\n```")
#this one took me a sec
token = open("token.txt","r").read()
client.run(token)