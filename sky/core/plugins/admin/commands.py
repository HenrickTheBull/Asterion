from sky.core.utilities.converters import PrimeTierConverter
from sky.core.utilities.converters import AsterGuildConverter
from sky.core.utilities.converters import AsterUserProfileConverter

import typing

from .base import Admin
from discord.ext import commands


# noinspection PyUnresolvedReferences
class AdminCommands(Admin):

    @Admin.command(name="giveprime")
    async def give_prime(
            self, ctx, user: AsterUserProfileConverter,
            server: typing.Optional[CosmosGuildConverter] = None,
            tier: typing.Optional[PrimeTierConverter] = None,
    ):
        if not await ctx.confirm():
            return
        extra = str()
        guild_id = None
        if server:
            guild_id = server.id
            extra = f"and {server.guild.name}"
        await user.make_prime(tier=tier, guild_id=guild_id)
        await ctx.send_line(f"🎉    {user.user.name} {extra} has been given prime.")

    @give_prime.error
    async def give_prime_error(self, ctx, error):
        if isinstance(error, commands.BadUnionArgument):
            return await ctx.send_line(f"❌    A dark argument was passed.")

    @Admin.command(name="removeprime")
    async def remove_prime(self, ctx, *, user: AsterUserProfileConverter):
        if not await ctx.confirm():
            return
        await user.remove_prime()
        await ctx.send_line(f"✅    Removed prime from {user.name}.")

    @remove_prime.error
    async def remove_prime_error(self, ctx, error):
        return await self.give_prime_error(ctx, error)

    @Admin.command(name="givefermions")
    async def give_fermions(self, ctx, user: AsterUserProfileConverter, fermions: int):
        if not await ctx.confirm():
            return
        await user.give_fermions(fermions)
        await ctx.send_line(f"✅    Gave {fermions} fermions to {user.name}.")