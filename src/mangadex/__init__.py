# File: /mangadex-api/mangadex-api/src/mangadex/__init__.py

"""
This is the MangaDex API wrapper module.

This module provides both synchronous and asynchronous implementations for interacting with the MangaDex API.

Available API actions:
- Authentication
  - Login
  - Logout
  - Refresh Token
  - Check Permissions
- Manga
  - Fetch Manga List
  - Fetch Manga Details
  - Create Manga
  - Update Manga
  - Delete Manga
- Chapter
  - Fetch Chapter List
  - Fetch Chapter Details
  - Create Chapter
  - Update Chapter
  - Delete Chapter
- Group
  - Fetch Scanlation Group List
  - Fetch Scanlation Group Details
  - Create Scanlation Group
  - Update Scanlation Group
  - Delete Scanlation Group
- User
  - Fetch User List
  - Fetch User Details
  - Delete User
- Custom List
  - Create Custom List
  - Update Custom List
  - Delete Custom List
  - Follow/Unfollow Custom List
"""

from .api.sync import *
from .models import *
from .utils import *
from .constants import *