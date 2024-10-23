from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentDirectorsRepository
from services import ContentDirectorsService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/content_directors",
    tags=["content_directors"]
)

@router.get('/')
async def get_content_directors(db: AsyncSession = Depends(get_db)):
    content_directors = await ContentDirectorsService(ContentDirectorsRepository(db)).get_content_directors()
    if content_directors is None:
        raise HTTPException(status_code=400, detail="Content directors not found")
    return content_directors

@router.get('/{content_director_id}')
async def get_content_director(content_director_id: int, db: AsyncSession = Depends(get_db)):
    content_director = await ContentDirectorsService(ContentDirectorsRepository(db)).get_content_director(content_director_id=content_director_id)
    if content_director is None:
        raise HTTPException(status_code=400, detail="Content director not found")
    return content_director

@router.post('/')
async def create_content_director(content_id: int, director_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_content_director = await ContentDirectorsService(ContentDirectorsRepository(db)).create_content_director(content_id=content_id, director_id=director_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_director

@router.put('/{content_director_id}')
async def update_content_director(content_director_id: int, content_id: int = None, director_id: int = None, db: AsyncSession = Depends(get_db)):
    try:
        content_director = await ContentDirectorsService(ContentDirectorsRepository(db)).update_content_director(content_director_id=content_director_id, content_id=content_id, director_id=director_id)
        if content_director is None:
            raise HTTPException(status_code=400, detail="Content director not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return content_director

@router.delete('/{content_director_id}')
async def delete_content_director(content_director_id: int, db: AsyncSession = Depends(get_db)):
    if not await ContentDirectorsService(ContentDirectorsRepository(db)).delete_content_director(content_director_id=content_director_id):
        raise HTTPException(status_code=400, detail="Content director not found")
    return {"message": "Content director deleted successfully"}