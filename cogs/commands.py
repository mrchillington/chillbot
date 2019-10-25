import discord
import urllib
from discord.ext import commands
from discord.utils import get
from urllib.request import urlopen

class Cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

#commands
#mod commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! Server latency = **{round(self.client.latency * 1000)}ms**")

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name="Help")
        embed.add_field(name="Commands\n\n.ping",value="Returns Pong! with latency.",inline=False)
        embed.add_field(name=".ss",value="Posts a link to ScreenShare in a channel.",inline=False)
        embed.add_field(name=".help",value="Posts this message.",inline=False)
        embed.add_field(name="Mod Commands\n\n.clear",value="Clears 1 message if no number specified",inline=False)
        embed.add_field(name=".kick",value="Kicks a specific member from the server",inline=False)
        embed.add_field(name=".ban",value="Bans a specific member from the server",inline=False)
        embed.add_field(name=".unban",value="Unbans a specific banned member",inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def ss(self, ctx):
        try:
            channel_id = ctx.message.author.voice.channel.id
            server_id = ctx.guild.id
            await ctx.message.delete()
            await ctx.send(f"http://www.discordapp.com/channels/{server_id}/{channel_id}", delete_after=60)
        except Exception:
            await ctx.message.delete()
            await ctx.send("`"+"`"+"`You need to be in a voice channel.`"+"`"+"`", delete_after=10)
    
#    @commands.command()
#    async def this(self, ctx, emoji: guild.Emoji("thisguy")):
#        await ctx.send(f"{emoji}")


def setup(client):
    client.add_cog(Cmd(client))