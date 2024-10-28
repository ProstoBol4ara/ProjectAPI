from repositories import DirectorsRepository
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import DirectorsService
from responses.directors import *

router = APIRouter(
    prefix="/directors",
    tags=["directors"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all directors", responses=get_directors)
async def get_directors(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/directors
    """

    directors = await DirectorsService(DirectorsRepository(db)).get_directors()
    return directors

@handle_exceptions(status_code=400)
@router.get('/{director_id}', summary="Fetch director by id", responses=get_director)
async def get_director(director_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/directors/1
    """

    director = await DirectorsService(DirectorsRepository(db)).get_director(director_id=director_id)
    return director

@handle_exceptions(status_code=400)
@router.post('/', summary="Create director", responses=create_director)
async def create_director(director_name: str, biography: str = None, birth_date: str = None, db: AsyncSession = Depends(get_db)):
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

    new_director = await DirectorsService(DirectorsRepository(db)).create_director(director_name=director_name, biography=biography, birth_date=birth_date)
    return new_director

@handle_exceptions(status_code=400)
@router.put('/{director_id}', summary="Update director by id", responses=update_director)
async def update_director(director_id: int, director_name: str = None, biography:str = None, birth_date: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/directors/1
        {
            "director_id": 1,
            "director_name": "bbb"
        }
    """

    director = await DirectorsService(DirectorsRepository(db)).update_director(director_id=director_id, director_name=director_name, biography=biography, birth_date=birth_date)
    return director

@handle_exceptions(status_code=400)
@router.delete('/{director_id}', summary="Delete director by id", responses=delete_director)
async def delete_director(director_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/directors/1
    """

    await DirectorsService(DirectorsRepository(db)).delete_director(director_id=director_id)
    return {"message": "Director deleted successfully"}
