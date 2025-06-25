# File: /mangadex-api/mangadex-api/src/mangadex/models/manga.py

class Manga:
    def __init__(self, id: str, title: str, description: str, authors: list, artists: list, tags: list, status: str, publication_demographic: str, created_at: str, updated_at: str):
        self.id = id
        self.title = title
        self.description = description
        self.authors = authors
        self.artists = artists
        self.tags = tags
        self.status = status
        self.publication_demographic = publication_demographic
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Manga(id={self.id}, title={self.title}, status={self.status})>"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            authors=data.get("authors", []),
            artists=data.get("artists", []),
            tags=data.get("tags", []),
            status=data.get("status"),
            publication_demographic=data.get("publicationDemographic"),
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
        )