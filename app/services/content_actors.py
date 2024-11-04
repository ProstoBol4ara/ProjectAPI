from repositories import ContentActorsRepository


class ContentActorsService:
    def __init__(self, repository: ContentActorsRepository):
        self.repository = repository

    async def get_all(self):
        content_actors = await self.repository.get_all()

        return (
            None
            if content_actors is None
            else [
                {
                    "content_actor_id": content_actor.content_actor_id,
                    "content_id": content_actor.content_id,
                    "actor_id": content_actor.actor_id,
                    "role": content_actor.role,
                }
                for content_actor in content_actors
            ]
        )

    async def get_one(self, content_actor_id: int):
        if not content_actor_id:
            raise ValueError("content_actor_id cannot be empty")

        content_actor = await self.repository.get_one(content_actor_id=content_actor_id)

        if not content_actor:
            raise ValueError("Content actor not found")

        return {
            "content_actor_id": content_actor.content_actor_id,
            "content_id": content_actor.content_id,
            "actor_id": content_actor.actor_id,
            "role": content_actor.role,
        }

    async def create(self, content_id: int, actor_id: int, role: str = None):
        if not content_id or not actor_id:
            raise ValueError("Content id and actor id cannot be empty")

        new_content_actor = await self.repository.create(
            content_id=content_id, actor_id=actor_id, role=role
        )

        return {
            "content_actor_id": new_content_actor.content_actor_id,
            "content_id": new_content_actor.content_id,
            "actor_id": new_content_actor.actor_id,
            "role": new_content_actor.role,
        }

    async def update(
        self,
        content_actor_id: int,
        content_id: int = None,
        actor_id: int = None,
        role: str = None,
    ):
        if not content_actor_id:
            raise ValueError("content_actor_id cannot be empty")

        if not content_actor_id:
            raise ValueError("content_actor_id cannot be empty")

        content_actor = await self.repository.update(
            content_actor_id=content_actor_id,
            content_id=content_id,
            actor_id=actor_id,
            role=role,
        )

        if not content_actor:
            raise ValueError("Content actor not found")

        return {
            "content_actor_id": content_actor.content_actor_id,
            "content_id": content_actor.content_id,
            "actor_id": content_actor.actor_id,
            "role": content_actor.role,
        }

    async def delete(self, content_actor_id: int):
        if not content_actor_id:
            raise ValueError("content_actor_id cannot be empty")

        if not (
            delete_content_actors := await self.repository.delete(
                content_actor_id=content_actor_id
            )
        ):
            raise ValueError("Content actor not found")
        return delete_content_actors
