from .presence import Presence

__all__ = [Presence]    # Fast.


def setup(bot):
    bot.plugins.setup(__file__) 
