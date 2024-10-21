from database import AsyncSession
from models import WatchHistory

class WatchHistoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_users(self):
        watch_historys = await self.db.execute(select(WatchHistory))
        return watch_historys.scalar().all()

    async def get_user(self, watch_history_id: int):
        watch_history = await self.db.execute(
            select(WatchHistory).where(WatchHistory.watch_history_id == watch_history_id)
        )
        return watch_history.scalar_one_or_none()

    async def create_user(self, user_id: int, content_id: int):
        new_watch_history = WatchHistory(user_id=user_id, content_id=content_id)
        self.db.add(new_watch_history)
        await self.db.commit()
        await self.db.refresh(new_watch_history)
        return new_watch_history

    async def update_user(self, watch_history_id: int, user_id: int = None, content_id: int = None):
        watch_history = await self.db.execute(
            select(WatchHistory).where(WatchHistory.watch_history_id == watch_history_id)
        )
        watch_history = watch_history.scalar_one_or_none()

        if user_id:
            watch_history.user_id = user_id
        if content_id:
            watch_history.content_id = content_id

        await self.db.commit()
        await self.db.refresh(watch_history)
        return watch_history

    async def delete_user(self, watch_history_id: int):
        await self.db.execute(
            delete(WatchHistory).where(WatchHistory.watch_history_id == watch_history_id)
        )
        await self.db.commit()
