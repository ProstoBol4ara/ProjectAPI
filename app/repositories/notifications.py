from database import AsyncSession, select, delete
from models import Notifications


class NotificationsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        notifications = await self.db.execute(select(Notifications))
        return notifications.scalars().all()

    async def get_one(self, notification_id: int):
        notification = await self.db.execute(
            select(Notifications).where(
                Notifications.notification_id == notification_id
            )
        )
        return notification.scalar_one_or_none()

    async def create(self, message: str, user_id: int = None):
        new_notification = Notifications(message=message, user_id=user_id)
        self.db.add(new_notification)
        await self.db.commit()
        await self.db.refresh(new_notification)
        return new_notification

    async def update(self, notification_id: int, message: str, user_id: int = None):
        notification = await self.db.execute(
            select(Notifications).where(
                Notifications.notification_id == notification_id
            )
        )
        notification = notification.scalar_one_or_none()

        if message:
            notification.message = message
        if user_id:
            notification.user_id = user_id

        await self.db.commit()
        await self.db.refresh(notification)
        return notification

    async def delete(self, notification_id: int):
        result = await self.db.execute(
            delete(Notifications).where(
                Notifications.notification_id == notification_id
            )
        )
        await self.db.commit()
        return result.rowcount > 0
