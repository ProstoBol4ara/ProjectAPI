from fastapi import APIRouter, HTTPException, Depends
from repositories import CountriesRepository
from database import AsyncSession, get_db
from services import CountriesService

router = APIRouter(
    prefix="/countries",
    tags=["countries"]
)

@router.get('/')
async def get_countries(db: AsyncSession = Depends(get_db)):
    countries = await CountriesService(CountriesRepository(db)).get_countries()
    if countries is None:
        raise HTTPException(status_code=400, detail="Country not found")
    return countries

@router.get('/{country_id}')
async def get_country(country_id: int, db: AsyncSession = Depends(get_db)):
    country = await CountriesService(CountriesRepository(db)).get_country(country_id=country_id)
    if country is None:
        raise HTTPException(status_code=400, detail="Country not found")
    return country

@router.post('/')
async def create_country(country_name: str, db: AsyncSession = Depends(get_db)):
    try:
        new_country = await CountriesService(CountriesRepository(db)).create_country(country_name=country_name)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_country

@router.put('/{country_id}')
async def update_country(country_id: int, country_name: str = None, db: AsyncSession = Depends(get_db)):
    try:
        country = await CountriesService(CountriesRepository(db)).update_country(country_id=country_id, country_name=country_name)
        if country is None:
            raise HTTPException(status_code=400, detail="Country not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return country

@router.delete('/{country_id}')
async def delete_country(country_id: int, db: AsyncSession = Depends(get_db)):
    if not await CountriesService(CountriesRepository(db)).delete_country(country_id=country_id):
        raise HTTPException(status_code=400, detail="Country not found")
    return {"message": "Countrie deleted successfully"}