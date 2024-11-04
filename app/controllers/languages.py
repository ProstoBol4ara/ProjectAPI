from api_decorators import handle_exceptions
from repositories import LanguagesRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import LanguagesService
from responses.languages import *

router = APIRouter(prefix="/languages", tags=["languages"])


@router.get("/", summary="Fetch all languages", responses=get_languages)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/languages
    """

    languages = await LanguagesService(LanguagesRepository(db)).get_all()
    return languages


@router.get("/{language_id}", summary="Fetch language by id", responses=get_language)
@handle_exceptions(status_code=400)
async def get_one(language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/languages/1
    """

    language = await LanguagesService(LanguagesRepository(db)).get_one(
        language_id=language_id
    )
    return language


@router.post("/", summary="Create language", responses=create_language)
@handle_exceptions(status_code=400)
async def create(language_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/languages/
        {
            "language_id": 1,
            "name": "aaa"
        }
    """

    new_language = await LanguagesService(LanguagesRepository(db)).create(
        language_name=language_name
    )
    return new_language


@router.put(
    "/{language_id}", summary="Update language by id", responses=update_language
)
@handle_exceptions(status_code=400)
async def update(
    language_id: int, language_name: str = None, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        PUT /api/languages/1
        {
            "language_id": 1,
            "name": "bbb"
        }
    """

    language = await LanguagesService(LanguagesRepository(db)).update(
        language_id=language_id, language_name=language_name
    )
    return language


@router.delete(
    "/{language_id}", summary="Delete language by id", responses=delete_language
)
@handle_exceptions(status_code=400)
async def delete(language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/languages/1
    """

    await LanguagesService(LanguagesRepository(db)).delete(language_id=language_id)
    return {"message": "Language deleted successfully"}
