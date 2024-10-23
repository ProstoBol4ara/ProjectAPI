from fastapi import APIRouter, HTTPException, Depends
from services import ContentCountriesService
from repositories import ContentRepository
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/content_countries",
    tags=["content_countries"]
)

@router.get('/')
async def get_content_countries(db: AsyncSession = Depends(get_db)):
    content_countries = await ContentCountriesService(ContentRepository(db)).get_content_countries()
    if content_countries is None:
        raise HTTPException(status_code=400, detail="Content countries not found")
    return content_countries

@router.get('/{content_country_id}')
async def get_content_country(content_country_id: int, db: AsyncSession = Depends(get_db)):
    content_country = await ContentCountriesService(ContentRepository(db)).get_content_country(content_country_id=content_country_id)
    if content_country is None:
        raise HTTPException(status_code=400, detail="Content country not found")
    return content_country

@router.post('/')
async def create_content_country(content_id: int, country_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_content_country = await ContentCountriesService(ContentRepository(db)).create_content_country(content_id=content_id, country_id=country_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_country

@router.put('/{content_country_id}')
async def update_content_country(content_country_id: int, content_id: int = None, country_id: int = None, db: AsyncSession = Depends(get_db)):
    try:
        content_country = await ContentCountriesService(ContentRepository(db)).update_content_country(content_country_id=content_country_id, content_id=content_id, country_id=country_id)
        if content_country is None:
            raise HTTPException(status_code=400, detail="Content country not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return content_country

@router.delete('/{content_country_id}')
async def delete_content_country(content_country_id: int, db: AsyncSession = Depends(get_db)):
    if not await ContentCountriesService(ContentRepository(db)).delete_content_country(content_country_id=content_country_id):
        raise HTTPException(status_code=400, detail="Content country not found")
    return {"message": "Content countries deleted successfully"}