from api_decorators import handle_exceptions
from repositories import GenresRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import GenresService
from responses.genres import *

router = APIRouter(prefix="/genres", tags=["genres"])


@router.get("/", summary="Fetch all genres", responses=get_genres)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/genres
    """

    genres = await GenresService(GenresRepository(db)).get_all()
    return genres


@router.get("/{genre_id}", summary="Fetch genre by id", responses=get_genre)
@handle_exceptions(status_code=400)
async def get_one(genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/genres/1
    """

    genre = await GenresService(GenresRepository(db)).get_one(genre_id=genre_id)
    return genre


@router.post("/", summary="Create genre", responses=create_genre)
@handle_exceptions(status_code=400)
async def create(genre_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/genres/
        {
            "genre_id": 1,
            "genre_name": "aaa"
        }
    """

    new_genre = await GenresService(GenresRepository(db)).create(genre_name=genre_name)
    return new_genre


@router.put("/{genre_id}", summary="Update genre by id", responses=update_genre)
@handle_exceptions(status_code=400)
async def update(
    genre_id: int, genre_name: str = None, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        PUT /api/genres/1
        {
            "genre_id": 1,
            "genre_name": "bbb"
        }
    """

    genre = await GenresService(GenresRepository(db)).update(
        genre_id=genre_id, genre_name=genre_name
    )
    return genre


@router.delete("/{genre_id}", summary="Delete genre by id", responses=delete_genre)
@handle_exceptions(status_code=400)
async def delete(genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/genres/1
    """

    await GenresService(GenresRepository(db)).delete(genre_id=genre_id)
    return {"message": "Genre deleted successfully"}
