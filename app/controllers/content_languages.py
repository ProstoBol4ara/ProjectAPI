from repositories import ContentLanguagesRepository
from services import ContentLanguagesService
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from responses.content_languages import *
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/content_languages", tags=["content_languages"])


@router.get("/", summary="Fetch all content languages", responses=get_content_languages)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_languages
    """

    content_languages = await ContentLanguagesService(
        ContentLanguagesRepository(db)
    ).get_all()
    return content_languages


@router.get(
    "/{content_language_id}",
    summary="Fetch content language by id",
    responses=get_content_language,
)
@handle_exceptions(status_code=400)
async def get_one(content_language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_languages/1
    """

    content_language = await ContentLanguagesService(
        ContentLanguagesRepository(db)
    ).get_one(content_language_id=content_language_id)
    return content_language


@router.post("/", summary="Create content language", responses=create_content_language)
@handle_exceptions(status_code=400)
async def create(content_id: int, language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/content_languages/
        {
            "content_language_id": 1,
            "content_id": 1,
            "language_id": 1
        }
    """

    new_content_language = await ContentLanguagesService(
        ContentLanguagesRepository(db)
    ).create(content_id=content_id, language_id=language_id)

    return new_content_language


@router.put(
    "/{content_language_id}",
    summary="Update content language by id",
    responses=update_content_language,
)
@handle_exceptions(status_code=400)
async def update(
    content_language_id: int,
    content_id: int = None,
    language_id: int = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/content_languages/1
        {
            "content_language_id": 1,
            "content_id": 1,
            "language_id": 2
        }
    """

    content_language = await ContentLanguagesService(
        ContentLanguagesRepository(db)
    ).update(
        content_language_id=content_language_id,
        content_id=content_id,
        language_id=language_id,
    )

    return content_language


@router.delete(
    "/{content_language_id}",
    summary="Delete content language by id",
    responses=delete_content_language,
)
@handle_exceptions(status_code=400)
async def delete(content_language_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_languages/1
    """

    await ContentLanguagesService(ContentLanguagesRepository(db)).delete(
        content_language_id=content_language_id
    )
    return {"message": "Content language deleted successfully"}
