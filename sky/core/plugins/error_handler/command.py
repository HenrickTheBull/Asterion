from ...functions.context.functions.paginators import NoEntriesError

import sys
import asyncio
import discord
import traceback

from ...functions import Cog
from sky import exceptions
from discord.ext import commands
from sentry_sdk import configure_scope


class CommandErrorHandler(Cog):

    def __init__(self, plugin):
        super().__init__()
        self.plugin = plugin

    @staticmethod
    async def __send_response(ctx, emote_url, content, **kwargs):
        try:
            return await ctx.send_line(content, emote_url, color=discord.Color(0xFF1744), **kwargs)
        except discord.Forbidden:
            pass

    @Cog.listener()
    async def on_command_error(self, ctx, error):

        images = self.bot.theme.images

        try:
            original = error.original
        except AttributeError:
            pass
        else:
            if isinstance(original, discord.Forbidden):
                return
            elif isinstance(original, exceptions.UserIsBotError):
                return await ctx.send_line("Sorry Bro Bot, I only respond to users.", images.robot)

        if isinstance(error, discord.Forbidden):
            pass

        elif getattr(error, "handled", False):
            pass    # Silently pass internally handled exceptions.

        elif isinstance(error, (exceptions.GuildNotPrime, exceptions.UserNotPrime)):
            # Tried to use prime function in non-prime guild.
            await ctx.send_line(error.message, icon_url=images.privacy, author_url=self.bot.configs.info.patreon)

        elif isinstance(error, exceptions.DisabledFunctionError):
            if error.globally:
                res = "That function has been disabled in this server."
            else:
                res = "That function has been disabled in this channel."
            await self.__send_response(ctx, images.unavailable, res)

        elif isinstance(error, exceptions.CosmosIsDisableError):
            pass

        elif isinstance(error, commands.BotMissingPermissions):
            await self.__send_response(
                ctx, images.mandenied,
                f"Bot is missing {error.missing_perms[0].replace('_', ' ').title()} permissions to run that command.")

        elif isinstance(error, commands.MissingPermissions):
            await self.__send_response(
                ctx, images.denied,
                f"You're missing {error.missing_perms[0].replace('_', ' ').title()} permissions to run that command.")

        elif isinstance(error, commands.PrivateMessageOnly):
            dm_channel = ctx.author.dm_channel or await ctx.author.create_dm()
            await self.__send_response(
                ctx, images.feedback, "That command can only be used in my DMs.",
                author_url=f"https://discord.com/channels/@me/{dm_channel.id}"
            )

        elif isinstance(error, commands.CheckFailure):
            await self.__send_response(ctx, images.denied, "You're not allowed to use that command.")

        elif isinstance(error, commands.UserInputError):
            await self.__send_response(
                ctx, images.error, "Unable to recognize the specified parameter or wrong command syntax.")

        elif isinstance(error, NoEntriesError):
            await ctx.message.add_reaction(self.bot.emotes.misc.nill)

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction(self.bot.emotes.misc.clock)

        elif isinstance(error, commands.CommandNotFound):
            pass

        elif isinstance(error, asyncio.TimeoutError):
            pass

        else:
            with configure_scope() as scope:
                scope._user = {"username": str(ctx.author), "id": ctx.author.id}
                extras = dict()
                if ctx.guild:
                    extras = {"guild": ctx.guild.name, "guild_id": ctx.guild.id}
                extras.update({"command": ctx.command.name, "args": ctx.args, "kwargs": ctx.kwargs})
                scope._extras = extras
            self.bot.eh.sentry.capture_exception(error)
            self.bot.log.debug(f"Ignoring exception in command {ctx.command}")
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)