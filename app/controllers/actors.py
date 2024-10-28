from fastapi import APIRouter, HTTPException, Depends
from database import AsyncSession, get_db
from repositories import ActorsRepository
from services import ActorsService
from responses.actors import *

router = APIRouter(
    prefix="/actors",
    tags=["actors"]
)

@router.get('/', summary="Fetch all actors", responses=get_actors)
async def get_actors(db: AsyncSession = Depends(get_db)):
    actors = await ActorsService(ActorsRepository(db)).get_actors()
    if actors is None:
        raise HTTPException(status_code=400, detail="Actors not found")
    return actors

@router.get('/{actor_id}', summary="Fetch actor by id", responses=get_actor)
async def get_actor(actor_id: int, db: AsyncSession = Depends(get_db)):
    actor = await ActorsService(ActorsRepository(db)).get_actor(actor_id=actor_id)
    if actor is None:
        raise HTTPException(status_code=400, detail="Actor not found")
    return actor

@router.post('/', summary="Create actor", responses=create_actor)
async def create_actor(actor_name: str, biography: str = None, birth_date: str = None, db: AsyncSession = Depends(get_db)):
    try:
        new_actor = await ActorsService(ActorsRepository(db)).create_actor(actor_name=actor_name, biography=biography, birth_date=birth_date)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_actor

@router.put('/{actor_id}', summary="Update actor by id", responses=update_actor)
async def update_actor(actor_id: int, actor_name: str = None, biography: str = None, birth_date: str = None, db: AsyncSession = Depends(get_db)):
    try:
        actor = await ActorsService(ActorsRepository(db)).update_actor(actor_id=actor_id, actor_name=actor_name, biography=biography, birth_date=birth_date)
        if actor is None:
            raise HTTPException(status_code=400, detail="Actor not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return actor

@router.delete('/{actor_id}', summary="Delete actor by id", responses=delete_actor)
async def delete_actor(actor_id: int, db: AsyncSession = Depends(get_db)):
    if not await ActorsService(ActorsRepository(db)).delete_actor(actor_id=actor_id):
        raise HTTPException(status_code=400, detail="Actor not found")
    return {"message": "Actors deleted successfully"}
