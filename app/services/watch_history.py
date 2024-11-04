from repositories import WatchHistoryRepository


class WatchHistoryService:
    def __init__(self, repository: WatchHistoryRepository):
        self.repository = repository

    async def get_all(self):
        watch_historys = await self.repository.get_all()

        return (
            None
            if watch_historys is None
            else [
                {
                    "watch_history_id": watch_history.watch_history_id,
                    "user_id": watch_history.user_id,
                    "content_id": watch_history.content_id,
                }
                for watch_history in watch_historys
            ]
        )

    async def get_one(self, watch_history_id: int):
        if not watch_history_id:
            raise ValueError("watch_history_id cannot be empty")

        watch_history = await self.repository.get_one(watch_history_id=watch_history_id)

        if not watch_history:
            raise ValueError("Watch history not found")

        return {
            "watch_history_id": watch_history.watch_history_id,
            "user_id": watch_history.user_id,
            "content_id": watch_history.content_id,
        }

    async def create(self, user_id: int, content_id: int):
        if not user_id or not content_id:
            raise ValueError("user_id and content_id cannot be empty")

        new_watch_history = await self.repository.create(
            user_id=user_id, content_id=content_id
        )

        return {
            "watch_history_id": new_watch_history.watch_history_id,
            "user_id": new_watch_history.user_id,
            "content_id": new_watch_history.content_id,
        }

    async def update(
        self, watch_history_id: int, user_id: int = None, content_id: int = None
    ):
        if not watch_history_id:
            raise ValueError("watch_history_id cannot be empty")

        watch_history = await self.repository.update(
            watch_history_id=watch_history_id, user_id=user_id, content_id=content_id
        )

        if not watch_history:
            raise ValueError("Watch history not found")

        return {
            "watch_history_id": watch_history.watch_history_id,
            "user_id": watch_history.user_id,
            "content_id": watch_history.content_id,
        }

    async def delete(self, watch_history_id: int):
        if not watch_history_id:
            raise ValueError("watch_history_id cannot be empty")

        if not (
            delete_watch_history := await self.repository.delete(
                watch_history_id=watch_history_id
            )
        ):
            raise ValueError("Watch history not found")
        return delete_watch_history
