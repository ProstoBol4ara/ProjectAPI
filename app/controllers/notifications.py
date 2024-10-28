from fastapi import APIRouter, HTTPException, Depends
from repositories import NotificationsRepository
from services import NotificationsService
from database import AsyncSession, get_db
from responses.notifications import *

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

@router.get('/', summary="Fetch all notifications", responses=get_notifications)
async def get_notifications(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/notifications
    """

    notifications = await NotificationsService(NotificationsRepository(db)).get_notifications()
    if notifications is None:
        raise HTTPException(status_code=400, detail="Notification not found")
    return notifications

@router.get('/{notification_id}', summary="Fetch notification by id", responses=get_notification)
async def get_notification(notification_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/notifications/1
    """

    notification = await NotificationsService(NotificationsRepository(db)).get_notification(notification_id=notification_id)
    if notification is None:
        raise HTTPException(status_code=400, detail="Notification not found")
    return notification

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

    try:
        new_notification = await NotificationsService(NotificationsRepository(db)).create_notification(message=message, user_id=user_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_notification

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

    try:
        notification = await NotificationsService(NotificationsRepository(db)).update_notification(notification_id=notification_id, message=message, user_id=user_id)
        if notification is None:
            raise HTTPException(status_code=400, detail="Notification not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return notification

@router.delete('/{notification_id}', summary="Delete notification by id", responses=delete_notification)
async def delete_notification(notification_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/notifications/1
    """

    if not await NotificationsService(NotificationsRepository(db)).delete_notification(notification_id=notification_id):
        raise HTTPException(status_code=400, detail="Notification not found")
    return {"message": "Notification deleted successfully"}
