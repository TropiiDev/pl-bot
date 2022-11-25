import discord, guildid
from discord import app_commands
from discord.ext import commands

class setnick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Setnick Online")

    @commands.hybrid_command(name="setnick", description="Sets a users nickname", aliases=['nick'])
    @commands.has_permissions(manage_nicknames=True)
    @app_commands.guilds(guildid.guilds)
    async def setnick(self, ctx, user: discord.Member = None, *, nick: str):
        if user == None:
            user = ctx.author
        await user.edit(nick=nick)
        await ctx.send(f"Set {user.mention}'s nickname to {nick}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(setnick(bot))