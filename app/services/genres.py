from repositories import GenresRepository

class GenresService:
    def __init__(self, genres_repository: GenresRepository):
        self.genres_repository = genres_repository

    async def get_genres(self):
        genres = await self.genres_repository.get_genres()
        return None if genres is None else [{"genre_id": genre.genre_id, "genre_name": genre.genre_name} for genre in genres]

    async def get_genre(self, genre_id: int):
        genre = await self.genres_repository.get_genre(genre_id=genre_id)
        return None if genre is None else {"genre_id": genre.genre_id, "genre_name": genre.genre_name}

    async def create_genre(self, genre_name: str):
        new_genre = await self.genres_repository.create_genre(genre_name=genre_name)
        return {"genre_id": new_genre.genre_id, "genre_name": new_genre.genre_name}

    async def update_genre(self, genre_id: int, genre_name: str = None):
        genre = await self.genres_repository.update_genre(genre_id=genre_id, genre_name=genre_name)
        return None if genre is None else {"genre_id": genre.genre_id, "genre_name": genre.genre_name}

    async def delete_genre(self, genre_id: int):
        return await self.genres_repository.delete_genre(genre_id=genre_id)
    