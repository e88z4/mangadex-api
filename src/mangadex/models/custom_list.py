# File: /mangadex-api/mangadex-api/src/mangadex/models/custom_list.py

class CustomList:
    def __init__(self, id: str, name: str, description: str, user_id: str, manga_ids: list):
        self.id = id
        self.name = name
        self.description = description
        self.user_id = user_id
        self.manga_ids = manga_ids

    def add_manga(self, manga_id: str):
        if manga_id not in self.manga_ids:
            self.manga_ids.append(manga_id)

    def remove_manga(self, manga_id: str):
        if manga_id in self.manga_ids:
            self.manga_ids.remove(manga_id)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id,
            "manga_ids": self.manga_ids
        }