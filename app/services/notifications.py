from repositories import NotificationsRepository

class NotificationsService:
    def __init__(self, notifications_repository: NotificationsRepository):
        self.notifications_repository = notifications_repository
    
    async def get_notifications(self):
        return await self.notifications_repository.get_notifications()

    async def get_notification(self, notification_id: int):
        return await self.notifications_repository.get_notification(notification_id=notification_id)

    async def create_notification(self, message: str, user_id: int = None):
        return await self.notifications_repository.create_notification(message=message, user_id=user_id)

    async def update_notification(self, notification_id: int, message: str, user_id: int = None):
        return await self.notifications_repository.update_notification(notification_id=notification_id, message=message, user_id=user_id)

    async def delete_notification(self, notification_id: int):
        await self.notifications_repository.delete_notification(notification_id=notification_id)

    