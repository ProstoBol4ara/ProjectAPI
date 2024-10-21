from repositories import GenresRepository

class GenresService:
    def __init__(self, genres_repository: Genres):
        self.genres_repository = genres_repository

    async def get_genres(self):
        return await self.genres_repository.get_genres()

    async def get_genre(self, genre_id: int):
        return await self.genres_repository.get_genre(genre_id=genre_id)

    async def create_genre(self, genre_name: str):
        return await self.genres_repository.create_genre(genre_name=genre_name)

    async def update_genre(self, genre_id: int, genre_name: str = None):
        return await self.genres_repository.update_genre(genre_id=genre_id, genre_name=genre_name)

    async def delete_genre(self, genre_id: int):
        await self.genres_repository.delete_genre(genre_id=genre_id)
    