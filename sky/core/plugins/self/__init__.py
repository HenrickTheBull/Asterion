from .information import AsterInformation


__all__ = [
    AsterInformation,
]


def setup(bot):
    bot.plugins.setup(__file__)
