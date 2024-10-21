from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Notifications

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

@router.get('/')
async def get_notifications(db: Session = Depends(get_db)):
    notifications = db.query(Notifications).all()
    if notifications is None:
        raise HTTPException(status_code=400, detail="Notifications not found")
    return [{"notification_id": notification.notification_id, "message": notification.message, "user_id": notification.user_id} for notification in notifications]

@router.get('/{notification_id}')
async def get_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(Notifications).filter(Notifications.notification_id == notification_id).first()
    if notification is None:
        raise HTTPException(status_code=400, detail="Notification not found")
    return {"notification_id": notification.notification_id, "message": notification.message, "user_id": notification.user_id}

@router.post('/')
async def create_notification(message: str, user_id: int = None, db: Session = Depends(get_db)):
    try:
        new_notification = Notifications(message=message, user_id=user_id)
        db.add(new_notification)
        db.commit()
        db.refresh(new_notification)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"notification_id": new_notification.notification_id, "message": new_notification.message, "user_id": new_notification.user_id}

@router.put('/{notification_id}')
async def update_notification(notification_id: int, message: str, user_id: int = None, db: Session = Depends(get_db)):
    notification = db.query(Notifications).filter(Notifications.notification_id == notification_id).first()
    if notification is None:
        raise HTTPException(status_code=400, detail="Notification not found")

    if message:
        notification.message = message
    if user_id:
        notification.user_id = user_id

    db.commit()
    db.refresh(notification)
    return {"notification_id": notification.notification_id, "message": notification.message, "user_id": notification.user_id}

@router.delete('/{notification_id}')
async def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(Notifications).filter(Notifications.notification_id == notification_id).first()
    if notification is None:
        raise HTTPException(status_code=400, detail="Notification not found")

    db.delete(notification)
    db.commit()
    return {"message": "Notification deleted successfully"}