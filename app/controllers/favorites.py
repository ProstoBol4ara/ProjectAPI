from fastapi import APIRouter, HTTPException, Depends
from repositories import FavoritesRepository
from database import AsyncSession, get_db
from services import FavoritesService

router = APIRouter(
    prefix="/favorites",
    tags=["favorites"]
)

@router.get('/')
async def get_favorites(db: AsyncSession = Depends(get_db)):
    favorites = await FavoritesService(FavoritesRepository(db)).get_favorites()
    if favorites is None:
        raise HTTPException(status_code=400, detail="Favorites not found")
    return favorites

@router.get('/{favorite_id}')
async def get_favorite(favorite_id: int, db: AsyncSession = Depends(get_db)):
    favorite = await FavoritesService(FavoritesRepository(db)).get_favorite(favorite_id=favorite_id)
    if favorite is None:
        raise HTTPException(status_code=400, detail="Favorite not found")
    return favorite

@router.post('/')
async def create_favorite(user_id: int, content_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_favorite = await FavoritesService(FavoritesRepository(db)).create_favorite(user_id=user_id, content_id=content_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_favorite

@router.put('/{favorite_id}')
async def update_favorite(favorite_id: int, user_id: int = None, content_id = None, db: AsyncSession = Depends(get_db)):
    try:
        favorite = await FavoritesService(FavoritesRepository(db)).update_favorite(favorite_id=favorite_id, user_id=user_id, content_id=content_id)
        if favorite is None:
            raise HTTPException(status_code=400, detail="Favorite not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return favorite

@router.delete('/{favorite_id}')
async def delete_favorite(favorite_id: int, db: AsyncSession = Depends(get_db)):
    if not await FavoritesService(FavoritesRepository(db)).delete_favorite(favorite_id=favorite_id):
        raise HTTPException(status_code=400, detail="Favorite not found")
    return {"message": "Favorite deleted successfully"}