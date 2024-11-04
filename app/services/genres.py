from repositories import GenresRepository


class GenresService:
    def __init__(self, repository: GenresRepository):
        self.repository = repository

    async def get_all(self):
        genres = await self.repository.get_all()
        return (
            None
            if genres is None
            else [
                {"genre_id": genre.genre_id, "genre_name": genre.genre_name}
                for genre in genres
            ]
        )

    async def get_one(self, genre_id: int):
        if not genre_id:
            raise ValueError("genre_id cannot be empty")

        genre = await self.repository.get_one(genre_id=genre_id)

        if not genre:
            raise ValueError("Genre not found")

        return {"genre_id": genre.genre_id, "genre_name": genre.genre_name}

    async def create(self, genre_name: str):
        if not genre_name:
            raise ValueError("genre_name cannot be empty")

        new_genre = await self.repository.create(genre_name=genre_name)
        return {"genre_id": new_genre.genre_id, "genre_name": new_genre.genre_name}

    async def update(self, genre_id: int, genre_name: str = None):
        if not genre_id:
            raise ValueError("genre_id cannot be empty")

        genre = await self.repository.update(genre_id=genre_id, genre_name=genre_name)

        if not genre:
            raise ValueError("Genre not found")

        return {"genre_id": genre.genre_id, "genre_name": genre.genre_name}

    async def delete(self, genre_id: int):
        if not genre_id:
            raise ValueError("genre_id cannot be empty")

        if not (delete_genre := await self.repository.delete(genre_id=genre_id)):
            raise ValueError("Genre not found")
        return delete_genre
