import discord, guildid
from discord import app_commands
from discord.ext import commands

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear Online")

    @commands.hybrid_command(name="clear", description="Bulk deletes messages")
    @commands.has_permissions(manage_messages=True)
    @app_commands.guilds(guildid.guilds)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {amount} messages", ephemeral=True, delete_after=2)

async def setup(bot):
    await bot.add_cog(clear(bot))