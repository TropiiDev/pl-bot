import discord, guildid, datetime
from discord import app_commands
from discord.ext import commands

class timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Timeout Online")

    @commands.hybrid_command(name="timeout", description="Timeout a user")
    @app_commands.guilds(guildid.guilds)
    async def timeout(self, ctx, user: discord.Member, time: int, reason: str = None):
        await user.timeout(datetime.timedelta(minutes=time), reason=reason)
        await ctx.send(f"{user.mention} has been timed out for {reason}", ephemeral=True)

    @commands.hybrid_command(name="removetimeout", description="Remove a users timeout")
    @app_commands.guilds(guildid.guilds)
    async def removetimeout(self, ctx, user: discord.Member):
        await user.timeout(None)
        await ctx.send(f"{user.mention} has been removed from timeout", ephemeral=True)

async def setup(bot):
    await bot.add_cog(timeout(bot))