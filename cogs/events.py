import discord
from traceback import format_exc
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import Bot, BadArgument, CommandNotFound, MissingRequiredArgument
from discord.ext import commands
from discord.utils import get

class events(commands.Cog):
    def __init__(self, client):
        self.client = client

    class get:
        def channel(self, channelname):
            return utils.get(discord.Guild.text_channels, name=channelname)
        def role(self, rolename):
            return utils.get(discord.Guild.roles, name=rolename)

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        await utils.get.channel("audit_log").send(f"```{format_exc()[-1994:]}```")
        return

    @commands.Cog.listener()
    async def on_command_error(self,ctx,exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send(":warning: *Command not found, type* **.help** *for a list of commands to use.*")
        if isinstance(exc, MissingRequiredArgument):
            await ctx.send(":warning: *Missing required argument.*")

    @commands.Cog.listener()
    async def on_reaction_add(self, Reaction, User):
        return

    @commands.Cog.listener()
    async def on_reaction_remove(self, Reaction, User):
        return

    @commands.Cog.listener()
    async def on_message(self, message):
        return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = get(member.guild.roles, name="Spuds")
        await member.add_roles(role)
        embed = discord.Embed(colour=discord.Colour.dark_teal())
        embed.add_field(name="**__Member joined:__**", value=member, inline=True)
        embed.add_field(name="**__Role given:__**", value=role, inline=True)
        await self.client.get_channel(644218055177797644).send(embed=embed)
#        await self.client.get_channel(342892870350667777).send(embed=embed)
        print(f"{member} was given {role}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(colour=discord.Colour.magenta())
        embed.add_field(name="**__User has left us:__** :slight_frown: ", value=member)
        await self.client.get_channel(644218055177797644).send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        return

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        return


def setup(client):
    client.add_cog(events(client))