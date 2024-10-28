from repositories import NotificationsRepository
from api_decorators import handle_exceptions
from services import NotificationsService
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from responses.notifications import *

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all notifications", responses=get_notifications)
async def get_notifications(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/notifications
    """

    notifications = await NotificationsService(NotificationsRepository(db)).get_notifications()
    return notifications

@handle_exceptions(status_code=400)
@router.get('/{notification_id}', summary="Fetch notification by id", responses=get_notification)
async def get_notification(notification_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/notifications/1
    """

    notification = await NotificationsService(NotificationsRepository(db)).get_notification(notification_id=notification_id)
    return notification

@handle_exceptions(status_code=400)
@router.post('/', summary="Create notification", responses=create_notification)
async def create_notification(message: str, user_id: int = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/notifications/
        {
            "notification_id": 1,
            "message": "aaa",
            "user_id": 1
        }
    """

    new_notification = await NotificationsService(NotificationsRepository(db)).create_notification(message=message, user_id=user_id)
    return new_notification

@handle_exceptions(status_code=400)
@router.put('/{notification_id}', summary="Update notification by id", responses=update_notification)
async def update_notification(notification_id: int, message: str, user_id: int = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/notifications/1
        {
            "notification_id": 1,
            "message": "bbb"
        }
    """

    notification = await NotificationsService(NotificationsRepository(db)).update_notification(notification_id=notification_id, message=message, user_id=user_id)
    return notification

@handle_exceptions(status_code=400)
@router.delete('/{notification_id}', summary="Delete notification by id", responses=delete_notification)
async def delete_notification(notification_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/notifications/1
    """

    await NotificationsService(NotificationsRepository(db)).delete_notification(notification_id=notification_id)
    return {"message": "Notification deleted successfully"}
