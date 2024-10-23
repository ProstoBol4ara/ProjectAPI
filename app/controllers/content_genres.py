from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentGenresRepository
from services import ContentGenresService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/content_genres",
    tags=["content_genres"]
)

@router.get('/')
async def get_content_genres(db: AsyncSession = Depends(get_db)):
    content_genres = await ContentGenresService(ContentGenresRepository(db)).get_content_genres()
    if content_genres is None:
        raise HTTPException(status_code=400, detail="Content genres not found")
    return content_genres

@router.get('/{content_genre_id}')
async def get_content_genre(content_genre_id: int, db: AsyncSession = Depends(get_db)):
    content_genre = await ContentGenresService(ContentGenresRepository(db)).get_content_genre(content_genre_id=content_genre_id)
    if content_genre is None:
        raise HTTPException(status_code=400, detail="Content genre not found")
    return content_genre

@router.post('/')
async def create_content_genre(content_id: int, genres_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_content_genre = await ContentGenresService(ContentGenresRepository(db)).create_content_genre(content_id=content_id, genres_id=genres_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_genre

@router.put('/{content_genre_id}')
async def update_content_genre(content_genre_id: int, content_id: int = None, genres_id: int = None, db: AsyncSession = Depends(get_db)):
    try:
        content_genre = await ContentGenresService(ContentGenresRepository(db)).update_content_genre(content_genre_id=content_genre_id, content_id=content_id, genres_id=genres_id)
        if content_genre is None:
            raise HTTPException(status_code=400, detail="Content genre not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return content_genre

@router.delete('/{content_genre_id}')
async def delete_content_genre(content_genre_id: int, db: AsyncSession = Depends(get_db)):
    if not await ContentGenresService(ContentGenresRepository(db)).delete_content_genre(content_genre_id=content_genre_id):
        raise HTTPException(status_code=400, detail="Content genre not found")
    return {"message": "Content genre deleted successfully"}