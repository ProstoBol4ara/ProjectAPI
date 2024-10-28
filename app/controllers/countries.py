from fastapi import APIRouter, HTTPException, Depends
from repositories import CountriesRepository
from database import AsyncSession, get_db
from services import CountriesService
from responses.countries import *

router = APIRouter(
    prefix="/countries",
    tags=["countries"]
)

@router.get('/', summary="Fetch all countries", responses=get_countries)
async def get_countries(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/countries
    """

    countries = await CountriesService(CountriesRepository(db)).get_countries()
    if countries is None:
        raise HTTPException(status_code=400, detail="Countries not found")
    return countries

@router.get('/{country_id}', summary="Fetch countries by id", responses=get_country)
async def get_country(country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/countries/1
    """

    country = await CountriesService(CountriesRepository(db)).get_country(country_id=country_id)
    if country is None:
        raise HTTPException(status_code=400, detail="Country not found")
    return country

@router.post('/', summary="Create country", responses=create_country)
async def create_country(country_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/countries/
        {
            "country_id": 1,
            "country_name": "aaa"
        }
    """

    try:
        new_country = await CountriesService(CountriesRepository(db)).create_country(country_name=country_name)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_country

@router.put('/{country_id}', summary="Update country by id", responses=update_country)
async def update_country(country_id: int, country_name: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/countries/1
        {
            "country_id": 1,
            "country_name": "bbb"
        }
    """

    try:
        country = await CountriesService(CountriesRepository(db)).update_country(country_id=country_id, country_name=country_name)
        if country is None:
            raise HTTPException(status_code=400, detail="Country not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return country

@router.delete('/{country_id}', summary="Delete country by id", responses=delete_country)
async def delete_country(country_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/contents/1
    """

    if not await CountriesService(CountriesRepository(db)).delete_country(country_id=country_id):
        raise HTTPException(status_code=400, detail="Country not found")
    return {"message": "Countrie deleted successfully"}
