import discord, guildid
from discord import app_commands
from discord.ext import commands

class giverole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Giverole Online")

    @commands.hybrid_command(name="giverole", description="Gives a user a role")
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(administrator=True)
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(f"Gave {user.mention} the {role.name} role", ephemeral=True)

async def setup(bot):
    await bot.add_cog(giverole(bot))