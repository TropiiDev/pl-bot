import discord, guildid
from discord import app_commands
from discord.ext import commands

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Avatar Online")

    @commands.hybrid_command(name="avatar", description="Shows a users avatar", aliases=['av'])
    @app_commands.guilds(guildid.guilds)
    async def avatar(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        em = discord.Embed(title=f"{user.name}'s Avatar", color=user.color)
        em.set_image(url=user.avatar)
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(avatar(bot))