from fastapi import APIRouter, HTTPException, Depends
from repositories import EpisodesRepository
from database import AsyncSession, get_db
from services import EpisodesService

router = APIRouter(
    prefix="/episodes",
    tags=["episodes"]
)

@router.get('/')
async def get_episodes(db: AsyncSession = Depends(get_db)):
    episodes = await EpisodesService(EpisodesRepository(db)).get_episodes()
    if episodes is None:
        raise HTTPException(status_code=400, detail="Episodes not found")
    return 

@router.get('/{episode_id}')
async def get_episode(episode_id: int, db: AsyncSession = Depends(get_db)):
    episode = await EpisodesService(EpisodesRepository(db)).get_episode(episode_id=episode_id)
    if episode is None:
        raise HTTPException(status_code=400, detail="Episode not found")
    return episode

@router.post('/')
async def create_episode(content_id: int, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None, db: AsyncSession = Depends(get_db)):
    try:
        new_episode = await EpisodesService(EpisodesRepository(db)).create_episode(content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_episode

@router.put('/{episode_id}')
async def update_episode(episode_id: int, content_id: int = None, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None, db: AsyncSession = Depends(get_db)):
    try:
        episode = await EpisodesService(EpisodesRepository(db)).update_episode(episode_id=episode_id, content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
        if episode is None:
            raise HTTPException(status_code=400, detail="Episode not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return episode

@router.delete('/{episode_id}')
async def delete_episode(episode_id: int, db: AsyncSession = Depends(get_db)):
    if not await EpisodesService(EpisodesRepository(db)).delete_episode(episode_id=episode_id):
        raise HTTPException(status_code=400, detail="Episode not found")
    return {"message": "User deleted successfully"}