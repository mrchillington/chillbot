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

    @commands.command()
    async def help(self, ctx, arg=None):
        if arg is None:
            embed = discord.Embed(
                title = "User Commands:",
                colour = discord.Colour.orange()
            )
            embed.add_field(name="..ping", value="Returns Pong! with latency.",inline=False)
            embed.add_field(name="..ss", value="Posts a link to ScreenShare in a channel.",inline=False)
            embed.add_field(name="..obs", value="Posts OBS settings",inline=False)
            embed.add_field(name="..help", value="Posts this message.",inline=False)
            embed.add_field(name="..dl", value="Gives you the list of options available",inline=False)
            embed.add_field(name="..booty", value="Posts the high quality booty gif",inline=False)
            embed.add_field(name="..stream", value="Posts the list of variables to use",inline=False)
            embed.add_field(name="..help mod", value="Give you the list of commands for mods",inline=False)
            await ctx.send(embed=embed)

        elif arg == "mod":
            embed = discord.Embed(
                title = "Mod Commands:",
                colour = discord.Colour.orange()
            )
            embed.add_field(name="..clear", value="Clears 1 message if no number specified",inline=False)
            embed.add_field(name="..kick w/optional reason", value="Kicks a specific member from the server",inline=False)
            embed.add_field(name="..ban w/optional reason", value="Bans a specific member from the server",inline=False)
            embed.add_field(name="..unban w/optional reason", value="Unbans a specific banned member",inline=False)
            embed.add_field(name="..live gamename", value="Posts live message",inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def ss(self, ctx):
        try:
            channel_id = ctx.message.author.voice.channel.id
            server_id = ctx.guild.id
            await ctx.message.delete()
            await ctx.send(f"http://www.discordapp.com/channels/{server_id}/{channel_id}")
        except Exception:
            await ctx.message.delete()
            await ctx.send("`"+"`"+"`You need to be in a voice channel.`"+"`"+"`", delete_after=10)

    @commands.command()
    async def dl(self, ctx, arg=None):
        if arg is None:
            embed = discord.Embed(colour=discord.Colour.dark_gold())
            embed.add_field(name="**__Available options__**:\n"
            "**..dl** - *Brings up this menu.*\n"
            "**..dl obs** - *Takes you to the official OBS site.*\n"
            "**..dl slobs** - *Takes you to the download page for Streamlabs OBS.*\n"
            "**..dl ts** - *Takes to the homepage of Twitch Studio Beta.*", value=f"example: .dl <option>")
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

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name="This is a test", value="This is a test")
        embed.add_field(name="*This is a test*", value="*This is a test*")
        embed.add_field(name="**This is a test**", value="**This is a test**")
        embed.add_field(name="__This is a test__", value="__This is a test__")
        embed.set_footer(text="This is a test")
        await ctx.send(embed=embed)

    @commands.command()
    async def booty(self, ctx):
        await ctx.send("https://tenor.com/view/h%c3%a2m-frog-toad-frog-l%e1%ba%afc-wiggle-gif-14557565")

    @commands.command()
    @commands.has_role("Mods")
    async def live(self, ctx, *arg):
        try:
            game = " ".join(arg)
            embed = discord.Embed(
                title = "https://www.twitch.tv/mr_chillington",
                colour = discord.Colour.dark_purple()
            )
            embed.set_author(name="Chillington is currently live on")
            embed.set_thumbnail(url="https://i.imgur.com/NAjJG3E.png")
            embed.add_field(name="Game being played", value=game.title(), inline=True)
            await ctx.send(embed=embed)
        except Exception:
            embed = discord.Embed(
                title = "https://www.twitch.tv/mr_chillington",
                colour = discord.Colour.dark_purple()
            )
            embed.set_author(name="Chillington is currently live on")
            embed.set_thumbnail(url="https://i.imgur.com/NAjJG3E.png")
            embed.add_field(name="Game being played", value="Probably playing Dead By Daylight", inline=True)
            await ctx.send(embed=embed)

    @commands.command()
    async def stream(self, ctx, arg=None):
        if arg is None:
            embed = discord.Embed(title="Here is a list of Variables.", colour=discord.Colour.dark_red())
            embed.add_field(name="Example ..stream bitrate", value="**bitrate** : Shows you how to find the bitrate."
            "\n**bpp** : Shows you how to find BPP(Bits Per Pixel)."
            "\n**masterclass** : Posts a link to EposVox's OBS Masterclass (can also be applies to SLOBS).")
            await ctx.send(embed=embed)
        elif arg == "bitrate":
            embed = discord.Embed(title="Figuring out your bitrate.", colour=discord.Colour.dark_red())
            embed.add_field(name="Bitrate Calculation", value="Stream res: Width x Height x FPS x BPP / 1000\n"
            "\nRemember that your audio bitrate gets added on top of your bitrate so if you want a bit more "
            "accurate number you would **subtract** your **audio bitrate** from the **bitrate**."
            "\n\n__Another note:__ **6000kbps** is the recommended max bitrate however you can go up to **8000kbps** without "
            "getting yelled at (remember that if you don't have quality options enabled on your channel you may have "
            "mobile users that can not watch your stream.)"
            "\n\n__Example of what you should do:__ 720p 60fps @ 6000kbps or 8000kbps / 900p 60fps @ 8000kbps but 720p 60fps will have a "
            "better image at the same bitrate."
            "\n\n__Example of what you **shouldn't** do:__ 720p 60fps @ anything under 6000kbps, 900p 60fps @ under 8000kbps or 1080p 60fps @ you guessed it 6000kbps."
            "\n1080p 60fps @ 8000kbps looks better then @ 6000kbps but just don't do it.")
            await ctx.send(embed=embed)
        elif arg == "bpp":
            embed = discord.Embed(title="Figuring out your BPP(Bits Per Pixel).", colour=discord.Colour.dark_red())
            embed.add_field(name="BPP Calculation", value="(Your upload speed x 1000)/(Width x Height x FPS)\n"
            "\nIf you want just a general BPP for high motion then use **0.1** or **0.06** for low motion like a CCG.")
            await ctx.send(embed=embed)
        elif arg == "masterclass":
            await ctx.send("https://www.youtube.com/watch?v=nK-Mu7nw5EA&list=PLzo7l8HTJNK-IKzM_zDicTd2u20Ab2pAl")

def setup(client):
    client.add_cog(Cmd(client))
