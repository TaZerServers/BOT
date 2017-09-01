import discord
from discord.ext import commands
import os # This is required because you will be creating folders/files
from .utils.dataIO import dataIO  # This is pulled from Twentysix26's utils
from .utils import checks

class Help:
    """ Help commands for our server """

    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=["how-to-join", "server"])
    async def ip(self):

        embed=discord.Embed(title="TaZerPrison", description="This discord is linked to a server called TaZerPrison on minehut.", color=0x5da039)
        embed.set_thumbnail(url='https//i.imgur.com/mJuHAnzg.png')
        embed.add_field(name="If you new to minehut how to join", value="Add a server with the ip minehut.com and join it. Once you joined type this command ``/join tazerprison``", inline=True)
        embed.add_field(name="If your not new to minehut", value="The server name is ``TaZerPrison``", inline=True)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
