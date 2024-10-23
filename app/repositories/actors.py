from database import AsyncSession, select, delete
from datetime import datetime
from models import Actors

class ActorsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_actors(self):
        actors = await self.db.execute(select(Actors))
        return actors.scalars().all()

    async def get_actor(self, actor_id: int):
        actor = await self.db.execute(
            select(Actors).where(Actors.actor_id == actor_id)
        )
        return actor.scalar_one_or_none()

    async def create_actor(self, actor_name: str, biography: str = None, birth_date: str = None):
        if not birth_date is None:
            birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
        new_actor = Actors(actor_name=actor_name, biography=biography, birth_date=birth_date)
        self.db.add(new_actor)
        await self.db.commit()
        await self.db.refresh(new_actor)   
        return new_actor

    async def update_actor(self, actor_id: int, actor_name: str = None, biography: str = None, birth_date: str = None):
        actor = await self.db.execute(
            select(Actors).where(Actors.actor_id == actor_id)
        )
        actor = actor.scalar_one_or_none()

        if actor_name:
            actor.actor_name = actor_name
        if biography:
            actor.biography = biography
        if birth_date:
            actor.birth_date = birth_date
        
        await self.db.commit()
        await self.db.refresh(actor)
        return actor

    async def delete_actor(self, actor_id: int):
        result = await self.db.execute(
            delete(Actors).where(Actors.actor_id == actor_id)
        )
        await self.db.commit()
        return result.rowcount > 0
