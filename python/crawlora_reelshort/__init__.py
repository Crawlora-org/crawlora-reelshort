"""Typed ReelShort client for the Crawlora hosted API."""

from .platform import ReelShortClient, AsyncReelShortClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = ReelShortClient
AsyncClient = AsyncReelShortClient
__version__ = '0.1.0'
DISPLAY_NAME = 'ReelShort'
PLATFORM = 'reelshort'
CONTRACT_REVISION = 'sha256:d05c7c916e44f76874f1d3a98ebf61fce4706f0a7c795a3bc5a64259a6894f4c'

__all__ = [
    "ReelShortClient", "AsyncReelShortClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
