import discord
from discord.ext import commands
from discord.utils import get

class Cmd(commands.Cog):
    def __init__(self, client):
        self.client = client
#events
#    @commands.Cog.listener()
#    async def on_ready(self):
#        print(f"{self.client.user} is online")
#    @commands.Cog.listener()
#    async def on_member_join(member):
#        role = get(member.guild.roles, name="Spuds")
#        await member.add_roles(role)

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
        embed.add_field(name=".help",value="Posts this message.",inline=False)
        embed.add_field(name="Mod Commands\n\n.clear",value="Clears 1 message if no number specified",inline=False)
        embed.add_field(name=".kick",value="Kicks a specific member from the server",inline=False)
        embed.add_field(name=".ban",value="Bans a specific member from the server",inline=False)
        embed.add_field(name=".unban",value="Unbans a specific banned member",inline=False)
#        embed.add_field(name="Commands\n___",value=".ping\n"
#        ".help\n"
#        ".clear\n"
#        ".kick\n"
#        ".ban\n"
#        ".unban\n",inline=True)
#        embed.add_field(name="Description\n___",value="Returns Pong! with latency\n"
#        "Posts this message\n"
#        "Clears 1 message if no number specified\n"
#        "Kicks a specific member from the server\n"
#        "Bans a specific member from the server\n"
#        "Unbans a specific banned member\n",inline=True)

        await ctx.send(embed=embed)
#    @commands.command()
#    async def kappa(self, ctx):
#        await ctx.send("<:thisguy:636022855993131009>")
    @commands.command()
    async def ss(self, ctx):
        try:
            channel_id = ctx.message.author.voice.channel.id
            server_id = ctx.guild.id
            await ctx.message.delete()
            await ctx.send(f"http://www.discordapp.com/channels/{server_id}/{channel_id}", delete_after=60)
        except Exception:
            await ctx.message.delete()
            await ctx.send("```You need to be in a voice channel.```", delete_after=10)

def setup(client):
    client.add_cog(Cmd(client))