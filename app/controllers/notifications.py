from fastapi import APIRouter, HTTPException, Depends
from repositories import NotificationsRepository
from services import NotificationsService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

@router.get('/')
async def get_notifications(db: AsyncSession = Depends(get_db)):
    notifications = await NotificationsService(NotificationsRepository(db)).get_notifications()
    if notifications is None:
        raise HTTPException(status_code=400, detail="Notification not found")
    return notifications

@router.get('/{notification_id}')
async def get_notification(notification_id: int, db: AsyncSession = Depends(get_db)):
    notification = await NotificationsService(NotificationsRepository(db)).get_notification(notification_id=notification_id)
    if notification is None:
        raise HTTPException(status_code=400, detail="Notification not found")
    return notification

@router.post('/')
async def create_notification(message: str, user_id: int = None, db: AsyncSession = Depends(get_db)):
    try:
        new_notification = await NotificationsService(NotificationsRepository(db)).create_notification(message=message, user_id=user_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_notification

@router.put('/{notification_id}')
async def update_notification(notification_id: int, message: str, user_id: int = None, db: AsyncSession = Depends(get_db)):
    try:
        notification = await NotificationsService(NotificationsRepository(db)).update_notification(notification_id=notification_id, message=message, user_id=user_id)
        if notification is None:
            raise HTTPException(status_code=400, detail="Notification not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return notification

@router.delete('/{notification_id}')
async def delete_notification(notification_id: int, db: AsyncSession = Depends(get_db)):
    if not await NotificationsService(NotificationsRepository(db)).delete_notification(notification_id=notification_id):
        raise HTTPException(status_code=400, detail="Notification not found")
    return {"message": "Notification deleted successfully"}