from database import AsyncSession, select, delete
from models import Directors

class DirectorsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_directors(self):
        directors = await self.db.execute(select(Directors))
        return directors.scalars().all()

    async def get_director(self, director_id: int):
        director = await self.db.execute(
            select(Directors).where(Directors.director_id == director_id)
        )
        return director.scalar_one_or_none()

    async def create_director(self, director_name: str, biography: str = None, birth_date: str = None):
        if not birth_date is None:
            birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
        new_director = Directors(director_name=director_name, biography=biography, birth_date=birth_date)
        self.db.add(new_director)
        await self.db.commit()
        await self.db.refresh(new_director)
        return new_director

    async def update_director(self, director_id: int, director_name: str = None, biography:str = None, birth_date: str = None):
        director = await self.db.execute(
            select(Directors).where(Directors.director_id == director_id)
        )
        director = director.scalar_one_or_none()

        if director_name:
            director.director_name = director_name
        if biography:
            director.biography = biography
        if birth_date:
            director.birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()

        await self.db.commit()
        await self.db.refresh(director) 
        return director

    async def delete_director(self, director_id: int):
        result = await self.db.execute(
            delete(Directors).where(Directors.director_id == director_id)
        )
        await self.db.commit()
        return result.rowcount > 0
