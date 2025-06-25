#!/usr/bin/env python
# oauth_examples.py

"""
Examples of using the MangaDex API with OAuth2 authentication.
These examples demonstrate how to:
1. Authenticate with client credentials (personal clients)
2. Make authenticated API calls
3. Handle token refresh
"""

import asyncio
import time
from mangadex.api.sync.client import MangaDexClient
from mangadex.api.async_api.client import MangaDexAsyncClient

# Example of using the synchronous client with OAuth2
def sync_example():
    print("=== Synchronous Client Example ===")
    
    # Create client
    client = MangaDexClient()
    
    # OAuth2 credentials
    # Replace these with your actual credentials
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    username = "your_username"
    password = "your_password"
    
    try:
        # Method 1: Authenticate with client credentials (for applications)
        print("\n[Method 1] Authenticating with client credentials...")
        auth_result = client.authenticate_with_client_credentials(client_id, client_secret)
        print(f"Authentication successful: Token expires in {auth_result.get('expires_in')} seconds")
        
        # Get manga details (authenticated request)
        print("\nFetching manga details:")
        manga_id = "a96676e5-8ae2-425e-b549-7f15dd34a6d8"  # Replace with actual manga ID
        manga_result = client.get_manga(manga_id)
        print(f"Manga title: {manga_result.get('data', {}).get('attributes', {}).get('title', {}).get('en', 'N/A')}")
        
        # Search for manga
        print("\nSearching for manga:")
        manga_data = {
            "title": "One Piece"
        }
        search_result = client.search_manga(manga_data)
        print(f"Found {len(search_result.get('data', []))} manga in search results")
        
        # Simulate token expiration and automatic refresh
        print("\nSimulating token expiration...")
        client.token_expires_at = time.time() - 1  # Force token to appear expired
        print("Making a request with expired token, should trigger auto-refresh:")
        manga_result = client.get_manga(manga_id)
        print("Request successfully completed after token refresh")
        
        # Method 2: Authenticate with password (for end users)
        print("\n[Method 2] Authenticating with username/password...")
        # Create a new client to demonstrate the password flow
        password_client = MangaDexClient()
        auth_result = password_client.authenticate_with_password(
            username=username, 
            password=password,
            client_id=client_id,
            client_secret=client_secret
        )
        print(f"Authentication successful: Token expires in {auth_result.get('expires_in')} seconds")
        
        # Make an authenticated request with the password-based token
        print("\nFetching manga details with password authentication:")
        manga_result = password_client.get_manga(manga_id)
        print(f"Manga title: {manga_result.get('data', {}).get('attributes', {}).get('title', {}).get('en', 'N/A')}")
        
    except Exception as e:
        print(f"Error: {e}")


# Example of using the asynchronous client with OAuth2
async def async_example():
    print("\n=== Asynchronous Client Example ===")
    
    # Create client
    client = MangaDexAsyncClient()
    
    # OAuth2 credentials
    # Replace these with your actual credentials
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    username = "your_username"
    password = "your_password"
    
    try:
        # Method 1: Authenticate with client credentials (for applications)
        print("\n[Method 1] Authenticating with client credentials...")
        auth_result = await client.authenticate_with_client_credentials(client_id, client_secret)
        print(f"Authentication successful: Token expires in {auth_result.get('expires_in')} seconds")
        
        # Get manga details (authenticated request)
        print("\nFetching manga details:")
        manga_id = "a96676e5-8ae2-425e-b549-7f15dd34a6d8"  # Replace with actual manga ID
        manga_result = await client.get_manga(manga_id)
        print(f"Manga title: {manga_result.get('data', {}).get('attributes', {}).get('title', {}).get('en', 'N/A')}")
        
        # Search for manga
        print("\nSearching for manga:")
        search_result = await client.search_manga(title="One Piece")
        print(f"Found {len(search_result.get('data', []))} manga in search results")
        
        # Simulate token expiration and automatic refresh
        print("\nSimulating token expiration...")
        client.token_expires_at = time.time() - 1  # Force token to appear expired
        print("Making a request with expired token, should trigger auto-refresh:")
        manga_result = await client.get_manga(manga_id)
        print("Request successfully completed after token refresh")

        # Method 2: Authenticate with password (for end users)
        print("\n[Method 2] Authenticating with username/password...")
        # Create a new client to demonstrate the password flow
        password_client = MangaDexAsyncClient()
        auth_result = await password_client.authenticate_with_password(
            username=username, 
            password=password,
            client_id=client_id,
            client_secret=client_secret
        )
        print(f"Authentication successful: Token expires in {auth_result.get('expires_in')} seconds")
        
        # Make an authenticated request with the password-based token
        print("\nFetching manga details with password authentication:")
        manga_result = await password_client.get_manga(manga_id)
        print(f"Manga title: {manga_result.get('data', {}).get('attributes', {}).get('title', {}).get('en', 'N/A')}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Always close the client to clean up resources
        await client.close()
        if 'password_client' in locals() and password_client.session:
            await password_client.close()


if __name__ == "__main__":
    # Run synchronous example
    sync_example()
    
    # Run asynchronous example
    asyncio.run(async_example())
