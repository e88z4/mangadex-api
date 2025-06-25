# File: /mangadex-api/mangadex-api/src/mangadex/models/auth.py

class LoginRequest:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class LoginResponse:
    def __init__(self, token: str, user_id: str):
        self.token = token
        self.user_id = user_id

class LogoutResponse:
    def __init__(self, message: str):
        self.message = message

class RefreshTokenRequest:
    def __init__(self, refresh_token: str):
        self.refresh_token = refresh_token

class RefreshTokenResponse:
    def __init__(self, token: str):
        self.token = token

class CheckResponse:
    def __init__(self, permissions: list):
        self.permissions = permissions

class AuthError:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message