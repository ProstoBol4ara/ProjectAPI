from repositories import ContentDirectorsRepository


class ContentDirectorsService:
    def __init__(self, repository: ContentDirectorsRepository):
        self.repository = repository

    async def get_all(self):
        content_directors = await self.repository.get_all()

        return (
            None
            if content_directors is None
            else [
                {
                    "content_director_id": content_director.content_director_id,
                    "content_id": content_director.content_id,
                    "director_id": content_director.director_id,
                }
                for content_director in content_directors
            ]
        )

    async def get_one(self, content_director_id: int):
        if not content_director_id:
            raise ValueError("content_director_id cannot be empty")

        content_director = await self.repository.get_one(
            content_director_id=content_director_id
        )

        if not content_director:
            raise ValueError("Content director not found")

        return {
            "content_director_id": content_director.content_director_id,
            "content_id": content_director.content_id,
            "director_id": content_director.director_id,
        }

    async def create(self, content_id: int, director_id: int):
        if not content_id or not director_id:
            raise ValueError("content_id and director_id cannot be empty")

        new_content_director = await self.repository.create(
            content_id=content_id, director_id=director_id
        )

        return {
            "content_director_id": new_content_director.content_director_id,
            "content_id": new_content_director.content_id,
            "director_id": new_content_director.director_id,
        }

    async def update(
        self, content_director_id: int, content_id: int = None, director_id: int = None
    ):
        if not content_director_id:
            raise ValueError("content_director_id cannot be empty")

        content_director = await self.repository.update(
            content_director_id=content_director_id,
            content_id=content_id,
            director_id=director_id,
        )

        if not content_director:
            raise ValueError("Content director not found")

        return {
            "content_director_id": content_director.content_director_id,
            "content_id": content_director.content_id,
            "director_id": content_director.director_id,
        }

    async def delete(self, content_director_id: int):
        if not content_director_id:
            raise ValueError("content_director_id cannot be empty")

        if not (
            delete_content_director := await self.repository.delete(
                content_director_id=content_director_id
            )
        ):
            raise ValueError("Content director not found")
        return delete_content_director
