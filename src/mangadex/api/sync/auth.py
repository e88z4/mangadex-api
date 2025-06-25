# File: /mangadex-api/mangadex-api/src/mangadex/api/sync/auth.py

import requests

class AuthAPI:
    BASE_URL = 'https://api.mangadex.org/auth'

    def login(self, username, password):
        response = requests.post(f'{self.BASE_URL}/login', json={
            'username': username,
            'password': password
        })
        return response.json()

    def logout(self, token):
        response = requests.post(f'{self.BASE_URL}/logout', headers={
            'Authorization': f'Bearer {token}'
        })
        return response.json()

    def refresh_token(self, refresh_token):
        response = requests.post(f'{self.BASE_URL}/refresh', json={
            'refresh_token': refresh_token
        })
        return response.json()

    def check_permissions(self, token):
        response = requests.get(f'{self.BASE_URL}/check', headers={
            'Authorization': f'Bearer {token}'
        })
        return response.json()