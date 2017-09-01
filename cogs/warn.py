import discord
from discord.ext import commands
import os # This is required because you will be creating folders/files
from .utils.dataIO import dataIO  # This is pulled from Twentysix26's utils
from .utils import checks

class Warn:
    """ A warn Cog made by "HaZe_Pug" """

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @checks.serverowner_or_permissions(ban_members=True)
    async def warn(self, ctx, user : discord.Member, *, reason):
        author = ctx.message.author
        """Warn a user and tell them off"""

        #Your code will go here
        embed=discord.Embed(title=":no_entry: Warn :no_entry:", description="You have been warned do not do it again or next time you might get punished", color=0xed0000)
        embed.add_field(name="User:", value=""  + user.mention + "", inline=False)
        embed.add_field(name="Moderator:", value="" + author.mention + "", inline=True)
        embed.add_field(name="Reason:", value="" + reason + "", inline=False)
        await self.bot.say(embed=embed)
        
def setup(bot):
    bot.add_cog(Warn(bot))
