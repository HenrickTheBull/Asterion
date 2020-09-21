from . import time

from discord.ext import commands


class RoleConvertor(commands.Converter):

    async def convert(self, ctx, argument):
        try:
            return [await commands.RoleConverter().convert(ctx, argument)]
        except commands.BadArgument:
            return [await commands.RoleConverter().convert(ctx, raw_role) for raw_role in argument.split()]


class AsterGuildConverter(commands.Converter):

    async def convert(self, ctx, argument):
        if not (guild := ctx.bot.get_guild(int(argument))):
            raise commands.BadArgument
        return await ctx.bot.guild_cache.get_profile(guild.id)


class AsterUserProfileConverter(commands.Converter):

    async def convert(self, ctx, argument):
        if not (user := await commands.UserConverter().convert(ctx, argument)):
            raise commands.BadArgument
        return await ctx.bot.profile_cache.get_profile(user.id)


class HumanTimeDeltaConverter(commands.Converter):

    async def convert(self, ctx, argument):
        try:
            return time.HumanDateTimeMixin.from_human_timedelta(argument)
        except ValueError:
            raise commands.BadArgument


class HumanDatetimeConverter(HumanTimeDeltaConverter):

    async def convert(self, ctx, argument):
        argument = argument.lower()
        try:
            if argument.lower().startswith("in"):
                return await super().convert(ctx, argument.lstrip("in "))
            return await super().convert(ctx, argument)
        except (ValueError, commands.BadArgument):
            try:
                return time.HumanDateTimeMixin.from_human(argument)
            except ValueError:
                raise commands.BadArgument
