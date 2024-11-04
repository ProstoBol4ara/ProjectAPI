from repositories import FavoritesRepository
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import FavoritesService
from responses.favorites import *

router = APIRouter(prefix="/favorites", tags=["favorites"])


@router.get("/", summary="Fetch all favorites", responses=get_favorites)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/favorites
    """

    favorites = await FavoritesService(FavoritesRepository(db)).get_all()
    return favorites


@router.get("/{favorite_id}", summary="Fetch favorite by id", responses=get_favorite)
@handle_exceptions(status_code=400)
async def get_one(favorite_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/favorites/1
    """

    favorite = await FavoritesService(FavoritesRepository(db)).get_one(
        favorite_id=favorite_id
    )
    return favorite


@router.post("/", summary="Create favorite", responses=create_favorite)
@handle_exceptions(status_code=400)
async def create(user_id: int, content_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/favorites/
        {
            "favorite_id": 1,
            "user_id": 1,
            "content_id": 1
        }
    """

    new_favorite = await FavoritesService(FavoritesRepository(db)).create(
        user_id=user_id, content_id=content_id
    )
    return new_favorite


@router.put(
    "/{favorite_id}", summary="Update favorite by id", responses=update_favorite
)
@handle_exceptions(status_code=400)
async def update(
    favorite_id: int,
    user_id: int = None,
    content_id=None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/favorites/1
        {
            "favorite_id": 1,
            "content_id": 2
        }
    """

    favorite = await FavoritesService(FavoritesRepository(db)).update(
        favorite_id=favorite_id, user_id=user_id, content_id=content_id
    )

    return favorite


@router.delete(
    "/{favorite_id}", summary="Delete favorite by id", responses=delete_favorite
)
@handle_exceptions(status_code=400)
async def delete(favorite_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/favorites/1
    """

    await FavoritesService(FavoritesRepository(db)).delete(favorite_id=favorite_id)
    return {"message": "Favorite deleted successfully"}
