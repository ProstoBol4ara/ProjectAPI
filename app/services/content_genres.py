from repositories import ContentGenresRepository


class ContentGenresService:
    def __init__(self, repository: ContentGenresRepository):
        self.repository = repository

    async def get_all(self):
        content_genres = await self.repository.get_all()

        return (
            None
            if content_genres is None
            else [
                {
                    "content_genre_id": content_genre.content_genre_id,
                    "content_id": content_genre.content_id,
                    "genre_id": content_genre.genre_id,
                }
                for content_genre in content_genres
            ]
        )

    async def get_one(self, content_genre_id: int):
        if not content_genre_id:
            raise ValueError("content_genre_id cannot be empty")

        content_genre = await self.repository.get_one(content_genre_id=content_genre_id)

        if not content_genre:
            raise ValueError("Content genre not found")

        return {
            "content_genre_id": content_genre.content_genre_id,
            "content_id": content_genre.content_id,
            "genre_id": content_genre.genre_id,
        }

    async def create(self, content_id: int, genre_id: int):
        if not content_id or not genre_id:
            raise ValueError("content_id and genres_id cannot be empty")

        new_content_genre = await self.repository.create(
            content_id=content_id, genre_id=genre_id
        )

        return {
            "content_genre_id": new_content_genre.content_genre_id,
            "content_id": new_content_genre.content_id,
            "genre_id": new_content_genre.genre_id,
        }

    async def update(
        self, content_genre_id: int, content_id: int = None, genre_id: int = None
    ):
        if not content_genre_id:
            raise ValueError("content_genre_id cannot be empty")

        content_genre = await self.repository.update(
            content_genre_id=content_genre_id, content_id=content_id, genre_id=genre_id
        )

        if not content_genre:
            raise ValueError("Content genre not found")

        return {
            "content_genre_id": content_genre.content_genre_id,
            "content_id": content_genre.content_id,
            "genre_id": content_genre.genre_id,
        }

    async def delete(self, content_genre_id: int):
        if not content_genre_id:
            raise ValueError("content_genre_id cannot be empty")

        if not (
            delete_content_genre := await self.repository.delete(
                content_genre_id=content_genre_id
            )
        ):
            raise ValueError("Content genre not found")
        return delete_content_genre
