# File: /mangadex-api/mangadex-api/src/mangadex/models/group.py

class Group:
    def __init__(self, id: str, name: str, created_at: str, updated_at: str):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Group id={self.id} name={self.name}>"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }