import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help, settings
from datetime import datetime
from collections import deque, defaultdict
from cogs.utils.chat_formatting import escape_mass_mentions, box, pagify
import os
import re
import logging
import asyncio

class Moderator:
    """ A warn Cog made by "HaZe_Pug" """
    
    def __init__(self, bot):
        self.bot = bot



    @commands.group(pass_context=True)
    @checks.serverowner_or_permissions(ban_members=True)
    async def mod(self, ctx):
        """Example2 group command is all about stuff"""
        
    @mod.command(name="warn", pass_context=True)
    async def _warn(self, ctx, user : discord.Member, reason):
        author = ctx.message.author
        
        embed=discord.Embed(title=":no_entry_sign: **Warn** ", description="You have been warned next time you will be punished ", color=ff0000)
        embed.add_field(name="Member:", value=user.mention, inline=True)
        embed.add_field(name="Moderator: ", value=author.mention, inline=True)
        embed.add_field(name="Reason: ", value=reason, inline=True)
        await self.bot.say(embed=embed)


    @mod.command(name="ban", pass_context=True, no_pm=False)
    async def _ban(self, ctx, user : discord.Member, reasson):
        author = ctx.message.author

        await self.bot.say("Error: \nError Code 808\nPlease contact a admin")

def setup(bot):
    bot.add_cog(Moderator(bot))
