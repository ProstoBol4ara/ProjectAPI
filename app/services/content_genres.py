from repositories import ContentGenresRepository

class ContentGenresService:
    def __init__(self, content_genres_repository: ContentGenresRepository):
        self.content_genres_repository = content_genres_repository
    
    async def get_content_genres(self):
        return await self.content_genres_repository.get_content_genres()

    async def get_content_genre(self, content_genre_id: int):
        return await self.content_genres_repository.get_content_genre(content_genre_id=content_genre_id)

    async def create_content_genre(self, content_id: int, genres_id: int):
        return await self.content_genres_repository.create_content_genre(content_id=content_id, genres_id=genres_id)

    async def update_content_genre(self, content_genre_id: int, content_id: int = None, genres_id: int = None):
        return await self.content_genres_repository.update_content_genre(content_genre_id=content_genre_id, content_id=content_id, genres_id=genres_id)

    async def delete_content_genre(self, content_genre_id: int):
        await self.content_genres_repository.delete_content_genre(content_genre_id=content_genre_id)
    