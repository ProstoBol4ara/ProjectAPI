from fastapi import APIRouter, HTTPException, Depends
from repositories import GenresRepository
from database import AsyncSession, get_db
from services import GenresService
from responses.genres import *

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)

@router.get('/', summary="Fetch all genres", responses=get_genres)
async def get_genres(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/genres
    """

    genres = await GenresService(GenresRepository(db)).get_genres()
    if genres is None:
        raise HTTPException(status_code=400, detail="Genres not found")
    return genres

@router.get('/{genre_id}', summary="Fetch genre by id", responses=get_genre)
async def get_genre(genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/genres/1
    """

    genre = await GenresService(GenresRepository(db)).get_genre(genre_id=genre_id)
    if genre is None:
        raise HTTPException(status_code=400, detail="Genre not found")
    return genre

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

    try:
        new_genre = await GenresService(GenresRepository(db)).create_genre(genre_name=genre_name)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_genre

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

    try:
        genre = await GenresService(GenresRepository(db)).update_genre(genre_id=genre_id, genre_name=genre_name)
        if genre is None:
            raise HTTPException(status_code=400, detail="Genre not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return genre

@router.delete('/{genre_id}', summary="Delete genre by id", responses=delete_genre)
async def delete_genre(genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/genres/1
    """

    if not await GenresService(GenresRepository(db)).delete_genre(genre_id=genre_id):
        raise HTTPException(status_code=400, detail="Genre not found")
    return {"message": "Genre deleted successfully"}
