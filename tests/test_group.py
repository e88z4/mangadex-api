# Test cases for the Group API actions using the main client classes

import unittest
import asyncio
from mangadex.api.sync.client import MangaDexClient
from mangadex.api import MangaDexAsyncClient

class TestGroupAPI(unittest.TestCase):
    def setUp(self):
        self.sync_client = MangaDexClient()
        self.async_client = MangaDexAsyncClient()

    def test_get_group(self):
        group_id = "some-group-id"
        response = self.sync_client.get_group(group_id)
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], group_id)

    def test_create_group(self):
        group_data = {"name": "Test Group", "language": "en"}
        response = self.sync_client.create_group(group_data)
        self.assertIsNotNone(response)
        self.assertEqual(response['name'], group_data['name'])

    def test_update_group(self):
        group_id = "some-group-id"
        update_data = {"name": "Updated Group Name"}
        response = self.sync_client.update_group(group_id, update_data)
        self.assertIsNotNone(response)
        self.assertEqual(response['name'], update_data['name'])

    def test_delete_group(self):
        group_id = "some-group-id"
        response = self.sync_client.delete_group(group_id)
        self.assertTrue(response.get('success', True))

    def test_async_get_group(self):
        group_id = "some-group-id"
        response = asyncio.run(self.async_client.get_group(group_id))
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], group_id)

    def test_async_create_group(self):
        group_data = {"name": "Test Group", "language": "en"}
        response = asyncio.run(self.async_client.create_group(group_data))
        self.assertIsNotNone(response)
        self.assertEqual(response['name'], group_data['name'])

    def test_async_update_group(self):
        group_id = "some-group-id"
        update_data = {"name": "Updated Group Name"}
        response = asyncio.run(self.async_client.update_group(group_id, update_data))
        self.assertIsNotNone(response)
        self.assertEqual(response['name'], update_data['name'])

    def test_async_delete_group(self):
        group_id = "some-group-id"
        response = asyncio.run(self.async_client.delete_group(group_id))
        self.assertTrue(response.get('success', True))

if __name__ == '__main__':
    unittest.main()