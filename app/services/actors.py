from repositories import ActorsRepository
from constants import date_pattern
from re import match


class ActorsService:
    def __init__(self, repository: ActorsRepository):
        self.repository = repository

    async def get_all(self):
        actors = await self.repository.get_all()

        return (
            None
            if actors is None
            else [
                {
                    "actor_id": actor.actor_id,
                    "actor_name": actor.actor_name,
                    "biography": actor.biography,
                    "birth_date": actor.birth_date,
                }
                for actor in actors
            ]
        )

    async def get_one(self, actor_id: int):
        if not actor_id:
            raise ValueError("actor_id cannot be empty")

        actor = await self.repository.get_one(actor_id=actor_id)

        if not actor:
            raise ValueError("Actor not found")

        return {
            "actor_id": actor.actor_id,
            "actor_name": actor.actor_name,
            "biography": actor.biography,
            "birth_date": actor.birth_date,
        }

    async def create(
        self, actor_name: str, biography: str = None, birth_date: str = None
    ):
        if not birth_date or not match(date_pattern, birth_date):
            raise ValueError("Invalid birth_date! Date format: day.month.year")

        if not actor_name:
            raise ValueError("Actor name cannot be empty")

        new_actor = await self.repository.create(
            actor_name=actor_name, biography=biography, birth_date=birth_date
        )

        return {
            "actor_id": new_actor.actor_id,
            "actor_name": new_actor.actor_name,
            "biography": new_actor.biography,
            "birth_date": new_actor.birth_date,
        }

    async def update(
        self,
        actor_id: int,
        actor_name: str = None,
        biography: str = None,
        birth_date: str = None,
    ):
        if not actor_id:
            raise ValueError("actor_id cannot be empty")

        if not birth_date or not match(date_pattern, birth_date):
            raise ValueError("Invalid birth_date! Date format: day.month.year")

        actor = await self.repository.update(
            actor_id=actor_id,
            actor_name=actor_name,
            biography=biography,
            birth_date=birth_date,
        )

        if not actor:
            raise ValueError("Actor not found")

        return {
            "actor_id": actor.actor_id,
            "actor_name": actor.actor_name,
            "biography": actor.biography,
            "birth_date": actor.birth_date,
        }

    async def delete(self, actor_id: int):
        if not actor_id:
            raise ValueError("actor_id cannot be empty")

        if not (delete_actor := await self.repository.delete(actor_id=actor_id)):
            raise ValueError("Actor not found")
        return delete_actor
