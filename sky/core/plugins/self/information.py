from ...functions import Cog


class AsterInformation(Cog):

    def __init__(self, plugin):
        super().__init__()
        self.plugin = plugin

    
    @Cog.command(name="invite")
    async def invite_aster(self, ctx):
        """Invite Asterion to any of the server you manage."""
        res = "Click here to invite Asterion to your server."
        await ctx.send_line(res, icon_url=self.bot.theme.images.invite, author_url=self.bot.configs.discord.invite_url)
