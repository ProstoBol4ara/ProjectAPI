from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Directors

router = APIRouter(
    prefix="/directors",
    tags=["directors"]
)

@router.get('/', response_model=list[dict])
async def get_directors(db: Session = Depends(get_db)):
    directors = db.query(Directors).all()
    if directors is None:
        raise HTTPException(status_code=400, detail="Directors not found")
    return [{"director_id": director.director_id, "director_name": director.director_name, "biography": director.biography, "birth_date": director.birth_date} for director in directors]

@router.get('/{director_id}', response_model=dict)
async def get_director(director_id: int, db: Session = Depends(get_db)):
    director = db.query(Directors).filter(Directors.director_id == director_id).first()
    if director is None:
        raise HTTPException(status_code=400, detail="Director not found")
    return {"director_id": director.director_id, "director_name": director.director_name, "biography": director.biography, "birth_date": director.birth_date}

@router.post('/', response_model=dict)
async def create_director(director_name: str, biography: str = None, birth_date: str = None, db: Session = Depends(get_db)):
    try:
        if not birth_date is None:
            birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
        new_director = Directors(director_name=director_name, biography=biography, birth_date=birth_date)
        db.add(new_director)
        db.commit()
        db.refresh(new_director)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"director_id": new_director.director_id, "director_name": new_director.director_name, "biography": new_director.biography, "birth_date": new_director.birth_date}

@router.put('/{director_id}', response_model=dict)
async def update_director(director_id: int, director_name: str = None, biography:str = None, birth_date: str = None, db: Session = Depends(get_db)):
    try:
        director = db.query(Directors).filter(Directors.director_id == director_id).first()
        if director is None:
            raise HTTPException(status_code=400, detail="Director not found")

        if director_name:
            director.director_name = director_name
        if biography:
            director.biography = biography
        if birth_date:
            director.birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()

        db.commit()
        db.refresh(director)
    except:
        raise HTTPException(status_code=400, detail="Update failed") 
    return {"director_id": director.director_id, "director_name": director.director_name, "biography": director.biography, "birth_date": director.birth_date}

@router.delete('/{director_id}', response_model=dict)
async def delete_director(director_id: int, db: Session = Depends(get_db)):
    director = db.query(Directors).filter(Directors.director_id == director_id).first()
    if director is None:
        raise HTTPException(status_code=400, detail="Director not found")

    db.delete(director)
    db.commit()
    return {"message": "Director deleted successfully"}