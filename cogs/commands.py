import discord

from discord.ext import commands

class Cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

#commands
#spiced up version of the simple ping command
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(colour=discord.Colour.greyple())
        embed.add_field(name="**Pong!**", value=f"Server latency: {round(self.client.latency * 1000)}ms")
        await ctx.send(embed=embed)

#nicer looking help command
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
        embed.add_field(name=".live gamename",value="Posts live message",inline=False)
        embed.add_field(name=".dl", value="Gives you the list of options avalible ")

        embed.add_field(name="Mod Commands\n\n.clear",value="Clears 1 message if no number specified",inline=False)
        embed.add_field(name=".kick",value="Kicks a specific member from the server",inline=False)
        embed.add_field(name=".ban",value="Bans a specific member from the server",inline=False)
        embed.add_field(name=".unban",value="Unbans a specific banned member",inline=False)
        embed.add_field(name=".unban",value="Unbans a specific banned member",inline=False)
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
    async def dl(self, ctx, arg=None):
        if arg is None:
            embed = discord.Embed(colour=discord.Colour.dark_gold())
            embed.add_field(name="**__Available options__**:\n"
            "**.dl** - *Brings up this menu.*\n"
            "**.dl obs** - *Takes you to the offical OBS site.*\n"
            "**.dl slobs** - *Takes you to the download page for Streamlabs OBS.*\n"
            "**.dl ts** - *Takes to the homepage of Twitch Studio Beta.*", value=f"example: .dl <option>")
            await ctx.send(embed=embed)
        elif arg == "obs":
            embed = discord.Embed(title="Click here", url="https://obsproject.com/", description="To download OBS Studio", colour=discord.Colour.darker_grey())
            await ctx.send(embed=embed)
        elif arg == "slobs":
            embed = discord.Embed(title="Click here", url="https://streamlabs.com/slobs/download", description="To download Streamlabs OBS", colour=discord.Colour.dark_teal())
            await ctx.send(embed=embed)
        elif arg == "ts":
            embed = discord.Embed(title="Click here", url="https://www.twitch.tv/broadcast/studio", description="To download Twitch Studio Beta", colour=discord.Colour.purple())
            await ctx.send(embed=embed)

    @commands.command()
    async def sl(self, ctx, arg=None):
        if arg is None:
            await ctx.send("something")
        elif arg == "obs":
            await ctx.send("Nothing")

    @commands.command()
    async def obs(self, ctx):
        embed = discord.Embed(colour=discord.Colour.purple())
        embed.set_author(name="~OBS Settings~")
        embed.add_field(name="Encoder:", value=8000, inline=True)
        embed.add_field(name="Rate Control:", value="CBR", inline=True)
        embed.add_field(name="Keyframe:", value=2, inline=True)
        embed.add_field(name="CPU Preset:", value="faster", inline=True)
        embed.add_field(name="x264 Options:", value="threads=18 rc-lookahead=60 trellis=1 aq-mode=1 direct-pred=spatial", inline=True)
        embed.add_field(name="Resolution:", value="1280x720", inline=True)
        embed.add_field(name="Downscale:", value="Bilinear", inline=True)
        embed.add_field(name="FPS:", value="60", inline=True)
        embed.add_field(name="Dynamic bitrate:", value=":white_check_mark: ", inline=True)
        embed.add_field(name="New networking code:", value=":white_check_mark: ", inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Cmd(client))