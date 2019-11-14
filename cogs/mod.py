import discord
from traceback import format_exc
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import Bot, BadArgument, CommandNotFound, MissingRequiredArgument
from discord.ext import commands
from discord.utils import get

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client
#commands
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
            embed = discord.Embed(colour=discord.Colour.dark_red())
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)
            embed.add_field(name=f"{amount} messages were deleted", value=f"*By {ctx.message.author}*")
            await ctx.send(embed=embed, delete_after=10)
            await self.client.get_channel(644218055177797644).send(embed=embed)
            print(f"{amount} messages were deleted | By {ctx.message.author}")

    @commands.command()
    @commands.has_role("Mods")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete(delay=10)
        await member.kick(reason=reason)
        cat = ctx.message.author #i have no idea what im doing anymore
#        await self.client.get_channel(644218055177797644).send(f"{member} has been kicked")
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.add_field(name="**__User kicked:__**", value=f"{member}", inline=False)
        embed.add_field(name="**__Kicked by:__**", value=f"{cat}", inline=True)
        embed.add_field(name="**__Reason:__**", value=f"{reason}", inline=True)

#        channel = self.client.get_channel(644218055177797644)
        await self.client.get_channel(644218055177797644).send(embed=embed)

    @commands.command()
    @commands.has_role("Mods")
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_role("Mods")
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

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

def setup(client):
    client.add_cog(Mod(client))