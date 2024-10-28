from repositories import ActorsRepository

class ActorsService:
    def __init__(self, actors_repository: ActorsRepository):
        self.actors_repository = actors_repository

    async def get_actors(self):
        actors = await self.actors_repository.get_actors()
        return None if actors is None else [{"actor_id": actor.actor_id, "actor_name": actor.actor_name, "biography": actor.biography, "birth_date": actor.birth_date} for actor in actors]

    async def get_actor(self, actor_id: int):
        actor = await self.actors_repository.get_actor(actor_id=actor_id)

        if not actor: raise ValueError("Actor not found")

        return {"actor_id": actor.actor_id, "actor_name": actor.actor_name, "biography": actor.biography, "birth_date": actor.birth_date}

    async def create_actor(self, actor_name: str, biography: str = None, birth_date: str = None):
        new_actor = await self.actors_repository.create_actor(actor_name=actor_name, biography=biography, birth_date=birth_date)
        return {"actor_id": new_actor.actor_id, "name": new_actor.actor_name}

    async def update_actor(self, actor_id: int, actor_name: str = None, biography: str = None, birth_date: str = None):
        actor = await self.actors_repository.update_actor(actor_id=actor_id, actor_name=actor_name, biography=biography, birth_date=birth_date)

        if not actor: raise ValueError("Actor not found")

        return {"actor_id": actor.actor_id, "actor_name": actor.actor_name, "biography": actor.biography, "birth_date": actor.birth_date}

    async def delete_actor(self, actor_id: int):
        if not await self.actors_repository.delete_actor(actor_id=actor_id): raise ValueError("Actor not found")
