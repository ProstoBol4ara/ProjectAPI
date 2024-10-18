from fastapi import APIRouter, HTTPException
from database import get_depends
from models import ContentActors

router = APIRouter(
    prefix="/content_actors",
    tags=["content_actors"]
)

@router.get('/', response_model=ContentActors)
async def get_content_actors(db: Session = get_depends()):
    content_actors = db.query(ContentActors)
    if content_actors is None:
        raise HTTPException(status_code=404, detail="Сontent actors not found")
    return content_actors

@router.get('/{content_actor_id}', response_model=ContentActors)
async def get_content_actors(content_actor_id: int, db: Session = get_depends()):
    content_actor = db.query(ContentActors).filter(ContentActors.id == content_actor_id).first()
    if content_actor is None:
        raise HTTPException(status_code=404, detail="Content actor not found")
    return content_actor

@router.post('/', response_model=ContentActors)
async def create_content_actors(content_actorsname: str, email: str, password: str, db: Session = get_depends()):
    new_content_actor = ContentActors()
    db.add(new_content_actor)
    db.commit()
    db.refresh(new_content_actor)
    return {"id": new_content_actor.id, "name": new_content_actor.name, "email": new_content_actor.email}

@router.put('/{content_actor_id}', response_model=ContentActors)
async def update_content_actors(content_actor_id: int, db: Session = get_depends()):
    content_actor = db.query(ContentActors).filter(ContentActors.id == content_actors_id).first()
    if content_actor is None:
        raise HTTPException(status_code=404, detail="Сontent actor not found")
    
    db.commit()
    db.refresh(content_actor)
    return {"id": content_actor.id, "name": content_actor.name, "email": content_actor.email}

@router.delete('/{content_actor_id}', response_model=ContentActors)
async def delete_content_actors(content_actor_id: int, db: Session = get_depends()):
    content_actor = db.query(ContentActors).filter(ContentActors.id == content_actor_id).first()
    if content_actor is None:
        raise HTTPException(status_code=404, detail="Сontent actor not found")

    db.delete(content_actor)
    db.commit()
    return {"message": "Сontent actor deleted successfully"}