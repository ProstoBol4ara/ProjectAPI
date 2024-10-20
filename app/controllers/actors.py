from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from datetime import datetime
from models import Actors

router = APIRouter(
    prefix="/actors",
    tags=["actors"]
)

@router.get('/', response_model=list[dict])
async def get_actors(db: Session = Depends(get_db)):
    actors = db.query(Actors).all()
    if actors is None:
        raise HTTPException(status_code=400, detail="Actors not found")
    return [{"actor_id": actor.actor_id, "actor_name": actor.actor_name, "biography": actor.biography, "birth_date": actor.birth_date} for actor in actors]

@router.get('/{actor_id}', response_model=dict)
async def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = db.query(Actors).filter(Actors.actor_id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=400, detail="Actor not found")
    return {"actor_id": actor.actor_id, "actor_name": actor.actor_name, "biography": actor.biography, "birth_date": actor.birth_date}

@router.post('/', response_model=dict)
async def create_actor(actor_name: str, biography: str = None, birth_date: str = None, db: Session = Depends(get_db)):
    try:
        if not birth_date is None:
            birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
        new_actor = Actors(actor_name=actor_name, biography=biography, birth_date=birth_date)
        db.add(new_actor)
        db.commit()
        db.refresh(new_actor)   
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"actor_id": new_actor.actor_id, "name": new_actor.actor_name}

@router.put('/{actor_id}', response_model=dict)
async def update_actor(actor_id: int, actor_name: str = None, biography: str = None, birth_date: str = None, db: Session = Depends(get_db)):
    actor = db.query(Actors).filter(Actors.actor_id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=400, detail="Actor not found")

    if actor_name:
        actor.actor_name = actor_name
    if biography:
        actor.biography = biography
    if birth_date:
        actor.birth_date = birth_date
    
    db.commit()
    db.refresh(actor)
    return {"actor_id": actor.actor_id, "name": actor.actor_name}

@router.delete('/{actor_id}', response_model=dict)
async def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = db.query(Actors).filter(Actors.actor_id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=400, detail="Actor not found")

    db.delete(actor)
    db.commit()
    return {"message": "Actors deleted successfully"}