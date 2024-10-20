from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Episodes

router = APIRouter(
    prefix="/episodes",
    tags=["episodes"]
)

@router.get('/', response_model=list[dict])
async def get_episodes(db: Session = Depends(get_db)):
    episodes = db.query(Episodes).all()
    if episodes is None:
        raise HTTPException(status_code=400, detail="Episodes not found")
    return [{"episode_id": episode.episode_id, "content_id": episode.content_id, "season_number": episode.season_number, "episode_number": episode.episode_number, "title": episode.title, "release_date": episode.release_date, "episode_path": episode.episode_path} for episode in episodes]

@router.get('/{episode_id}', response_model=dict)
async def get_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episodes).filter(Episodes.episode_id == episode_id).first()
    if episode is None:
        raise HTTPException(status_code=400, detail="User not found")
    return {"episode_id": episode.episode_id, "content_id": episode.content_id, "season_number": episode.season_number, "episode_number": episode.episode_number, "title": episode.title, "release_date": episode.release_date, "episode_path": episode.episode_path}

@router.post('/', response_model=dict)
async def create_episode(content_id: int, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None, db: Session = Depends(get_db)):
    try:
        if not release_date is None:
            release_date = datetime.strptime(release_date, '%d.%m.%Y').date()
        new_episode = Episodes(content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
        db.add(new_episode)
        db.commit()
        db.refresh(new_episode)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"episode_id": new_episode.episode_id, "content_id": new_episode.content_id, "season_number": new_episode.season_number, "episode_number": new_episode.episode_number, "title": new_episode.title, "release_date": new_episode.release_date, "episode_path": new_episode.episode_path}

@router.put('/{episode_id}', response_model=dict)
async def update_episode(episode_id: int, content_id: int = None, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None, db: Session = Depends(get_db)):
    try:
        episode = db.query(Episodes).filter(Episodes.episode_id == episode_id).first()
        if episode is None:
            raise HTTPException(status_code=400, detail="User not found")

        if title:
            episode.title = title
        if content_id:
            episode.content_id = content_id
        if release_date:
            episode.release_date = datetime.strptime(release_date, '%d.%m.%Y').date()
        if episode_path:
            episode.episode_path = episode_path
        if season_number:
            episode.season_number = season_number
        if episode_number:
            episode.episode_number = episode_number

        db.commit()
        db.refresh(episode)
    except:
        raise HTTPException(status_code=400, detail="Update failed")
    return {"episode_id": episode.episode_id, "content_id": episode.content_id, "season_number": episode.season_number, "episode_number": episode.episode_number, "title": episode.title, "release_date": episode.release_date, "episode_path": episode.episode_path}

@router.delete('/{episode_id}', response_model=dict)
async def delete_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episodes).filter(Episodes.episode_id == episode_id).first()
    if episode is None:
        raise HTTPException(status_code=400, detail="User not found")

    db.delete(episode)
    db.commit()
    return {"message": "User deleted successfully"}