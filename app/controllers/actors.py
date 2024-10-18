from fastapi import APIRouter, HTTPException
from database import get_depends
from datetime import datetime
from models import Actors

router = APIRouter(
    prefix="/actors",
    tags=["actors"]
)

@router.get('/', response_model=Actors)
async def get_actors(db: Session = get_depends()):
    actors = db.query(Actors)
    if actors is None:
        raise HTTPException(status_code=404, detail="Actors not found")
    return actors

@router.get('/{actor_id}', response_model=Actors)
async def get_actor(actor_id: int, db: Session = get_depends()):
    actor = db.query(Actors).filter(Actors.id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.post('/', response_model=Actors)
async def create_actor(actor_name: str, biography: str = '', birth_date: str = '', db: Session = get_depends()):
    try:
        birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
    except:
        raise HTTPException(status_code=400, detail='Birth date convert problem! format [day].[mounth].[year]')
    
    new_actor = Actors(actor_name=actor_name, biography=biography, birth_date=birth_date)
    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    return {"id": new_actor.id, "name": new_actor.name}

@router.put('/{actor_id}', response_model=Actors)
async def update_actor(actor_id: int, actor_name: str = None, biography: str = None, birth_date: str = None, db: Session = get_depends()):
    actor = db.query(Actors).filter(Actors.id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")

    if actor_name:
        actor.name = name
    if biography:
        actor.email = email
    if birth_date:
        actor.password = password

    db.commit()
    db.refresh(actor)
    return {"id": actor.id, "name": actor.name}

@router.delete('/{actor_id}', response_model=Actors)
async def delete_actor(actor_id: int, db: Session = get_depends()):
    actor = db.query(Actors).filter(Actors.id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")

    db.delete(actor)
    db.commit()
    return {"message": "Actors deleted successfully"}