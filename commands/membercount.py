import discord, guildid
from discord import app_commands
from discord.ext import commands

class membercount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Membercount Online")
    
    @commands.hybrid_command(name="membercount", description="Shows the membercount", aliases=['mc'])
    @app_commands.guilds(guildid.guilds)
    async def membercount(self, ctx):
        em = discord.Embed(title="Member Count", description=f"Total Members: {ctx.guild.member_count}", color=ctx.author.color)
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(membercount(bot))