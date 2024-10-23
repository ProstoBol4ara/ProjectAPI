from fastapi import APIRouter, HTTPException, Depends
from repositories import WatchHistoryRepository
from database import AsyncSession, get_db
from services import WatchHistoryService

router = APIRouter(
    prefix="/watch_historys",
    tags=["watch_historys"]
)

@router.get('/')
async def get_watch_historys(db: AsyncSession = Depends(get_db)):
    watch_historys = await WatchHistoryService(WatchHistoryRepository(db)).get_watch_historys()
    if watch_historys is None:
        raise HTTPException(status_code=400, detail="Watch historys not found")
    return watch_historys

@router.get('/{watch_history_id}')
async def get_watch_history(watch_history_id: int, db: AsyncSession = Depends(get_db)):
    watch_history = await WatchHistoryService(WatchHistoryRepository(db)).get_watch_history(watch_history_id=watch_history_id)
    if watch_history is None:
        raise HTTPException(status_code=400, detail="Watch history not found")
    return watch_history

@router.post('/')
async def create_watch_history(user_id: int, content_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_watch_history = await WatchHistoryService(WatchHistoryRepository(db)).create_watch_history(user_id=user_id, content_id=content_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_watch_history

@router.put('/{watch_history_id}')
async def update_watch_history(watch_history_id: int, user_id: int = None, content_id: int = None, db: AsyncSession = Depends(get_db)):
    try:
        watch_history = await WatchHistoryService(WatchHistoryRepository(db)).update_watch_history(watch_history_id=watch_history_id, user_id=user_id, content_id=content_id)
        if watch_history is None:
            raise HTTPException(status_code=400, detail="Watch history not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return watch_history

@router.delete('/{watch_history_id}')
async def delete_watch_history(watch_history_id: int, db: AsyncSession = Depends(get_db)):
    if not await WatchHistoryService(WatchHistoryRepository(db)).delete_watch_history(watch_history_id=watch_history_id):
        raise HTTPException(status_code=400, detail="Watch history not found")
    return {"message": "Watch history deleted successfully"}