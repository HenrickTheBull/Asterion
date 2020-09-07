#Initial Init, this is a bit of a cascade operation from this point on.

from .core import Aster
from .core import utilities
from .core.functions import exceptions


__release__ = "St Michel Ave"
__version__ = "0.0.118"


def get_bot():
    return Aster(version=__version__, release=__release__)