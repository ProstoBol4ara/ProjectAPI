from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import WatchHistory

router = APIRouter(
    prefix="/watch_historys",
    tags=["watch_historys"]
)

@router.get('/', response_model=list[dict])
async def get_users(db: Session = Depends(get_db)):
    watch_historys = db.query(WatchHistory).all()
    if watch_historys is None:
        raise HTTPException(status_code=400, detail="Watch historys not found")
    return [{"watch_history_id": watch_history.watch_history_id, "user_id": watch_history.user_id, "content_id": watch_history.content_id} for watch_history in watch_historys]

@router.get('/{watch_history_id}', response_model=dict)
async def get_user(watch_history_id: int, db: Session = Depends(get_db)):
    watch_history = db.query(WatchHistory).filter(WatchHistory.watch_history_id == watch_history_id).first()
    if watch_history is None:
        raise HTTPException(status_code=400, detail="Watch history not found")
    return {"watch_history_id": watch_history.watch_history_id, "user_id": watch_history.user_id, "content_id": watch_history.content_id}

@router.post('/', response_model=dict)
async def create_user(user_id: int, content_id: int, db: Session = Depends(get_db)):
    try:
        new_watch_history = WatchHistory(user_id=user_id, content_id=content_id)
        db.add(new_watch_history)
        db.commit()
        db.refresh(new_watch_history)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"watch_history_id": new_watch_history.watch_history_id, "user_id": new_watch_history.user_id, "content_id": new_watch_history.content_id}

@router.put('/{watch_history_id}', response_model=dict)
async def update_user(watch_history_id: int, user_id: int = None, content_id: int = None, db: Session = Depends(get_db)):
    watch_history = db.query(WatchHistory).filter(WatchHistory.watch_history_id == watch_history_id).first()
    if watch_history is None:
        raise HTTPException(status_code=400, detail="Watch history not found")

    if user_id:
        watch_history.user_id = user_id
    if content_id:
        watch_history.content_id = content_id

    db.commit()
    db.refresh(watch_history)
    return {"watch_history_id": watch_history.watch_history_id, "user_id": watch_history.user_id, "content_id": watch_history.content_id}

@router.delete('/{watch_history_id}', response_model=dict)
async def delete_user(watch_history_id: int, db: Session = Depends(get_db)):
    watch_history = db.query(WatchHistory).filter(WatchHistory.watch_history_id == watch_history_id).first()
    if watch_history is None:
        raise HTTPException(status_code=400, detail="Watch history not found")

    db.delete(watch_history)
    db.commit()
    return {"message": "Watch history deleted successfully"}