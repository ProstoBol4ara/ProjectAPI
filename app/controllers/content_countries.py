from services import ContentCountriesService
from api_decorators import handle_exceptions
from repositories import ContentRepository
from database import AsyncSession, get_db
from responses.content_countries import *
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/content_countries", tags=["content_countries"])


@router.get("/", summary="Fetch all content countries", responses=get_content_countries)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_countries
    """

    content_countries = await ContentCountriesService(ContentRepository(db)).get_all()
    return content_countries


@router.get(
    "/{content_country_id}",
    summary="Fetch content country",
    responses=get_content_country,
)
@handle_exceptions(status_code=400)
async def get_one(content_country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_countries/1
    """

    content_country = await ContentCountriesService(ContentRepository(db)).get_one(
        content_country_id=content_country_id
    )
    return content_country


@router.post("/", summary="Create content country", responses=create_content_country)
@handle_exceptions(status_code=400)
async def create(content_id: int, country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/content_countries/
        {
            "content_country_id": 1,
            "content_id": 1,
            "country_id": 1
        }
    """

    new_content_country = await ContentCountriesService(ContentRepository(db)).create(
        content_id=content_id, country_id=country_id
    )
    return new_content_country


@router.put(
    "/{content_country_id}",
    summary="Update content country",
    responses=update_content_country,
)
@handle_exceptions(status_code=400)
async def update(
    content_country_id: int,
    content_id: int = None,
    country_id: int = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/content_countries/1
        {
            "content_country_id": 1,
            "country_id": 2
        }
    """

    content_country = await ContentCountriesService(ContentRepository(db)).update(
        content_country_id=content_country_id,
        content_id=content_id,
        country_id=country_id,
    )
    return content_country


@router.delete(
    "/{content_country_id}",
    summary="Delete content country",
    responses=delete_content_country,
)
@handle_exceptions(status_code=400)
async def delete(content_country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_countries/1
    """

    await ContentCountriesService(ContentRepository(db)).delete(
        content_country_id=content_country_id
    )
    return {"message": "Content countries deleted successfully"}
