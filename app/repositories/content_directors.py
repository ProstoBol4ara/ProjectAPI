from database import AsyncSession, select, delete
from models import ContentDirectors


class ContentDirectorsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        content_directors = await self.db.execute(select(ContentDirectors))
        return content_directors.scalars().all()

    async def get_one(self, content_director_id: int):
        content_director = await self.db.execute(
            select(ContentDirectors).filter(
                ContentDirectors.content_director_id == content_director_id
            )
        )
        return content_director.scalar_one_or_none()

    async def create(self, content_id: int, director_id: int):
        new_content_director = ContentDirectors(
            content_id=content_id, director_id=director_id
        )
        self.db.add(new_content_director)
        await self.db.commit()
        await self.db.refresh(new_content_director)
        return new_content_director

    async def update(
        self, content_director_id: int, content_id: int = None, director_id: int = None
    ):
        content_director = await self.db.execute(
            select(ContentDirectors).filter(
                ContentDirectors.content_director_id == content_director_id
            )
        )
        content_director = content_director.scalar_one_or_none()

        if content_id:
            content_director.email = content_id
        if director_id:
            content_director.director_id = director_id

        await self.db.commit()
        await self.db.refresh(content_director)
        return content_director

    async def delete(self, content_director_id: int):
        result = await self.db.execute(
            delete(ContentDirectors).where(
                ContentDirectors.content_director_id == content_director_id
            )
        )
        await self.db.commit()
        return result.rowcount > 0
