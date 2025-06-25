# File: /mangadex-api/mangadex-api/src/mangadex/api/__init__.py

from .sync.client import MangaDexClient as SyncClient
from .async_api.client import MangaDexAsyncClient as AsyncClient

__all__ = [
    'SyncClient',
    'AsyncClient',
]