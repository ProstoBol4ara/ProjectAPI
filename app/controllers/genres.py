from fastapi import APIRouter, HTTPException, Depends
from repositories import GenresRepository
from database import AsyncSession, get_db
from services import GenresService

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)

@router.get('/')
async def get_genres(db: AsyncSession = Depends(get_db)):
    genres = await GenresService(GenresRepository(db)).get_genres()
    if genres is None:
        raise HTTPException(status_code=400, detail="Genres not found")
    return genres

@router.get('/{genre_id}')
async def get_genre(genre_id: int, db: AsyncSession = Depends(get_db)):
    genre = await GenresService(GenresRepository(db)).get_genre(genre_id=genre_id)
    if genre is None:
        raise HTTPException(status_code=400, detail="Genre not found")
    return genre

@router.post('/')
async def create_genre(genre_name: str, db: AsyncSession = Depends(get_db)):
    try:
        new_genre = await GenresService(GenresRepository(db)).create_genre(genre_name=genre_name)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_genre

@router.put('/{genre_id}')
async def update_genre(genre_id: int, genre_name: str = None, db: AsyncSession = Depends(get_db)):
    try:
        genre = await GenresService(GenresRepository(db)).update_genre(genre_id=genre_id, genre_name=genre_name)
        if genre is None:
            raise HTTPException(status_code=400, detail="Genre not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return genre

@router.delete('/{genre_id}')
async def delete_genre(genre_id: int, db: AsyncSession = Depends(get_db)):
    if not await GenresService(GenresRepository(db)).delete_genre(genre_id=genre_id):
        raise HTTPException(status_code=400, detail="Genre not found")
    return {"message": "Genre deleted successfully"}