from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import ContentCountries

router = APIRouter(
    prefix="/content_countries",
    tags=["content_countries"]
)

@router.get('/')
async def get_content_countries(db: Session = Depends(get_db)):
    content_countries = db.query(ContentCountries).all()
    if content_countries is None:
        raise HTTPException(status_code=400, detail="Content countries not found")
    return [{"content_country_id": content_country.content_actor_id, "content_id": content_country.content_id, "country_id": content_country.country_id} for content_country in content_countries]

@router.get('/{content_country_id}')
async def get_content_country(content_country_id: int, db: Session = Depends(get_db)):
    content_country = db.query(ContentCountries).filter(ContentCountries.content_country_id == content_country_id).first()
    if content_country is None:
        raise HTTPException(status_code=400, detail="Content countries not found")
    return {"content_country_id": content_country.content_actor_id, "content_id": content_country.content_id, "country_id": content_country.country_id}

@router.post('/')
async def create_content_country(content_id: int, country_id: int, db: Session = Depends(get_db)):
    try:
        new_content_country = ContentCountries(content_id=content_id, country_id=country_id)
        db.add(new_content_country)
        db.commit()
        db.refresh(new_content_country)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"content_country_id": new_content_country.content_country_id, "content_id": new_content_country.content_id, "country_id": new_content_country.country_id}

@router.put('/{content_country_id}')
async def update_content_country(content_country_id: int, content_id: int = None, country_id: int = None, db: Session = Depends(get_db)):
    content_country = db.query(ContentCountries).filter(ContentCountries.content_country_id == content_country_id).first()
    if content_country is None:
        raise HTTPException(status_code=400, detail="Content countries not found")

    if content_id:
        content_country.content_id = content_id
    if country_id:
        content_country.country_id = country_id
    
    db.commit()
    db.refresh(content_country)
    return {"content_country_id": content_country.content_country_id, "content_id": content_countrie.content_id, "country_id": content_countrie.country_id}

@router.delete('/{content_country_id}')
async def delete_content_country(content_country_id: int, db: Session = Depends(get_db)):
    content_country = db.query(ContentCountries).filter(ContentCountries.content_country_id == content_country_id).first()
    if content_country is None:
        raise HTTPException(status_code=400, detail="Content countries not found")

    db.delete(content_country)
    db.commit()
    return {"message": "Content countries deleted successfully"}