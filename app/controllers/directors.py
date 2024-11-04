from repositories import DirectorsRepository
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import DirectorsService
from responses.directors import *

router = APIRouter(prefix="/directors", tags=["directors"])


@router.get("/", summary="Fetch all directors", responses=get_directors)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/directors
    """

    directors = await DirectorsService(DirectorsRepository(db)).get_all()
    return directors


@router.get("/{director_id}", summary="Fetch director by id", responses=get_director)
@handle_exceptions(status_code=400)
async def get_one(director_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/directors/1
    """

    director = await DirectorsService(DirectorsRepository(db)).get_one(
        director_id=director_id
    )
    return director


@router.post("/", summary="Create director", responses=create_director)
@handle_exceptions(status_code=400)
async def create(
    director_name: str,
    biography: str = None,
    birth_date: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        POST /api/directors/
        {
            "director_id": 1,
            "director_name": "aaa",
            "biography": "aaa",
            "birth_date": "2000-10-10"
        }
    """

    new_director = await DirectorsService(DirectorsRepository(db)).create(
        director_name=director_name, biography=biography, birth_date=birth_date
    )

    return new_director


@router.put(
    "/{director_id}", summary="Update director by id", responses=update_director
)
@handle_exceptions(status_code=400)
async def update(
    director_id: int,
    director_name: str = None,
    biography: str = None,
    birth_date: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/directors/1
        {
            "director_id": 1,
            "director_name": "bbb"
        }
    """

    director = await DirectorsService(DirectorsRepository(db)).update(
        director_id=director_id,
        director_name=director_name,
        biography=biography,
        birth_date=birth_date,
    )
    return director


@router.delete(
    "/{director_id}", summary="Delete director by id", responses=delete_director
)
@handle_exceptions(status_code=400)
async def delete(director_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/directors/1
    """

    await DirectorsService(DirectorsRepository(db)).delete(director_id=director_id)
    return {"message": "Director deleted successfully"}
