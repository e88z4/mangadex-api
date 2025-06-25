# File: /mangadex-api/mangadex-api/src/mangadex/models/chapter.py

class Chapter:
    def __init__(self, id: str, title: str, manga_id: str, volume: str, chapter: str, language: str, created_at: str, updated_at: str):
        self.id = id
        self.title = title
        self.manga_id = manga_id
        self.volume = volume
        self.chapter = chapter
        self.language = language
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Chapter id={self.id} title={self.title} manga_id={self.manga_id} volume={self.volume} chapter={self.chapter}>"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            manga_id=data.get("manga_id"),
            volume=data.get("volume"),
            chapter=data.get("chapter"),
            language=data.get("language"),
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
        )