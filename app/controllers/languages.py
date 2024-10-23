from fastapi import APIRouter, HTTPException, Depends
from repositories import LanguagesRepository
from database import AsyncSession, get_db
from services import LanguagesService

router = APIRouter(
    prefix="/languages",
    tags=["languages"]
)

@router.get('/')
async def get_languages(db: AsyncSession = Depends(get_db)):
    languages = await LanguagesService(LanguagesRepository(db)).get_languages()
    if languages is None:
        raise HTTPException(status_code=400, detail="Languages not found")
    return languages

@router.get('/{language_id}')
async def get_language(language_id: int, db: AsyncSession = Depends(get_db)):
    language = await LanguagesService(LanguagesRepository(db)).get_language(language_id=language_id)
    if language is None:
        raise HTTPException(status_code=400, detail="Language not found")
    return language

@router.post('/')
async def create_language(language_name: str, db: AsyncSession = Depends(get_db)):
    try:
        new_language = await LanguagesService(LanguagesRepository(db)).create_language(language_name=language_name)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return new_language

@router.put('/{language_id}')
async def update_language(language_id: int, language_name: str = None, db: AsyncSession = Depends(get_db)):
    language = await LanguagesService(LanguagesRepository(db)).update_language(language_id=language_id, language_name=language_name)
    if language is None:
        raise HTTPException(status_code=400, detail="Language not found")
    return language

@router.delete('/{language_id}')
async def delete_language(language_id: int, db: AsyncSession = Depends(get_db)):
    if not await LanguagesService(LanguagesRepository(db)).delete_language(language_id=language_id):
        raise HTTPException(status_code=400, detail="Language not found")
    return {"message": "Language deleted successfully"}