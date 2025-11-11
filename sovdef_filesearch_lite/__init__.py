"""
SovDef FileSearch Lite
======================

Lightweight file search system for MVPs
Google File Search level convenience with quality guarantees
"""

__version__ = "1.0.0"
__author__ = "SovDef"
__license__ = "MIT"

from .core import SovDefLite
from .config import Config

__all__ = ["SovDefLite", "Config"]
