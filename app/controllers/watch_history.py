from repositories import WatchHistoryRepository
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from services import WatchHistoryService
from fastapi import APIRouter, Depends
from responses.watch_history import *

router = APIRouter(prefix="/watch_historys", tags=["watch_historys"])


@router.get("/", summary="Fetch all watch historys", responses=get_watch_history)
@handle_exceptions(status_code=400)
async def get_watch_historys(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/watch_historys
    """

    watch_historys = await WatchHistoryService(
        WatchHistoryRepository(db)
    ).get_watch_historys()
    return watch_historys


@router.get(
    "/{watch_history_id}",
    summary="Fetch watch history by id",
    responses=get_watch_history,
)
@handle_exceptions(status_code=400)
async def get_watch_history(watch_history_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/watch_historys/1
    """

    watch_history = await WatchHistoryService(
        WatchHistoryRepository(db)
    ).get_watch_history(watch_history_id=watch_history_id)
    return watch_history


@router.post("/", summary="Create watch history", responses=create_watch_history)
@handle_exceptions(status_code=400)
async def create_watch_history(
    user_id: int, content_id: int, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        POST /api/watch_historys/
        {
            "watch_history_id": 1,
            "user_id": 1,
            "content_id": 1
        }
    """

    new_watch_history = await WatchHistoryService(
        WatchHistoryRepository(db)
    ).create_watch_history(user_id=user_id, content_id=content_id)
    return new_watch_history


@router.put(
    "/{watch_history_id}",
    summary="Update watch history by id",
    responses=update_watch_history,
)
@handle_exceptions(status_code=400)
async def update_watch_history(
    watch_history_id: int,
    user_id: int = None,
    content_id: int = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/watch_historys/1
        {
            "watch_history_id": 1,
            "user_id": 1,
            "content_id": 2
        }
    """

    watch_history = await WatchHistoryService(
        WatchHistoryRepository(db)
    ).update_watch_history(
        watch_history_id=watch_history_id, user_id=user_id, content_id=content_id
    )
    return watch_history


@router.delete(
    "/{watch_history_id}",
    summary="Delete watch history by id",
    responses=delete_watch_history,
)
@handle_exceptions(status_code=400)
async def delete_watch_history(
    watch_history_id: int, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        DELETE /api/watch_historys/1
    """

    await WatchHistoryService(WatchHistoryRepository(db)).delete_watch_history(
        watch_history_id=watch_history_id
    )
    return {"message": "Watch history deleted successfully"}
