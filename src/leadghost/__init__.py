"""LeadGhost - A LinkedIn lead generation automation tool."""

__version__ = "0.1.0"
__name__ = "LeadGhost"

from leadghost.bot import Bot
from leadghost.selenium_bot import SeleniumBot
from leadghost.utils import generate_md5

__all__ = [
    "Bot",
    "SeleniumBot",
    "generate_md5",
]
