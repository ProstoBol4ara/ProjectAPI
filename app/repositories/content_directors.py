from database import AsyncSession
from models import ContentDirectors

class ContentDirectorsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_content_directors(self):
        content_directors = await self.db.execute(select(ContentDirectors))
        return content_directors.scalar().all()

    async def get_content_director(self, content_director_id: int):
        content_director = await self.db.execute(
            select(ContentDirectors).filter(ContentDirectors.content_director_id == content_director_id)
        )
        return content_director.scalar_one_or_none()

    async def create_content_director(self, content_id: int, director_id: int):
        new_content_director = ContentDirectors(content_id=content_id, director_id=director_id)
        self.db.add(new_content_director)
        await self.db.commit()
        await self.db.refresh(new_content_director)
        return new_content_director

    async def update_content_director(self, content_director_id: int, content_id: int = None, director_id: int = None):
        content_director = await self.db.execute(
            select(ContentDirectors).filter(ContentDirectors.content_director_id == content_director_id)
        )
        content_director = content_director.scalar_one_or_none()

        if content_id:
            content_director.email = content_id
        if director_id:
            content_director.director_id = director_id

        await self.db.commit()
        await self.db.refresh(content_director)
        return content_director

    async def delete_content_director(self, content_director_id: int):
        await self.db.execute(
            delete(ContentDirectors).where(ContentDirectors.content_director_id == content_director_id)
        )
        await self.db.commit()