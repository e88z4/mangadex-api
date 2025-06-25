# async_examples.py

import asyncio
from mangadex.api.async_api.client import MangaDexAsyncClient

async def main():
    # Create an instance of the AsyncClient
    client = MangaDexAsyncClient()
    
    try:
        # Example of logging in using OAuth2
        print("\nAuthenticating with OAuth2...")
        # Replace with your actual credentials
        client_id = "your_client_id"
        client_secret = "your_client_secret"
        
        auth_response = await client.authenticate_with_client_credentials(client_id, client_secret)
        print('Authentication Response:', auth_response)
        
        # Example of fetching manga details (with authentication)
        print("\nFetching manga details...")
        manga_id = "a96676e5-8ae2-425e-b549-7f15dd34a6d8"  # Example ID, replace with actual
        manga_response = await client.get_manga(manga_id)
        print('Manga Details:', manga_response)
        
        # Example of creating a new manga
        print("\nCreating a new manga...")
        manga_data = {
            "title": {"en": "New Manga Title"},
            "description": {"en": "This is a test manga"},
            "publicationDemographic": "seinen",
            "status": "ongoing",
            "contentRating": "safe"
        }
        new_manga_response = await client.create_manga(manga_data)
        print('New Manga Created:', new_manga_response)
        
        # Example of fetching a chapter
        print("\nFetching chapter details...")
        chapter_id = "chapter_id_here"  # Replace with actual
        chapter_response = await client.get_chapter(chapter_id)
        print('Chapter Details:', chapter_response)
        
        # Example of fetching user details
        print("\nFetching user details...")
        user_id = "user_id_here"  # Replace with actual
        user_response = await client.get_user(user_id)
        print('User Details:', user_response)
        
        # Example of creating a custom list
        print("\nCreating a custom list...")
        list_data = {"name": "My Custom List", "visibility": "private"}
        custom_list_response = await client.create_custom_list(list_data)
        print('Custom List Created:', custom_list_response)
    finally:
        # Important: Always close the client to release resources
        await client.close()

if __name__ == '__main__':
    asyncio.run(main())