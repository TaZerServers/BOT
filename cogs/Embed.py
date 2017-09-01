import discord
from discord.ext import commands
import os # This is required because you will be creating folders/files
from .utils.dataIO import dataIO  # This is pulled from Twentysix26's utils
from .utils import checks

class Embed:
    """ No Desc """

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="embed", pass_context=True)
    async def _embed(self, ctx):

            if ctx.invoked_subcommand is None:
                await send_cmd_help(ctx)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def advert(self):

        embed=discord.Embed(title="Help us grow", description="We are trying our best to grow our community and we need your help by advertising, if you advert our server 4 times please contact a admin and you will recive a rank called TaZer Rank With some cool features  __**But**__ you must create a invite for our server and create 4 diffrent ones and advert them to other servers they must all be diffrent", color=0x00ed00)
        embed.set_author(name="Advert Our Discord", url='https://tazerprison.enjin.com')
        embed.set_thumbnail(url='https://i.imgur.com/9HTtjgb.png')
        embed.add_field(name="Put this to 4 servers", value="__**TaZerPrison**__, we are a medium sized minehut community with over 4000 join and a goal to reach 6000 we have a update every week or 2. We are a prison server with a few mini games like cookie clicker, pvp and some fun stuff to do on our server join our discord to learn more about our server and how to join it. we also have website you can find on our discord. Join with YOUR_INVITE_CODE_GOSE_HERE ", inline=True)
        embed.add_field(name="------------------------------------------------------------------------", value="You might need to re add the mark down format but you dont have to", inline=True)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def report(self):

        embed=discord.Embed(title="Reporting", description="It is **recommend** to report players on our website but you may report people here as well. But please remember to follow this format when reporting", color=0xed0000)
        embed.set_author(name="Report a player", url='https://tazerprison.enjin.com')
        embed.set_thumbnail(url='https://i.imgur.com/9HTtjgb.png')
        embed.add_field(name="Format", value="(Player reporting), (reasson)", inline=False)
        embed.add_field(name="If you wish to report someone on the website", value="Click the title thats says Report a player", inline=True)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def ranks(self):

        embed=discord.Embed(title="Minecraft Ranks And Website ranks", color=0xfde706)
        embed.set_author(name="Ranks Infomation", url='https://tazerprison.enjin.com/shop')
        embed.add_field(name="Admin-", value="A member of staff that controls the server", inline=False)
        embed.add_field(name="Develpor-", value="Helps with command blocks and sometimes coding. someone that will fix bugs", inline=True)
        embed.add_field(name="Sr.Mod-", value="A well trusted moderator that have more permissions", inline=True)
        embed.add_field(name="Mod-", value="Someone that helps out the server and punsh the ones who need to be.", inline=True)
        embed.add_field(name="Jr.Mod-", value="A new moderator that only just started but not trusted enough for more permissions", inline=True)
        embed.add_field(name="Legend-", value="A rank you can buy with gems on our store tazerprison.enjin.com/shop, has fly permissions and more find out more about this rank on our store", inline=True)
        embed.add_field(name="Mvp-", value="A rank you can buy with gens on our store tazerprison.enjin.com/shop, has fly permissions and more find out more about this rank on our store", inline=True)
        embed.add_field(name="Vip-", value="A rank you can buy with gens on our store tazerprison.enjin.com/shop, has fly permissions and more find out more about this rank on our store", inline=True)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def goals_6000_no(self):

        embed=discord.Embed(title="Reach 6000 Total joins", description="Our current goal is to reach 6000 total server joins on our minehut server.", color=0xed0000)
        embed.set_author(name="Goals", icon_url='http://www.clipartbest.com/cliparts/9c4/zby/9c4zby9gi.png')
        embed.add_field(name="Completed??", value="No", inline=False)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def goals_6000_yes(self):

        embed=discord.Embed(title="Reach 6000 Total joins", description="Our current goal is to reach 6000 total server joins on our minehut server.", color=0x5da039)
        embed.set_author(name="Goals", icon_url='https://www.clker.com/cliparts/R/C/5/I/G/P/green-light-tick-mark-hi.png')
        embed.add_field(name="Completed??", value="Yes", inline=False)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def goals_100_no(self):

        embed=discord.Embed(title="Reach 100 discord users", description="Our current goal is to reach 100 discord memebers. advert our server by going to advert-our-discord to help us. Were half way there ``49 Members ``", color=0xed0000)
        embed.set_author(name="Goals", icon_url='http://www.clipartbest.com/cliparts/9c4/zby/9c4zby9gi.png')
        embed.add_field(name="Completed??", value="No", inline=False)
        await self.bot.say(embed=embed)    

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def goals_100_yes(self):

        embed=discord.Embed(title="Reach 100 discord users", description="Our current goal is to reach 100 discord memebers. advert our server by going to advert-our-discord to help us", color=0x5da039)
        embed.set_author(name="Goals", icon_url='https://www.clker.com/cliparts/R/C/5/I/G/P/green-light-tick-mark-hi.png')
        embed.add_field(name="Completed??", value="Yes", inline=False)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def rules(self):

        embed=discord.Embed(title="Rules", color=0xda039)
        embed.set_thumbnail(url='https://i.imgur.com/9HTtjgb.png')
        embed.add_field(name="1)", value="Do not swear in none nsfw channels", inline=False)
        embed.add_field(name="2)", value="Do not be rude to anyone in cluding staff", inline=False)
        embed.add_field(name="3)", value="Be nice and hepful", inline=False)
        embed.add_field(name="4)", value="Change your discord nickname to your mc name", inline=False)
        embed.add_field(name="If you want minecraft rules go to ", value="https://tazerprison.enjin.com/rules", inline=True)
        await self.bot.say(embed=embed)


    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def gems(self):

        embed=discord.Embed(title="What are gems??", description="Gems are like points and you can spend them on our shop (https://tazerprison.enjin.com) you can buy all sort of things like ranks upgrades and more. __**They is currenly 50% off sale**__", color=0x5da039)
        embed.add_field(name="How do i get gems?", value="You can earn them by playing on our server or even doing achievements **but what are achievements** you can earn achievements by doing challenges for the first time.", inline=True)
        embed.add_field(name="Were do i buy stuff with gems?", value="https://tazerprison.enjin.com/shop", inline=True)
        embed.add_field(name="Why are these a thing?", value="Becuse at the minute i can't setup a proper currency for the shop so i had a idea to add a in-game and website currency ", inline=True)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def giveaway1_no(self):

        embed=discord.Embed(title="Giveaway", description="@everyone More giveaways will come when we complete goals (massive giveaways)", color=0xed0000)
        embed.set_author(name="Not ended yet", icon_url='http://www.clipartbest.com/cliparts/9c4/zby/9c4zby9gi.png')
        embed.add_field(name="What is in this giveaway", value="1x 50000 in game cash (Dosent last long) and 2x Taze ranks in discord", inline=False)
        embed.add_field(name="How do i enter", value="Scroll up and there be active giveaways", inline=True)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def giveaway1_yes(self):

        embed=discord.Embed(title="Giveaway", description="@everyone More giveaways will come when we complete goals (massive giveaways)", color=0x5da039)
        embed.set_author(name="Giveaway Ended", icon_url='https://www.clker.com/cliparts/R/C/5/I/G/P/green-light-tick-mark-hi.png')
        embed.add_field(name="What is in this giveaway", value="1x 50000 in game cash (Dosent last long) and 2x Taze ranks in discord", inline=False)
        embed.add_field(name="How do i enter", value="Scroll up and there be active giveaways", inline=True)
        await self.bot.say(embed=embed)

    @_embed.command(pass_context=True)
    @checks.is_owner()
    async def tazerrank_2(self):

        embed=discord.Embed(title="2 people have TaZer Ranks", description="Lets increese the advertisment Have 2 people have the taze rank to help us just do this one thing in #advert-our-discord", color=0xed0000)
        embed.set_author(name="Goals", icon_url='http://www.clipartbest.com/cliparts/9c4/zby/9c4zby9gi.png')
        embed.add_field(name="Completed?", value="No", inline=True)
        embed.set_footer(text="Current ranks <1 person>")
        await self.bot.say(embed=embed)


    @_embed.command()
    @checks.is_owner()
    async def tazerrank_2_yes(self, user_1, user_2):

        embed=discord.Embed(title="2 people have TaZeR Ranks", description="Lets increese the advertisment Have 2 people have the taze rank to help us just do this one thing in #advert-our-discord", color=0x5da039)
        embed.set_author(name="Goals", icon_url='https://www.clker.com/cliparts/R/C/5/I/G/P/green-light-tick-mark-hi.png')
        embed.add_field(name="Completed?", value="Yes", inline=True)
        embed.set_footer(text="Two people with ranks | " + user_1 + ", " + user_2 + "")
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def suggestion(self, *, suggestion):

        embed=discord.Embed(title="" + suggestion + "", description="Leave a suggestion in this channel for " + suggestion + ", we will look at it and see if we our selfs should add it.", color=0x5da039)
        embed.set_author(name="Suggestions open for ", icon_url='https://www.clker.com/cliparts/R/C/5/I/G/P/green-light-tick-mark-hi.png')
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def update14(self):

        embed=discord.Embed(title="Update 14", url='https://tazerprison.enjin.com/forum/m/44744132/viewthread/30756453-update-14', color=0x5da039)
        embed.set_thumbnail(url='https://i.imgur.com/zu3Eob3.png')
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def update9(self):

        embed=discord.Embed(title="Update 9", url='https://tazerprison.enjin.com/forum/m/44744132/viewthread/30296292-update-9', color=0x5da039)
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def update10(self):

        embed=discord.Embed(title="Update 10", url='https://tazerprison.enjin.com/forum/m/44744132/viewthread/30341890-update-10', color=0x5da039)
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def update11(self):

        embed=discord.Embed(title="Update 11", url='https://tazerprison.enjin.com/forum/m/44744132/viewthread/30391711-update-11', color=0x5da039)
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def update12(self):

        embed=discord.Embed(title="Update 12", url='https://tazerprison.enjin.com/forum/m/44744132/viewthread/30492228-update-12', color=0x5da039)
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def update13(self):

        embed=discord.Embed(title="Update 13", url='https://tazerprison.enjin.com/forum/m/44744132/viewthread/30612106-update-13', color=0x5da039)
        embed.set_thumbnail(url='https://i.imgur.com/zsfc5j8.png')
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def bg(self):

        embed=discord.Embed(title="Boneless Gaming", description="Check these guys out there discord channel is hyped.They also do alt drops so check them out!", color=0xeeff00)
        embed.add_field(name="Link", value="https://discord.gg/TDMWpYX", inline=False)
        await self.bot.say(embed=embed)

    @_embed.command()
    @checks.is_owner()
    async def update15(self):

        embed=discord.Embed(title="Update 15", url='https://tazerprison.enjin.com/forum/m/44744132/viewthread/30612106-update-13', color=0x5da039)
        embed.set_thumbnail(url='https://i.imgur.com/zsfc5j8.png')
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Embed(bot))
