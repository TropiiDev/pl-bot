import discord, guildid
from discord import app_commands
from discord.ext import commands

class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mute Online")

    @commands.hybrid_command(name="mute", description="Mute a user")
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member:discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)

        em = discord.Embed(title="Muted", description=f"{member.mention} has been muted by {ctx.author.mention} for {reason}", color = ctx.author.color)
        memberem = discord.Embed(title="Muted", description=f"You have been muted in {guild.name} by {ctx.author.mention} for {reason}")
        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(embed=em)
        await member.send(embed=memberem)

    @commands.hybrid_command(name="unmute", description="Unmute a user")
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx,member:discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        em = discord.Embed(title="Unmuted", description=f"{member.mention} was unmuted by {ctx.author.mention} for {reason}")
        memberem = discord.Embed(title="Unmuted", description=f"You were unmuted in {guild.name} for {reason}")

        await member.remove_roles(mutedRole, reason=reason)
        await ctx.send(embed=em)
        await member.send(embed=memberem)

async def setup(bot):
    await bot.add_cog(mute(bot))