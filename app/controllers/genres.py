from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Genres

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)

@router.get('/')
async def get_genres(db: Session = Depends(get_db)):
    genres = db.query(Genres).all()
    if genres is None:
        raise HTTPException(status_code=400, detail="Genres not found")
    return [{"genre_id": genre.genre_id, "genre_name": genre.genre_name} for genre in genres]

@router.get('/{genre_id}')
async def get_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genres).filter(Genres.genre_id == genre_id).first()
    if genre is None:
        raise HTTPException(status_code=400, detail="Genre not found")
    return {"genre_id": genre.genre_id, "genre_name": genre.genre_name}

@router.post('/')
async def create_genre(genre_name: str, db: Session = Depends(get_db)):
    try:
        new_genre = Genres(genre_name=genre_name)
        db.add(new_genre)
        db.commit()
        db.refresh(new_genre)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"genre_id": new_genre.genre_id, "genre_name": new_genre.genre_name}

@router.put('/{genre_id}')
async def update_genre(genre_id: int, genre_name: str = None, db: Session = Depends(get_db)):
    genre = db.query(Genres).filter(Genres.genre_id == genre_id).first()
    if genre is None:
        raise HTTPException(status_code=400, detail="Genre not found")

    if genre_name:
        genre.genre_name = genre_name

    db.commit()
    db.refresh(genre)
    return {"genre_id": genre.genre_id, "genre_name": genre.genre_name}

@router.delete('/{genre_id}')
async def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genres).filter(Genres.genre_id == genre_id).first()
    if genre is None:
        raise HTTPException(status_code=400, detail="Genre not found")

    db.delete(genre)
    db.commit()
    return {"message": "Genre deleted successfully"}