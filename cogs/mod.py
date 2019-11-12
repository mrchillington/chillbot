import discord
from discord.ext import commands

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
            embed.add_field(name=f"{amount} messages were deleted", value=f"*User of the command {ctx.message.author}*")
            await ctx.send(embed=embed, delete_after=10)
            print(f"{amount} messages were deleted | User of the command {ctx.message.author}")

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

def setup(client):
    client.add_cog(Mod(client))