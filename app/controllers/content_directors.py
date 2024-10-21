from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import ContentDirectors

router = APIRouter(
    prefix="/content_directors",
    tags=["content_directors"]
)

@router.get('/')
async def get_content_directors(db: Session = Depends(get_db)):
    content_directors = db.query(ContentDirectors).all()
    if content_directors is None:
        raise HTTPException(status_code=400, detail="Content directors not found")
    return [{"content_director_id": content_director.content_director_id, "content_id": content_director.content_id, "director_id": content_director.director_id} for content_director in content_directors]

@router.get('/{content_director_id}')
async def get_content_director(content_director_id: int, db: Session = Depends(get_db)):
    content_director = db.query(ContentDirectors).filter(ContentDirectors.content_director_id == content_director_id).first()
    if content_director is None:
        raise HTTPException(status_code=400, detail="Content director not found")
    return {"content_director_id": content_director.content_director_id, "content_id": content_director.content_id, "director_id": content_director.director_id}

@router.post('/')
async def create_content_director(content_id: int, director_id: int, db: Session = Depends(get_db)):
    try:
        new_content_director = ContentDirectors(content_id=content_id, director_id=director_id)
        db.add(new_content_director)
        db.commit()
        db.refresh(new_content_director)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"content_director_id": new_content_director.content_director_id, "content_id": new_content_director.content_id, "director_id": new_content_director.director_id}

@router.put('/{content_director_id}')
async def update_content_director(content_director_id: int, content_id: int = None, director_id: int = None, db: Session = Depends(get_db)):
    content_director = db.query(ContentDirectors).filter(ContentDirectors.content_director_id == content_director_id).first()
    if content_director is None:
        raise HTTPException(status_code=400, detail="Content director not found")

    if content_id:
        content_director.email = content_id
    if director_id:
        content_director.director_id = director_id

    db.commit()
    db.refresh(content_director)
    return {"content_director_id": content_director.content_director_id, "content_id": content_director.content_id, "director_id": content_director.director_id}

@router.delete('/{content_director_id}')
async def delete_content_director(content_director_id: int, db: Session = Depends(get_db)):
    content_director = db.query(ContentDirectors).filter(ContentDirectors.content_director_id == content_director_id).first()
    if content_director is None:
        raise HTTPException(status_code=400, detail="Content director not found")

    db.delete(content_director)
    db.commit()
    return {"message": "Content director deleted successfully"}