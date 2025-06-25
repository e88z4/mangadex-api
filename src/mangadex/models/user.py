# File: /mangadex-api/mangadex-api/src/mangadex/models/user.py

class User:
    def __init__(self, id: str, username: str, email: str, created_at: str, updated_at: str):
        self.id = id
        self.username = username
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            email=data.get("email"),
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }