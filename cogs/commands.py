import discord
from discord.ext import commands

class Cmd(commands.Cog):
    def __init__(self, client):
        self.client = client
#events
#    @commands.Cog.listener()
#    async def on_ready(self):
#        print(f"{self.client.user} is online")

#commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! Server latency = **{round(self.client.latency * 1000)}ms**")

#    @commands.command()
#    async def kappa(self, ctx):
#        await ctx.send("<:thisguy:636022855993131009>")

def setup(client):
    client.add_cog(Cmd(client))