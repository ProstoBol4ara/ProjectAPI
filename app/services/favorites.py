from repositories import FavoritesRepository

class FavoritesService:
    def __init__(self, favorites_repository: FavoritesRepository):
        self.favorites_repository = favorites_repository

    async def get_favorites(self):
        return await self.favorites_repository.get_favorites()

    async def get_favorite(self, favorite_id: int):
        return await self.favorites_repository.get_favorite(favorite_id=favorite_id)

    async def create_favorite(self, user_id: int, content_id: int):
        return await self.favorites_repository.create_favorite(user_id=user_id, content_id=content_id)

    async def update_favorite(self, favorite_id: int, user_id: int = None, content_id = None):
        return await self.favorites_repository.update_favorite(favorite_id=favorite_id, user_id=user_id, content_id=content_id)

    async def delete_favorite(self, favorite_id: int):
        await self.favorites_repository.delete_favorite(favorite_id=favorite_id)
    