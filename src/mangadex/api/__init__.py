# File: /mangadex-api/mangadex-api/src/mangadex/api/__init__.py

from .sync.client import MangaDexClient
from importlib import import_module

# Workaround for reserved keyword 'async' in import
MangaDexAsyncClient = import_module('mangadex.api.async.client').MangaDexAsyncClient

__all__ = [
    'MangaDexClient',
    'MangaDexAsyncClient',
]