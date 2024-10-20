from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import ContentGenres

router = APIRouter(
    prefix="/content_genres",
    tags=["content_genres"]
)

@router.get('/', response_model=list[dict])
async def get_content_genres(db: Session = Depends(get_db)):
    content_genres = db.query(ContentGenres).all()
    if content_genres is None:
        raise HTTPException(status_code=400, detail="Content genres not found")
    return [{"content_genre_id": content_genre, "content_id": content_genre.content_id, "genre_id": content_genre.genre_id} for content_genre in content_genres]

@router.get('/{content_genre_id}', response_model=dict)
async def get_content_genre(content_genre_id: int, db: Session = Depends(get_db)):
    content_genre = db.query(ContentGenres).filter(ContentGenres.content_genre_id == content_genre_id).first()
    if content_genre is None:
        raise HTTPException(status_code=400, detail="Content genre not found")
    return {"content_genre_id": content_genre, "content_id": content_genre.content_id, "genre_id": content_genre.genre_id}

@router.post('/', response_model=dict)
async def create_content_genre(content_id: int, genres_id: int, db: Session = Depends(get_db)):
    try:
        new_content_genre = ContentGenres(content_id=content_id, genres_id=genres_id)
        db.add(new_content_genre)
        db.commit()
        db.refresh(new_content_genre)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"content_genre_id": new_content_genre.content_genre_id, "content_id": new_content_genre.content_id, "genres_id": new_content_genre.genres_id}

@router.put('/{content_genre_id}', response_model=dict)
async def update_content_genre(content_genre_id: int, content_id: int = None, genres_id: int = None, db: Session = Depends(get_db)):
    content_genre = db.query(ContentGenres).filter(ContentGenres.content_genre_id == content_genre_id).first()
    if content_genre is None:
        raise HTTPException(status_code=400, detail="Content genre not found")

    if content_id:
        content_genre.email = content_id
    if genres_id:
        content_genre.genres_id = genres_id

    db.commit()
    db.refresh(content_genre)
    return {"content_genre_id": content_genre.content_genre_id, "content_id": content_genre.content_id, "genres_id": content_genre.genres_id}

@router.delete('/{content_genre_id}', response_model=dict)
async def delete_content_genre(content_genre_id: int, db: Session = Depends(get_db)):
    content_genre = db.query(ContentGenres).filter(ContentGenres.content_genre_id == content_genre_id).first()
    if content_genre is None:
        raise HTTPException(status_code=400, detail="Content genre not found")

    db.delete(content_genre)
    db.commit()
    return {"message": "Content genre deleted successfully"}