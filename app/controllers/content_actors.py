from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import ContentActors

router = APIRouter(
    prefix="/content_actors",
    tags=["content_actors"]
)

@router.get('/', response_model=list[dict])
async def get_content_actors(db: Session = Depends(get_db)):
    content_actors = db.query(ContentActors).all()
    if content_actors is None:
        raise HTTPException(status_code=400, detail="Сontent actors not found")
    return [{"content_actor_id": content_actor.content_actor_id, "content_id": content_actor.content_id, "actor_id": content_actor.actor_id, "role": content_actor.role} for content_actor in content_actors]

@router.get('/{content_actor_id}', response_model=dict)
async def get_content_actors(content_actor_id: int, db: Session = Depends(get_db)):
    content_actor = db.query(ContentActors).filter(ContentActors.content_actor_id == content_actor_id).first()
    if content_actor is None:
        raise HTTPException(status_code=400, detail="Content actor not found")
    return {"content_actor_id": content_actor.content_actor_id, "content_id": content_actor.content_id, "actor_id": content_actor.actor_id, "role": content_actor.role}

@router.post('/', response_model=dict)
async def create_content_actors(content_id: int, actor_id: int, role: str = None, db: Session = Depends(get_db)):
    try:
        new_content_actor = ContentActors(content_id=content_id, actor_id=actor_id, role=role)
        db.add(new_content_actor)
        db.commit()
        db.refresh(new_content_actor)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"content_actor_id": new_content_actor.content_actor_id, "actor_id": new_content_actor.actor_id, "role": new_content_actor.role}

@router.put('/{content_actor_id}', response_model=dict)
async def update_content_actors(content_actor_id: int, content_id: int = None, actor_id: int = None, role: str = None, db: Session = Depends(get_db)):
    content_actor = db.query(ContentActors).filter(ContentActors.content_actor_id == content_actors_id).first()
    if content_actor is None:
        raise HTTPException(status_code=400, detail="Сontent actor not found")
    
    if content_id:
        content_actor.content_id = content_id
    if actor_id:
        content_actor.actor_id = actor_id
    if role:
        content_actor.role = role

    db.commit()
    db.refresh(content_actor)
    return {"content_actor_id": content_actor.content_actor_id, "actor_id": content_actor.actor_id, "role": content_actor.role}

@router.delete('/{content_actor_id}', response_model=dict)
async def delete_content_actors(content_actor_id: int, db: Session = Depends(get_db)):
    content_actor = db.query(ContentActors).filter(ContentActors.content_actor_id == content_actor_id).first()
    if content_actor is None:
        raise HTTPException(status_code=400, detail="Сontent actor not found")

    db.delete(content_actor)
    db.commit()
    return {"message": "Сontent actor deleted successfully"}