from fastapi import APIRouter, HTTPException, Depends
from repositories import EpisodesRepository
from database import AsyncSession, get_db
from services import EpisodesService
from responses.episodes import *

router = APIRouter(
    prefix="/episodes",
    tags=["episodes"]
)

@router.get('/', summary="Fetch all episodes", responses=get_episodes)
async def get_episodes(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/episodes
    """

    episodes = await EpisodesService(EpisodesRepository(db)).get_episodes()
    if episodes is None:
        raise HTTPException(status_code=400, detail="Episodes not found")
    return

@router.get('/{episode_id}', summary="Fetch episode by id", responses=get_episode)
async def get_episode(episode_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/episodes/1
    """

    episode = await EpisodesService(EpisodesRepository(db)).get_episode(episode_id=episode_id)
    if episode is None:
        raise HTTPException(status_code=400, detail="Episode not found")
    return episode

@router.post('/', summary="Create episode", responses=create_episode)
async def create_episode(content_id: int, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/episodes/
        {
            "episode_id": 1,
            "content_id": 1,
            "season_number": 1,
            "episode_number": 1,
            "title": "aaa",
            "release_date": "2000-10-10",
            "episode_path": "/ep1"
        }
    """

    try:
        new_episode = await EpisodesService(EpisodesRepository(db)).create_episode(content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_episode

@router.put('/{episode_id}', summary="Update episode by id", responses=update_episode)
async def update_episode(episode_id: int, content_id: int = None, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/episodes/1
        {
            "episode_id": 1,
            "content_id": 1,
            "title": "bbb"
        }
    """

    try:
        episode = await EpisodesService(EpisodesRepository(db)).update_episode(episode_id=episode_id, content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
        if episode is None:
            raise HTTPException(status_code=400, detail="Episode not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return episode

@router.delete('/{episode_id}', summary="Delete episode by id", responses=delete_episode)
async def delete_episode(episode_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/episodes/1
    """

    if not await EpisodesService(EpisodesRepository(db)).delete_episode(episode_id=episode_id):
        raise HTTPException(status_code=400, detail="Episode not found")
    return {"message": "User deleted successfully"}
