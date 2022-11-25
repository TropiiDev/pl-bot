import discord, guildid
from discord import app_commands
from discord.ext import commands

class kb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("KB Online")

    @commands.hybrid_command()
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        guild = ctx.guild
        em = discord.Embed(title="Kick", description=f"{member.mention} has been kicked for {reason}", color = ctx.author.color)
        emmember = discord.Embed(title="Kicked", description=f"You have been kicked in {guild.name} for {reason}", color = ctx.author.color)
        await ctx.send(embed=em)
        await member.send(embed=emmember)
        await member.kick(reason=reason)
        

    @commands.hybrid_command()
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        ctxem = discord.Embed(title="Ban", description=f"{member.mention} has been banned in the server for {reason}", color = ctx.author.color)
        await member.ban(reason=reason)
        await ctx.send(embed=ctxem)

async def setup(bot):
    await bot.add_cog(kb(bot))