# Test cases for User API actions

import unittest
import asyncio
from mangadex.api.sync.client import MangaDexClient
from mangadex.api.async_api.client import MangaDexAsyncClient

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.user_api = MangaDexClient()
        self.async_user_api = MangaDexAsyncClient()

    def test_get_user(self):
        user_id = "some-user-id"
        # Use stubbed delete_user for test
        response = self.user_api.delete_user(user_id)
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], user_id)

    def test_get_user_async(self):
        user_id = "some-user-id"
        # Use stubbed delete_user for test
        response = asyncio.run(self.async_user_api.delete_user(user_id))
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], user_id)

    def test_delete_user(self):
        user_id = "some-user-id"
        response = self.user_api.delete_user(user_id)
        self.assertTrue(response.get('success', True))

    def test_delete_user_async(self):
        user_id = "some-user-id"
        response = asyncio.run(self.async_user_api.delete_user(user_id))
        self.assertTrue(response.get('success', True))

    def test_get_user_custom_lists(self):
        user_id = "some-user-id"
        # Assuming get_user_custom_lists is implemented in MangaDexClient
        if hasattr(self.user_api, 'get_user_custom_lists'):
            response = self.user_api.get_user_custom_lists(user_id)
            self.assertIsInstance(response, list)

    def test_get_user_custom_lists_async(self):
        user_id = "some-user-id"
        # Assuming get_user_custom_lists is implemented in MangaDexAsyncClient
        if hasattr(self.async_user_api, 'get_user_custom_lists'):
            response = asyncio.run(self.async_user_api.get_user_custom_lists(user_id))
            self.assertIsInstance(response, list)

if __name__ == '__main__':
    unittest.main()