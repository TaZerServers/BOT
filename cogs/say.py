import discord
from discord.ext import commands
from .utils import checks

class Mycog:
    """Says something"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def say(self, *, say):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say(say)

    @commands.command()
    @checks.is_owner()
    async def announce(self, *, say):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say(133080797660971008, "Hello")

def setup(bot):
    bot.add_cog(Mycog(bot))
