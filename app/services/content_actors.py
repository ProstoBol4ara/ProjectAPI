from repositories import ContentActorsRepository

class ContentActorsService:
    def __init__(self, content_actors_repository: ContentActorsRepository):
        self.content_actors_repository = content_actors_repository

    async def get_content_actors(self):
        content_actors = await self.content_actors_repository.get_content_actors()

        return None if content_actors is None else \
            [{"content_actor_id": content_actor.content_actor_id, "content_id": content_actor.content_id,
              "actor_id": content_actor.actor_id, "role": content_actor.role} for content_actor in content_actors]

    async def get_content_actor(self, content_actor_id: int):
        content_actor = await self.content_actors_repository.get_content_actor(content_actor_id=content_actor_id)

        if not content_actor: raise ValueError("Content actor not found")

        return {"content_actor_id": content_actor.content_actor_id, "content_id": content_actor.content_id,
                 "actor_id": content_actor.actor_id, "role": content_actor.role}

    async def create_content_actors(self, content_id: int, actor_id: int, role: str = None):
        new_content_actor = await self.content_actors_repository \
            .create_content_actors(content_id=content_id, actor_id=actor_id, role=role)

        return {"content_actor_id": new_content_actor.content_actor_id, "actor_id": new_content_actor.actor_id,
                "role": new_content_actor.role}

    async def update_content_actors(self, content_actor_id: int, content_id: int = None, actor_id: int = None, role: str = None):
        content_actor = await self.content_actors_repository\
            .update_content_actors(content_actor_id=content_actor_id, content_id=content_id, actor_id=actor_id, role=role)

        if not content_actor: raise ValueError("Content actor not found")

        return {"content_actor_id": content_actor.content_actor_id, "actor_id": content_actor.actor_id,
                "role": content_actor.role}

    async def delete_content_actors(self, content_actor_id: int):
        if not await self.content_actors_repository.delete_content_actors(content_actor_id=content_actor_id):
            raise ValueError("Content actor not found")
