# sync_examples.py

from mangadex.api.sync.client import MangaDexClient

def main():
    # Create a client instance
    client = MangaDexClient()

    # Example of OAuth2 authentication with client credentials
    print("\nAuthenticating with OAuth2...")
    client_id = "your_client_id"  # Replace with actual client ID
    client_secret = "your_client_secret"  # Replace with actual client secret
    
    auth_response = client.authenticate_with_client_credentials(client_id, client_secret)
    print("Authentication Response:", auth_response)

    # Example of fetching manga details (authenticated request)
    print("\nFetching manga details...")
    manga_id = "a96676e5-8ae2-425e-b549-7f15dd34a6d8"  # Replace with actual manga ID
    manga_details = client.get_manga(manga_id)
    print("Manga Details:", manga_details)

    # Example of creating a new manga
    print("\nCreating a new manga...")
    new_manga_data = {
        "title": {"en": "New Manga Title"},
        "description": {"en": "This is a test manga"},
        "publicationDemographic": "seinen",
        "status": "ongoing",
        "contentRating": "safe"
    }
    create_response = client.create_manga(new_manga_data)
    print("Create Manga Response:", create_response)

    # Example of fetching a chapter
    print("\nFetching chapter details...")
    chapter_id = "some-chapter-id"  # Replace with actual chapter ID
    chapter_details = client.get_chapter(chapter_id)
    print("Chapter Details:", chapter_details)

    # Example of fetching user details
    print("\nFetching user details...")
    user_id = "some-user-id"  # Replace with actual user ID
    user_details = client.get_user(user_id)
    print("User Details:", user_details)

    # Example of creating a custom list
    print("\nCreating a custom list...")
    custom_list_data = {
        "name": "My Custom List",
        "visibility": "private"
    }
    custom_list_response = client.create_custom_list(custom_list_data)
    print("Create Custom List Response:", custom_list_response)
    
    # Token refresh demonstration
    print("\nSimulating token expiration...")
    client.token_expires_at = 0  # Force token to expire
    print("Making a request with expired token (should auto-refresh):")
    manga_details = client.get_manga(manga_id)
    print("Request completed successfully after token refresh")

if __name__ == "__main__":
    main()