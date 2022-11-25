import discord, guildid, urllib, json
from discord import app_commands
from discord.ext import commands

class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Meme Online")

    @commands.hybrid_command(name="meme", description="Shows a random meme")
    @app_commands.guilds(guildid.guilds)
    async def meme(self, ctx):
        memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

        memeData = json.load(memeApi)

        memeUrl = memeData['url']
        memeName = memeData['title']
        memePoster = memeData['author']

        em = discord.Embed(title=memeName)
        em.set_image(url=memeUrl)
        em.set_footer(text=f"Meme by: {memePoster}")   
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(meme(bot))