from repositories import WatchHistoryRepository

class WatchHistoryService:
    def __init__(self, watch_historys_repository: WatchHistoryRepository):
        self.watch_historys_repository = watch_historys_repository

    async def get_watch_historys(self):
        watch_historys = await self.watch_historys_repository.get_watch_historys()

        return None if watch_historys is None else \
            [{"watch_history_id": watch_history.watch_history_id, "user_id": watch_history.user_id,
              "content_id": watch_history.content_id} for watch_history in watch_historys]

    async def get_watch_history(self, watch_history_id: int):
        watch_history = await self.watch_historys_repository.get_watch_history(watch_history_id=watch_history_id)

        if not watch_history: raise ValueError("Watch history not found")

        return {"watch_history_id": watch_history.watch_history_id, "user_id": watch_history.user_id,
                "content_id": watch_history.content_id}

    async def create_watch_history(self, user_id: int, content_id: int):
        new_watch_history = await self.watch_historys_repository.create_watch_history(user_id=user_id, content_id=content_id)

        return {"watch_history_id": new_watch_history.watch_history_id, "user_id": new_watch_history.user_id,
                "content_id": new_watch_history.content_id}

    async def update_watch_history(self, watch_history_id: int, user_id: int = None, content_id: int = None):
        watch_history = await self.watch_historys_repository\
            .update_watch_history(watch_history_id=watch_history_id, user_id=user_id, content_id=content_id)

        if not watch_history: raise ValueError("Watch history not found")

        return {"watch_history_id": watch_history.watch_history_id, "user_id": watch_history.user_id,
                "content_id": watch_history.content_id}

    async def delete_watch_history(self, watch_history_id: int):
        return await self.watch_historys_repository.delete_watch_history(watch_history_id=watch_history_id)
