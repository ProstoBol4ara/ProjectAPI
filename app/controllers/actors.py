from database import AsyncSession, get_db
from repositories import ActorsRepository
from api_decorators import handle_exceptions
from fastapi import APIRouter, Depends
from services import ActorsService
from responses.actors import *

router = APIRouter(
    prefix="/actors",
    tags=["actors"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all actors", responses=get_actors)
async def get_actors(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/actors
    """

    actors = await ActorsService(ActorsRepository(db)).get_actors()
    return actors

@handle_exceptions(status_code=400)
@router.get('/{actor_id}', summary="Fetch actor by id", responses=get_actor)
async def get_actor(actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/actors/1
    """

    actor = await ActorsService(ActorsRepository(db)).get_actor(actor_id=actor_id)
    return actor

@handle_exceptions(status_code=400)
@router.post('/', summary="Create actor", responses=create_actor)
async def create_actor(actor_name: str, biography: str = None, birth_date: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/actors/
        {
            "actor_id": 1,
            "actor_name": "aaa",
            "biography": "aaa",
            "birth_date": "2002-10-10"
        }
    """

    new_actor = await ActorsService(ActorsRepository(db)).create_actor(actor_name=actor_name, biography=biography, birth_date=birth_date)
    return new_actor

@handle_exceptions(status_code=400)
@router.put('/{actor_id}', summary="Update actor by id", responses=update_actor)
async def update_actor(actor_id: int, actor_name: str = None, biography: str = None, birth_date: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/actors/1
        {
            "actor_id": 1,
            "actor_name": "bbb"
        }
    """

    actor = await ActorsService(ActorsRepository(db)).update_actor(actor_id=actor_id, actor_name=actor_name, biography=biography, birth_date=birth_date)
    return actor

@handle_exceptions(status_code=400)
@router.delete('/{actor_id}', summary="Delete actor by id", responses=delete_actor)
async def delete_actor(actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/actors/1
    """

    await ActorsService(ActorsRepository(db)).delete_actor(actor_id=actor_id)
    return {"message": "Actors deleted successfully"}
