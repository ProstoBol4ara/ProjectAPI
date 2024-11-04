from repositories import NotificationsRepository
from api_decorators import handle_exceptions
from services import NotificationsService
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from responses.notifications import *

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("/", summary="Fetch all notifications", responses=get_notifications)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/notifications
    """

    notifications = await NotificationsService(NotificationsRepository(db)).get_all()
    return notifications


@router.get(
    "/{notification_id}", summary="Fetch notification by id", responses=get_notification
)
@handle_exceptions(status_code=400)
async def get_one(notification_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/notifications/1
    """

    notification = await NotificationsService(NotificationsRepository(db)).get_one(
        notification_id=notification_id
    )
    return notification


@router.post("/", summary="Create notification", responses=create_notification)
@handle_exceptions(status_code=400)
async def create(message: str, user_id: int = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/notifications/
        {
            "notification_id": 1,
            "message": "aaa",
            "user_id": 1
        }
    """

    new_notification = await NotificationsService(NotificationsRepository(db)).create(
        message=message, user_id=user_id
    )
    return new_notification


@router.put(
    "/{notification_id}",
    summary="Update notification by id",
    responses=update_notification,
)
@handle_exceptions(status_code=400)
async def update(
    notification_id: int,
    message: str,
    user_id: int = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/notifications/1
        {
            "notification_id": 1,
            "message": "bbb"
        }
    """

    notification = await NotificationsService(NotificationsRepository(db)).update(
        notification_id=notification_id, message=message, user_id=user_id
    )

    return notification


@router.delete(
    "/{notification_id}",
    summary="Delete notification by id",
    responses=delete_notification,
)
@handle_exceptions(status_code=400)
async def delete(notification_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/notifications/1
    """

    await NotificationsService(NotificationsRepository(db)).delete(
        notification_id=notification_id
    )
    return {"message": "Notification deleted successfully"}
