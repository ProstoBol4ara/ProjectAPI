from repositories import WatchHistoryRepository

class WatchHistoryService:
    def __init__(self, watch_historys_repository: WatchHistoryRepository):
        self.watch_historys_repository = watch_historys_repository

    async def get_watch_historys(self):
        return await self.watch_historys_repository.get_watch_historys()

    async def get_watch_history(self, watch_history_id: int):
        return await self.watch_historys_repository.get_watch_history(watch_history_id=watch_history_id)

    async def create_watch_history(self, user_id: int, content_id: int):
        return await self.watch_historys_repository.create_watch_history(user_id=user_id, content_id=content_id)

    async def update_watch_history(self, watch_history_id: int, user_id: int = None, content_id: int = None):
        return await self.watch_historys_repository.update_watch_history(watch_history_id=watch_history_id, user_id=user_id, content_id=content_id)

    async def delete_watch_history(self, watch_history_id: int):
        await self.watch_historys_repository.delete_watch_history(watch_history_id=watch_history_id)