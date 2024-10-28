from fastapi import APIRouter, Depends
from api_decorators import handle_exceptions
from repositories import GenresRepository
from database import AsyncSession, get_db
from services import GenresService
from responses.genres import *

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all genres", responses=get_genres)
async def get_genres(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/genres
    """

    genres = await GenresService(GenresRepository(db)).get_genres()
    return genres

@handle_exceptions(status_code=400)
@router.get('/{genre_id}', summary="Fetch genre by id", responses=get_genre)
async def get_genre(genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/genres/1
    """

    genre = await GenresService(GenresRepository(db)).get_genre(genre_id=genre_id)
    return genre

@handle_exceptions(status_code=400)
@router.post('/', summary="Create genre", responses=create_genre)
async def create_genre(genre_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/genres/
        {
            "genre_id": 1,
            "genre_name": "aaa"
        }
    """

    new_genre = await GenresService(GenresRepository(db)).create_genre(genre_name=genre_name)
    return new_genre

@handle_exceptions(status_code=400)
@router.put('/{genre_id}', summary="Update genre by id", responses=update_genre)
async def update_genre(genre_id: int, genre_name: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/genres/1
        {
            "genre_id": 1,
            "genre_name": "bbb"
        }
    """

    genre = await GenresService(GenresRepository(db)).update_genre(genre_id=genre_id, genre_name=genre_name)
    return genre

@handle_exceptions(status_code=400)
@router.delete('/{genre_id}', summary="Delete genre by id", responses=delete_genre)
async def delete_genre(genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/genres/1
    """

    await GenresService(GenresRepository(db)).delete_genre(genre_id=genre_id)
    return {"message": "Genre deleted successfully"}
