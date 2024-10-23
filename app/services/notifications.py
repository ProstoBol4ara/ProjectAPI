from repositories import NotificationsRepository

class NotificationsService:
    def __init__(self, notifications_repository: NotificationsRepository):
        self.notifications_repository = notifications_repository
    
    async def get_notifications(self):
        notifications = await self.notifications_repository.get_notifications()
        return None if notifications is None else [{"notification_id": notification.notification_id, "message": notification.message, "user_id": notification.user_id} for notification in notifications]

    async def get_notification(self, notification_id: int):
        notification = await self.notifications_repository.get_notification(notification_id=notification_id)
        return None if notification is None else {"notification_id": notification.notification_id, "message": notification.message, "user_id": notification.user_id}

    async def create_notification(self, message: str, user_id: int = None):
        new_notification = await self.notifications_repository.create_notification(message=message, user_id=user_id)
        return {"notification_id": new_notification.notification_id, "message": new_notification.message, "user_id": new_notification.user_id}

    async def update_notification(self, notification_id: int, message: str, user_id: int = None):
        notification = await self.notifications_repository.update_notification(notification_id=notification_id, message=message, user_id=user_id)
        return None if notification is None else {"notification_id": notification.notification_id, "message": notification.message, "user_id": notification.user_id}

    async def delete_notification(self, notification_id: int):
        return await self.notifications_repository.delete_notification(notification_id=notification_id)

    