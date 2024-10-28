from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentLanguagesRepository
from services import ContentLanguagesService
from database import AsyncSession, get_db
from responses.content_languages import *

router = APIRouter(
    prefix="/content_languages",
    tags=["content_languages"]
)

@router.get('/', summary="Fetch all content languages", responses=get_content_languages)
async def get_content_languages(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_languages
    """

    content_languages = await ContentLanguagesService(ContentLanguagesRepository(db)).get_content_languages()
    if content_languages is None:
        raise HTTPException(status_code=400, detail="Content languages not found")
    return content_languages

@router.get('/{content_language_id}', summary="Fetch content language by id", responses=get_content_language)
async def get_content_language(content_language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_languages/1
    """

    content_language = await ContentLanguagesService(ContentLanguagesRepository(db)).get_content_language(content_language_id=content_language_id)
    if content_language is None:
        raise HTTPException(status_code=400, detail="Content language not found")
    return content_language

@router.post('/', summary="Create content language", responses=create_content_language)
async def create_content_language(content_id: int, language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/content_languages/
        {
            "content_language_id": 1,
            "content_id": 1,
            "language_id": 1
        }
    """

    try:
        new_content_language = await ContentLanguagesService(ContentLanguagesRepository(db)).create_content_language(content_id=content_id, language_id=language_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_language

@router.put('/{content_language_id}', summary="Update content language by id", responses=update_content_language)
async def update_content_language(content_language_id: int, content_id: int = None, language_id: int = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/content_languages/1
        {
            "content_language_id": 1,
            "content_id": 1,
            "language_id": 2
        }
    """

    content_language = await ContentLanguagesService(ContentLanguagesRepository(db)).update_content_language(content_language_id=content_language_id, content_id=content_id, language_id=language_id)
    if content_language is None:
        raise HTTPException(status_code=400, detail="Content language not found")
    return content_language

@router.delete('/{content_language_id}', summary="Delete content language by id", responses=delete_content_language)
async def delete_content_language(content_language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_languages/1
    """

    if not await ContentLanguagesService(ContentLanguagesRepository(db)).delete_content_language(content_language_id=content_language_id):
        raise HTTPException(status_code=400, detail="Content language not found")
    return {"message": "Content language deleted successfully"}
