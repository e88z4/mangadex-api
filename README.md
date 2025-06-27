# MangaDex API Wrapper

This project provides a Python wrapper for the MangaDex API, allowing both synchronous and asynchronous interactions with the API. The wrapper includes implementations for various API actions, making it easier to integrate MangaDex functionalities into your applications.

## Features

- **Synchronous and Asynchronous Implementations**: The wrapper supports both synchronous and asynchronous API calls, allowing flexibility in how you choose to interact with the API.
- **Comprehensive API Coverage**: The wrapper includes methods for all major API actions, including but not limited to:
  - User Authentication (Login, Logout, Refresh Token)
  - Manga Operations (Fetch Manga Details, Create, Update, Delete)
  - Chapter Management (Fetch Chapters, Create, Update, Delete)
  - Group Management (Fetch Groups, Create, Update, Delete)
  - Custom List Management (Create, Update, Delete Custom Lists)
  - User Management (Fetch User Details, Follow/Unfollow Manga or Groups)

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

### Synchronous Example

```python
from mangadex.api import MangaDexClient
client = MangaDexClient()
# Authenticate with OAuth2 client credentials
auth_response = client.authenticate_with_client_credentials(client_id='your_client_id', client_secret='your_client_secret')
print(auth_response)
```

### Asynchronous Example

```python
import asyncio
from mangadex.api import MangaDexAsyncClient

async def main():
    client = MangaDexAsyncClient()
    auth_response = await client.authenticate_with_client_credentials(client_id='your_client_id', client_secret='your_client_secret')
    print(auth_response)
    await client.close()

asyncio.run(main())
```

## Examples

See the `examples/` directory for more comprehensive usage, including OAuth2 password flow, manga operations, and more.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.