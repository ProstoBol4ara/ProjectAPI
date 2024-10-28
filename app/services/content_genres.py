from repositories import ContentGenresRepository

class ContentGenresService:
    def __init__(self, content_genres_repository: ContentGenresRepository):
        self.content_genres_repository = content_genres_repository

    async def get_content_genres(self):
        content_genres = await self.content_genres_repository.get_content_genres()

        return None if content_genres is None else \
            [{"content_genre_id": content_genre.content_genre_id, "content_id": content_genre.content_id,
              "genre_id": content_genre.genre_id} for content_genre in content_genres]

    async def get_content_genre(self, content_genre_id: int):
        content_genre = await self.content_genres_repository.get_content_genre(content_genre_id=content_genre_id)

        if not content_genre: raise ValueError("Content genre not found")

        return {"content_genre_id": content_genre.content_genre_id, "content_id": content_genre.content_id,
                "genre_id": content_genre.genre_id}

    async def create_content_genre(self, content_id: int, genres_id: int):
        new_content_genre = await self.content_genres_repository\
            .create_content_genre(content_id=content_id, genres_id=genres_id)

        return {"content_genre_id": new_content_genre.content_genre_id, "content_id": new_content_genre.content_id,
                "genres_id": new_content_genre.genres_id}

    async def update_content_genre(self, content_genre_id: int, content_id: int = None, genres_id: int = None):
        content_genre = await self.content_genres_repository\
            .update_content_genre(content_genre_id=content_genre_id, content_id=content_id, genres_id=genres_id)

        if not content_genre: raise ValueError("Content genre not found")

        return {"content_genre_id": content_genre.content_genre_id, "content_id": content_genre.content_id,
                "genres_id": content_genre.genres_id}

    async def delete_content_genre(self, content_genre_id: int):
        if not await self.content_genres_repository.delete_content_genre(content_genre_id=content_genre_id):
            raise ValueError("Content genre not found")
