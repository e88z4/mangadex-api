# File: /mangadex-api/mangadex-api/src/mangadex/constants.py

BASE_URL = "https://api.mangadex.org"
API_VERSION = "v5.12.0"

# Endpoints
PING_ENDPOINT = "/ping"
MANGA_ENDPOINT = "/manga"
AUTH_LOGIN_ENDPOINT = "/auth/login"
AUTH_CHECK_ENDPOINT = "/auth/check"
AUTH_LOGOUT_ENDPOINT = "/auth/logout"
AUTH_REFRESH_ENDPOINT = "/auth/refresh"
CLIENT_ENDPOINT = "/client"
GROUP_ENDPOINT = "/group"
USER_ENDPOINT = "/user"
CUSTOM_LIST_ENDPOINT = "/list"
CHAPTER_ENDPOINT = "/chapter"

# Content Types
CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE_FORM = "application/x-www-form-urlencoded"

# Error Messages
ERROR_UNAUTHORIZED = "Unauthorized access. Please check your credentials."
ERROR_FORBIDDEN = "Forbidden access. You do not have permission to perform this action."
ERROR_NOT_FOUND = "Resource not found."
ERROR_BAD_REQUEST = "Bad request. Please check your input."