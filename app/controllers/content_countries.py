from fastapi import APIRouter, HTTPException, Depends
from services import ContentCountriesService
from repositories import ContentRepository
from database import AsyncSession, get_db
from responses.content_countries import *

router = APIRouter(
    prefix="/content_countries",
    tags=["content_countries"]
)

@router.get('/', summary="Fetch all content countries", responses=get_content_countries)
async def get_content_countries(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_countries
    """

    content_countries = await ContentCountriesService(ContentRepository(db)).get_content_countries()
    if content_countries is None:
        raise HTTPException(status_code=400, detail="Content countries not found")
    return content_countries

@router.get('/{content_country_id}', summary="Fetch content country", responses=get_content_country)
async def get_content_country(content_country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_countries/1
    """

    content_country = await ContentCountriesService(ContentRepository(db)).get_content_country(content_country_id=content_country_id)
    if content_country is None:
        raise HTTPException(status_code=400, detail="Content country not found")
    return content_country

@router.post('/', summary="Create content country", responses=create_content_country)
async def create_content_country(content_id: int, country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/content_countries/
        {
            "content_country_id": 1,
            "content_id": 1,
            "country_id": 1
        }
    """

    try:
        new_content_country = await ContentCountriesService(ContentRepository(db)).create_content_country(content_id=content_id, country_id=country_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_country

@router.put('/{content_country_id}', summary="Update content country", responses=update_content_country)
async def update_content_country(content_country_id: int, content_id: int = None, country_id: int = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/content_countries/1
        {
            "content_country_id": 1,
            "country_id": 2
        }
    """

    try:
        content_country = await ContentCountriesService(ContentRepository(db)).update_content_country(content_country_id=content_country_id, content_id=content_id, country_id=country_id)
        if content_country is None:
            raise HTTPException(status_code=400, detail="Content country not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return content_country

@router.delete('/{content_country_id}', summary="Delete content country", responses=delete_content_country)
async def delete_content_country(content_country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_countries/1
    """

    if not await ContentCountriesService(ContentRepository(db)).delete_content_country(content_country_id=content_country_id):
        raise HTTPException(status_code=400, detail="Content country not found")
    return {"message": "Content countries deleted successfully"}
