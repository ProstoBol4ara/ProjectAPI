from database import AsyncSession
from models import ContentActors

class ContentActorsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_content_actors(self):
        content_actors = await self.db.execute(select(ContentActors))
        return content_actors.scalar().all()

    async def get_content_actors(self, content_actor_id: int):
        content_actor = await self.db.execute(
            select(ContentActors).where(ContentActors.content_actor_id == content_actor_id)
        )
        return content_actor.scalar_one_or_none()

    async def create_content_actors(self, content_id: int, actor_id: int, role: str = None):
        new_content_actor = ContentActors(content_id=content_id, actor_id=actor_id, role=role)
        self.db.add(new_content_actor)
        await self.db.commit()
        await self.db.refresh(new_content_actor)
        return new_content_actor

    async def update_content_actors(self, content_actor_id: int, content_id: int = None, actor_id: int = None, role: str = None):
        content_actor = await self.db.execute(
            select(ContentActors).where(ContentActors.content_actor_id == content_actor_id)
        )
        content_actor = content_actor.scalar_one_or_none()

        if content_id:
            content_actor.content_id = content_id
        if actor_id:
            content_actor.actor_id = actor_id
        if role:
            content_actor.role = role

        await self.db.commit()
        await self.db.refresh(content_actor)
        return content_actor

    async def delete_content_actors(self, content_actor_id: int):
        await self.db.execute(
            delete(ContentActors).where(ContentActors.content_actor_id == content_actor_id)
        )
        await self.db.commit()