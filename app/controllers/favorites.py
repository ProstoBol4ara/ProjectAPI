from fastapi import APIRouter, HTTPException, Depends
from repositories import FavoritesRepository
from database import AsyncSession, get_db
from services import FavoritesService
from responses.favorites import *

router = APIRouter(
    prefix="/favorites",
    tags=["favorites"]
)

@router.get('/', summary="Fetch all favorites", responses=get_favorites)
async def get_favorites(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/favorites
    """

    favorites = await FavoritesService(FavoritesRepository(db)).get_favorites()
    if favorites is None:
        raise HTTPException(status_code=400, detail="Favorites not found")
    return favorites

@router.get('/{favorite_id}', summary="Fetch favorite by id", responses=get_favorite)
async def get_favorite(favorite_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/favorites/1
    """

    favorite = await FavoritesService(FavoritesRepository(db)).get_favorite(favorite_id=favorite_id)
    if favorite is None:
        raise HTTPException(status_code=400, detail="Favorite not found")
    return favorite

@router.post('/', summary="Create favorite", responses=create_favorite)
async def create_favorite(user_id: int, content_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/favorites/
        {
            "favorite_id": 1,
            "user_id": 1,
            "content_id": 1
        }
    """

    try:
        new_favorite = await FavoritesService(FavoritesRepository(db)).create_favorite(user_id=user_id, content_id=content_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_favorite

@router.put('/{favorite_id}', summary="Update favorite by id", responses=update_favorite)
async def update_favorite(favorite_id: int, user_id: int = None, content_id = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/favorites/1
        {
            "favorite_id": 1,
            "content_id": 2
        }
    """

    try:
        favorite = await FavoritesService(FavoritesRepository(db)).update_favorite(favorite_id=favorite_id, user_id=user_id, content_id=content_id)
        if favorite is None:
            raise HTTPException(status_code=400, detail="Favorite not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return favorite

@router.delete('/{favorite_id}', summary="Delete favorite by id", responses=delete_favorite)
async def delete_favorite(favorite_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/favorites/1
    """

    if not await FavoritesService(FavoritesRepository(db)).delete_favorite(favorite_id=favorite_id):
        raise HTTPException(status_code=400, detail="Favorite not found")
    return {"message": "Favorite deleted successfully"}
