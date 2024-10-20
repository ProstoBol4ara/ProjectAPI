from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Favorites

router = APIRouter(
    prefix="/favorites",
    tags=["favorites"]
)

@router.get('/', response_model=list[dict])
async def get_favorites(db: Session = Depends(get_db)):
    favorites = db.query(Favorites).all()
    if favorites is None:
        raise HTTPException(status_code=400, detail="Favorites not found")
    return [{"favorite_id": favorite.favorite_id, "user_id": favorite.user_id, "content_id": favorite.content_id} for favorite in favorites]

@router.get('/{favorite_id}', response_model=dict)
async def get_favorite(favorite_id: int, db: Session = Depends(get_db)):
    favorite = db.query(Favorites).filter(Favorites.favorite_id == favorite_id).first()
    if favorite is None:
        raise HTTPException(status_code=400, detail="Favorite not found")
    return {"favorite_id": favorite.favorite_id, "user_id": favorite.user_id, "content_id": favorite.content_id}

@router.post('/', response_model=dict)
async def create_favorite(user_id: int, content_id: int, db: Session = Depends(get_db)):
    try:
        new_favorite = Favorites(user_id=user_id, content_id=content_id)
        db.add(new_favorite)
        db.commit()
        db.refresh(new_favorite)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"favorite_id": new_favorite.favorite_id, "user_id": new_favorite.user_id, "content_id": new_favorite.content_id}

@router.put('/{favorite_id}', response_model=dict)
async def update_favorite(favorite_id: int, user_id: int = None, content_id = None, db: Session = Depends(get_db)):
    favorite = db.query(Favorites).filter(Favorites.favorite_id == favorite_id).first()
    if favorite is None:
        raise HTTPException(status_code=400, detail="Favorite not found")

    if user_id:
        favorite.user_id = user_id
    if content_id:
        favorite.content_id = content_id

    db.commit()
    db.refresh(favorite)
    return {"favorite_id": favorite.favorite_id, "user_id": favorite.user_id, "content_id": favorite.content_id}

@router.delete('/{favorite_id}', response_model=dict)
async def delete_favorite(favorite_id: int, db: Session = Depends(get_db)):
    favorite = db.query(Favorites).filter(Favorites.favorite_id == favorite_id).first()
    if favorite is None:
        raise HTTPException(status_code=400, detail="Favorite not found")

    db.delete(favorite)
    db.commit()
    return {"message": "Favorite deleted successfully"}