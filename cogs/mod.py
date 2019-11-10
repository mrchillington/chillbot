import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client
#commands
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"`"+"`"+"`"+"{amount} messages were deleted"+"`"+"`"+"`", delete_after=6)

    @commands.command()
    @commands.has_role("Mods")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

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

def setup(client):
    client.add_cog(Mod(client))