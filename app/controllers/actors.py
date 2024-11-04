from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from repositories import ActorsRepository
from fastapi import APIRouter, Depends
from services import ActorsService
from responses.actors import *

router = APIRouter(prefix="/actors", tags=["actors"])


@router.get("/", summary="Fetch all actors", responses=get_actors)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/actors
    """

    actors = await ActorsService(ActorsRepository(db)).get_all()
    return actors


@router.get("/{actor_id}", summary="Fetch actor by id", responses=get_actor)
@handle_exceptions(status_code=400)
async def get_one(actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/actors/1
    """

    actor = await ActorsService(ActorsRepository(db)).get_one(actor_id=actor_id)
    return actor


@router.post("/", summary="Create actor", responses=create_actor)
@handle_exceptions(status_code=400)
async def create(
    actor_name: str,
    biography: str = None,
    birth_date: str = None,
    db: AsyncSession = Depends(get_db),
):
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

    new_actor = await ActorsService(ActorsRepository(db)).create(
        actor_name=actor_name, biography=biography, birth_date=birth_date
    )

    return new_actor


@router.put("/{actor_id}", summary="Update actor by id", responses=update_actor)
@handle_exceptions(status_code=400)
async def update(
    actor_id: int,
    actor_name: str = None,
    biography: str = None,
    birth_date: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/actors/1
        {
            "actor_id": 1,
            "actor_name": "bbb"
        }
    """

    actor = await ActorsService(ActorsRepository(db)).update(
        actor_id=actor_id,
        actor_name=actor_name,
        biography=biography,
        birth_date=birth_date,
    )

    return actor


@router.delete("/{actor_id}", summary="Delete actor by id", responses=delete_actor)
@handle_exceptions(status_code=400)
async def delete(actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/actors/1
    """

    await ActorsService(ActorsRepository(db)).delete(actor_id=actor_id)
    return {"message": "Actors deleted successfully"}
