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
            pfp = ctx.message.author.avatar_url
            if amount == 1:
                embed = discord.Embed(colour=discord.Colour.dark_red())
                await ctx.message.delete()
                await ctx.channel.purge(limit=amount)
                embed.set_author(name=f"{ctx.message.author}", icon_url=pfp)
                embed.add_field(name="Cleared:", value=f"**{amount}** Message", inline=False)
                #embed.add_field(name="Command inacted by:", value=f"{ctx.message.author.mention}", inline=False)
                await ctx.send(embed=embed, delete_after=1)
                await self.client.get_channel(502331932869263362).send(embed=embed)
                print(f"{amount} message was deleted | By {ctx.message.author}")
            elif amount > 1:
                embed = discord.Embed(colour=discord.Colour.dark_red())
                await ctx.message.delete()
                await ctx.channel.purge(limit=amount)
                embed.set_author(name=f"{ctx.message.author}", icon_url=pfp)
                embed.add_field(name="Cleared:", value=f"**{amount}** Messages", inline=False)
                #embed.add_field(name="Command inacted by:", value=f"{ctx.message.author.mention}", inline=False)
                await ctx.send(embed=embed, delete_after=1)
                await self.client.get_channel(502331932869263362).send(embed=embed)
                print(f"{amount} messages was deleted | By {ctx.message.author}")

    @commands.command()
    @commands.has_role("Mods")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete(delay=10)
        await member.kick(reason=reason)
        cat = ctx.message.author #i have no idea what im doing anymore
        pfp = ctx.message.author.avatar_url
        #await self.client.get_channel(644218055177797644).send(f"{member} has been kicked")
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name=cat, icon_url=pfp)
        embed.add_field(name="**__Kicked:__**", value=f"{member.mention}")
        #embed.add_field(name="**__User kicked:__**", value=f"{member}", inline=False)
        #embed.add_field(name="**__Kicked by:__**", value=f"{cat}", inline=True)
        embed.add_field(name="**__Reason:__**", value=f"{reason}", inline=True)
        #channel = self.client.get_channel(644218055177797644)
        await self.client.get_channel(502331932869263362).send(embed=embed)
        print(f"{cat} has Kicked {member} for reason: {reason}")

    @commands.command()
    @commands.has_role("Mods")
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete(delay=10)
        await member.ban(reason=reason)
        cat = ctx.message.author #i have no idea what im doing anymore
        pfp = ctx.message.author.avatar_url
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name=cat, icon_url=pfp)
        embed.add_field(name="**__Banned:__**", value=f"{member.mention}")
        #embed.add_field(name="**__Banned by:__**", value=f"{cat}", inline=True)
        embed.add_field(name="**__Reason:__**", value=f"**{reason}**", inline=True)
        await self.client.get_channel(502331932869263362).send(embed=embed)
        print(f"{cat} has Banned {member} for reason: {reason}")

    @commands.command()
    @commands.has_role("Mods")
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return
#                cat = ctx.message.author #i have no idea what im doing anymore
#                pfp = ctx.message.author.avatar_url
#                embed = discord.Embed(colour=discord.Colour.orange())
#                embed.set_author(name=cat, icon_url=pfp)
#                embed.add_field(name="**__Unbanned:__**", value=f"{user.mention}")
#                #embed.add_field(name="**__Unbanned by:__**", value=f"{cat}", inline=True)
#                embed.add_field(name="**__Reason:__**", value=f"{reason}", inline=True)
#                await self.client.get_channel(502331932869263362).send(f"{user.mention} has been unbanned")
#                print(f"{cat} has Unbanned {user} for reason: {reason}")
#                await ctx.send(f"Unbanned {user.mention}")

def setup(client):
    client.add_cog(Mod(client))
