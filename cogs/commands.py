import discord

from discord.ext import commands


class Cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

#commands
#mod commands
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(colour=discord.Colour.greyple())
        embed.add_field(name="**Pong!**", value=f"Server latency: {round(self.client.latency * 1000)}ms")
        await ctx.send(embed=embed)
#        await ctx.send(f"Pong! Server latency = **{round(self.client.latency * 1000)}ms**")

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name="Help")
        embed.add_field(name="Commands\n\n.ping",value="Returns Pong! with latency.",inline=False)
        embed.add_field(name=".ss",value="Posts a link to ScreenShare in a channel.",inline=False)
        embed.add_field(name=".obs",value="Posts OBS settings",inline=False)
        embed.add_field(name=".help",value="Posts this message.",inline=False)
        
        embed.add_field(name="Mod Commands\n\n.clear",value="Clears 1 message if no number specified",inline=False)
        embed.add_field(name=".kick",value="Kicks a specific member from the server",inline=False)
        embed.add_field(name=".ban",value="Bans a specific member from the server",inline=False)
        embed.add_field(name=".unban",value="Unbans a specific banned member",inline=False)
        embed.add_field(name=".unban",value="Unbans a specific banned member",inline=False)
        embed.add_field(name=".live gamename",value="Posts live message",inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def ss(self, ctx):
        try:
            channel_id = ctx.message.author.voice.channel.id
            server_id = ctx.guild.id
            await ctx.message.delete()
            await ctx.send(f"http://www.discordapp.com/channels/{server_id}/{channel_id}", delete_after=300)
        except Exception:
            await ctx.message.delete()
            await ctx.send("`"+"`"+"`You need to be in a voice channel.`"+"`"+"`", delete_after=10)

    @commands.command()
    @commands.has_role("Mods")
    async def live(self, ctx, *arg):
        game = " ".join(arg)
        embed = discord.Embed(
            title = "https://www.twitch.tv/mr_chillington",
            colour = discord.Colour.dark_purple()
        )
        embed.set_author(name="Chillington is currently live on")
        embed.set_thumbnail(url="https://i.imgur.com/NAjJG3E.png")
        embed.add_field(name="Game being played", value=game, inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def stuff(self, ctx, arg):
        if arg == "obs":
#            await ctx.message.delete()
            embed = discord.Embed()
            embed.add_field(name="OBS IS BETTER!", value=None)
            await ctx.send(embed=embed)
        elif arg == "slobs":
#            await ctx.message.delete()
            embed = discord.Embed()
            embed.add_field(name="SLOBS IS BETTER!", value=None)
            await ctx.send(embed=embed)
#    @commands.command()
#    async def stuff(self, ctx, arg):
#        if arg == "obs":
#            await ctx.message.delete()
#            print("OBS IS BETTER!")
#        elif arg == "slobs":
#            await ctx.message.delete()
#            print("SLOBS IS BETTER!")

    @commands.command()
    async def obs(self, ctx):
        embed = discord.Embed(colour=discord.Colour.purple())
        embed.set_author(name="~OBS Settings~")
        embed.add_field(name="Encoder:", value=8000, inline=False)
        embed.add_field(name="Rate Control:", value="CBR", inline=False)
        embed.add_field(name="Keyframe:", value=2, inline=False)
        embed.add_field(name="CPU Preset:", value="faster", inline=False)
        embed.add_field(name="x264 Options:", value="threads=18 rc-lookahead=60 trellis=1 aq-mode=1 direct-pred=spatial", inline=False)
        embed.add_field(name="Resolution:", value="1280x720", inline=False)
        embed.add_field(name="Downscale:", value="Bilinear", inline=False)
        embed.add_field(name="FPS:", value="60", inline=False)
        embed.add_field(name="Dynamic bitrate:", value=":white_check_mark: ", inline=False)
        embed.add_field(name="New networking code:", value=":white_check_mark: ", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Cmd(client))