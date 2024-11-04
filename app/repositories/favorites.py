from database import AsyncSession, select, delete
from models import Favorites


class FavoritesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        favorites = await self.db.execute(select(Favorites))
        return favorites.scalars().all()

    async def get_one(self, favorite_id: int):
        favorite = await self.db.execute(
            select(Favorites).where(Favorites.favorite_id == favorite_id)
        )
        return favorite.scalar_one_or_none()

    async def create(self, user_id: int, content_id: int):
        new_favorite = Favorites(user_id=user_id, content_id=content_id)
        self.db.add(new_favorite)
        await self.db.commit()
        await self.db.refresh(new_favorite)
        return new_favorite

    async def update(self, favorite_id: int, user_id: int = None, content_id=None):
        favorite = await self.db.execute(
            select(Favorites).where(Favorites.favorite_id == favorite_id)
        )
        favorite = favorite.scalar_one_or_none()

        if user_id:
            favorite.user_id = user_id
        if content_id:
            favorite.content_id = content_id

        await self.db.commit()
        await self.db.refresh(favorite)
        return favorite

    async def delete(self, favorite_id: int):
        result = await self.db.execute(
            delete(Favorites).where(Favorites.favorite_id == favorite_id)
        )
        await self.db.commit()
        return result.rowcount > 0
