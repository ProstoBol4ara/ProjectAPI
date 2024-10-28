from repositories import ContentDirectorsRepository

class ContentDirectorsService:
    def __init__(self, content_directors_repository: ContentDirectorsRepository):
        self.content_directors_repository = content_directors_repository

    async def get_content_directors(self):
        content_directors = await self.content_directors_repository.get_content_directors()
        return None if content_directors is None else [{"content_director_id": content_director.content_director_id, "content_id": content_director.content_id, "director_id": content_director.director_id} for content_director in content_directors]

    async def get_content_director(self, content_director_id: int):
        content_director = await self.content_directors_repository.get_content_director(content_director_id=content_director_id)
        return None if content_director is None else {"content_director_id": content_director.content_director_id, "content_id": content_director.content_id, "director_id": content_director.director_id}

    async def create_content_director(self, content_id: int, director_id: int):
        new_content_director = await self.content_directors_repository.create_content_director(content_id=content_id, director_id=director_id)
        return {"content_director_id": new_content_director.content_director_id, "content_id": new_content_director.content_id, "director_id": new_content_director.director_id}

    async def update_content_director(self, content_director_id: int, content_id: int = None, director_id: int = None):
        content_director = await self.content_directors_repository.update_content_director(content_director_id=content_director_id, content_id=content_id, director_id=director_id)
        return None if content_director is None else {"content_director_id": content_director.content_director_id, "content_id": content_director.content_id, "director_id": content_director.director_id}

    async def delete_content_director(self, content_director_id: int):
        return await self.content_directors_repository.delete_content_director(content_director_id=content_director_id)
