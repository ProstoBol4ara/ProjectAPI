from api_decorators import handle_exceptions
from repositories import LanguagesRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import LanguagesService
from responses.languages import *

router = APIRouter(
    prefix="/languages",
    tags=["languages"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all languages", responses=get_languages)
async def get_languages(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/languages
    """

    languages = await LanguagesService(LanguagesRepository(db)).get_languages()
    return languages

@handle_exceptions(status_code=400)
@router.get('/{language_id}', summary="Fetch language by id", responses=get_language)
async def get_language(language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/languages/1
    """

    language = await LanguagesService(LanguagesRepository(db)).get_language(language_id=language_id)
    return language

@handle_exceptions(status_code=400)
@router.post('/', summary="Create language", responses=create_language)
async def create_language(language_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/languages/
        {
            "language_id": 1,
            "name": "aaa"
        }
    """

    new_language = await LanguagesService(LanguagesRepository(db)).create_language(language_name=language_name)
    return new_language

@handle_exceptions(status_code=400)
@router.put('/{language_id}', summary="Update language by id", responses=update_language)
async def update_language(language_id: int, language_name: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/languages/1
        {
            "language_id": 1,
            "name": "bbb"
        }
    """

    language = await LanguagesService(LanguagesRepository(db)).update_language(language_id=language_id, language_name=language_name)
    return language

@handle_exceptions(status_code=400)
@router.delete('/{language_id}', summary="Delete language by id", responses=delete_language)
async def delete_language(language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/languages/1
    """

    await LanguagesService(LanguagesRepository(db)).delete_language(language_id=language_id)
    return {"message": "Language deleted successfully"}
