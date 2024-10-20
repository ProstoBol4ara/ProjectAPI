from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Countries

router = APIRouter(
    prefix="/countries",
    tags=["countries"]
)

@router.get('/', response_model=list[dict])
async def get_countries(db: Session = Depends(get_db)):
    countries = db.query(Countries).all()
    if countries is None:
        raise HTTPException(status_code=400, detail="Countries not found")
    return [{"country_id": country.country_id, "country_name": country.country_name} for country in countries]

@router.get('/{country_id}', response_model=dict)
async def get_country(country_id: int, db: Session = Depends(get_db)):
    country = db.query(Countries).filter(Countries.country_id == country_id).first()
    if country is None:
        raise HTTPException(status_code=400, detail="Countrie not found")
    return {"country_id": country.country_id, "country_name": country.country_name}

@router.post('/', response_model=dict)
async def create_country(country_name: str, db: Session = Depends(get_db)):
    try:
        new_country = Countries(country_name=country_name)
        db.add(new_country)
        db.commit()
        db.refresh(new_country)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"country_id": new_country.country_id, "country_name": new_country.country_name}

@router.put('/{country_id}', response_model=dict)
async def update_country(country_id: int, country_name: str = None, db: Session = Depends(get_db)):
    country = db.query(Countries).filter(Countries.country_id == country_id).first()
    if country is None:
        raise HTTPException(status_code=400, detail="Countrie not found")

    if country_name:
        country.country_name = country_name

    db.commit()
    db.refresh(country)
    return {"country_id": country.country_id, "country_name": country.country_name}

@router.delete('/{country_id}', response_model=dict)
async def delete_country(country_id: int, db: Session = Depends(get_db)):
    country = db.query(Countries).filter(Countries.country_id == country_id).first()
    if country is None:
        raise HTTPException(status_code=400, detail="Countrie not found")

    db.delete(country)
    db.commit()
    return {"message": "Countrie deleted successfully"}