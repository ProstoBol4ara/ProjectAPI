from repositories import NotificationsRepository


class NotificationsService:
    def __init__(self, repository: NotificationsRepository):
        self.repository = repository

    async def get_all(self):
        notifications = await self.repository.get_all()

        return (
            None
            if notifications is None
            else [
                {
                    "notification_id": notification.notification_id,
                    "message": notification.message,
                    "user_id": notification.user_id,
                }
                for notification in notifications
            ]
        )

    async def get_one(self, notification_id: int):
        if not notification_id:
            raise ValueError("notification_id cannot be empty")

        notification = await self.repository.get_one(notification_id=notification_id)

        if not notification:
            raise ValueError("Notification not found")

        return {
            "notification_id": notification.notification_id,
            "message": notification.message,
            "user_id": notification.user_id,
        }

    async def create(self, message: str, user_id: int = None):
        if not message:
            raise ValueError("message cannot be empty")

        new_notification = await self.repository.create(
            message=message, user_id=user_id
        )

        return {
            "notification_id": new_notification.notification_id,
            "message": new_notification.message,
            "user_id": new_notification.user_id,
        }

    async def update(
        self, notification_id: int, message: str = None, user_id: int = None
    ):
        if not notification_id:
            raise ValueError("notification_id cannot be empty")

        notification = await self.repository.update(
            notification_id=notification_id, message=message, user_id=user_id
        )

        if not notification:
            raise ValueError("Notification not found")

        return {
            "notification_id": notification.notification_id,
            "message": notification.message,
            "user_id": notification.user_id,
        }

    async def delete(self, notification_id: int):
        if not notification_id:
            raise ValueError("notification_id cannot be empty")

        if not (
            delete_notification := await self.repository.delete(
                notification_id=notification_id
            )
        ):
            raise ValueError("Notification not found")
        return delete_notification
