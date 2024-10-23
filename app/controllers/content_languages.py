from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentLanguagesRepository
from services import ContentLanguagesService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/content_languages",
    tags=["content_languages"]
)

@router.get('/')
async def get_content_languages(db: AsyncSession = Depends(get_db)):
    content_languages = await ContentLanguagesService(ContentLanguagesRepository(db)).get_content_languages()
    if content_languages is None:
        raise HTTPException(status_code=400, detail="Content languages not found")
    return content_languages

@router.get('/{content_language_id}')
async def get_content_language(content_language_id: int, db: AsyncSession = Depends(get_db)):
    content_language = await ContentLanguagesService(ContentLanguagesRepository(db)).get_content_language(content_language_id=content_language_id)
    if content_language is None:
        raise HTTPException(status_code=400, detail="Content language not found")
    return content_language

@router.post('/')
async def create_content_language(content_id: int, language_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_content_language = await ContentLanguagesService(ContentLanguagesRepository(db)).create_content_language(content_id=content_id, language_id=language_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_language

@router.put('/{content_language_id}')
async def update_content_language(content_language_id: int, content_id: int = None, language_id: int = None, db: AsyncSession = Depends(get_db)):
    content_language = await ContentLanguagesService(ContentLanguagesRepository(db)).update_content_language(content_language_id=content_language_id, content_id=content_id, language_id=language_id)
    if content_language is None:
        raise HTTPException(status_code=400, detail="Content language not found")
    return content_language

@router.delete('/{content_language_id}')
async def delete_content_language(content_language_id: int, db: AsyncSession = Depends(get_db)):
    if not await ContentLanguagesService(ContentLanguagesRepository(db)).delete_content_language(content_language_id=content_language_id):
        raise HTTPException(status_code=400, detail="Content language not found")
    return {"message": "Content language deleted successfully"}