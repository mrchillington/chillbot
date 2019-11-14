import discord
from traceback import format_exc
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import Bot, BadArgument, CommandNotFound, MissingRequiredArgument
from discord.ext import commands

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
            return
        if isinstance(exc, MissingRequiredArgument):
            await ctx.send(":warning: Missing required argument.")
    @commands.Cog.listener()
    async def on_reaction_add(self, Reaction, User):
        return
    @commands.Cog.listener()
    async def on_reaction_remove(self, Reaction, User):
        return
    @commands.Cog.listener()
    async def on_message(self, Message):
        if not Message.author.bot:
            await self.client.process_commands(Message)
        return

def setup(client):
    client.add_cog(events(client))