from api_decorators import handle_exceptions
from repositories import CountriesRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import CountriesService
from responses.countries import *

router = APIRouter(prefix="/countries", tags=["countries"])


@router.get("/", summary="Fetch all countries", responses=get_countries)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/countries
    """

    countries = await CountriesService(CountriesRepository(db)).get_all()
    return countries


@router.get("/{country_id}", summary="Fetch countries by id", responses=get_country)
@handle_exceptions(status_code=400)
async def get_one(country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/countries/1
    """

    country = await CountriesService(CountriesRepository(db)).get_one(
        country_id=country_id
    )
    return country


@router.post("/", summary="Create country", responses=create_country)
@handle_exceptions(status_code=400)
async def create(country_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/countries/
        {
            "country_id": 1,
            "country_name": "aaa"
        }
    """

    new_country = await CountriesService(CountriesRepository(db)).create(
        country_name=country_name
    )
    return new_country


@router.put("/{country_id}", summary="Update country by id", responses=update_country)
@handle_exceptions(status_code=400)
async def update(
    country_id: int, country_name: str = None, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        PUT /api/countries/1
        {
            "country_id": 1,
            "country_name": "bbb"
        }
    """

    country = await CountriesService(CountriesRepository(db)).update(
        country_id=country_id, country_name=country_name
    )
    return country


@router.delete(
    "/{country_id}", summary="Delete country by id", responses=delete_country
)
@handle_exceptions(status_code=400)
async def delete(country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/contents/1
    """

    await CountriesService(CountriesRepository(db)).delete(country_id=country_id)
    return {"message": "Countrie deleted successfully"}
