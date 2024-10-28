from repositories import FavoritesRepository

class FavoritesService:
    def __init__(self, favorites_repository: FavoritesRepository):
        self.favorites_repository = favorites_repository

    async def get_favorites(self):
        favorites = await self.favorites_repository.get_favorites()
        return None if favorites is None else \
            [{"favorite_id": favorite.favorite_id, "user_id": favorite.user_id, "content_id": favorite.content_id}
             for favorite in favorites]

    async def get_favorite(self, favorite_id: int):
        favorite = await self.favorites_repository.get_favorite(favorite_id=favorite_id)

        if not favorite: raise ValueError("Favorite not found")

        return {"favorite_id": favorite.favorite_id, "user_id": favorite.user_id, "content_id": favorite.content_id}

    async def create_favorite(self, user_id: int, content_id: int):
        new_favorite = await self.favorites_repository.create_favorite(user_id=user_id, content_id=content_id)
        return {"favorite_id": new_favorite.favorite_id, "user_id": new_favorite.user_id, "content_id": new_favorite.content_id}

    async def update_favorite(self, favorite_id: int, user_id: int = None, content_id = None):
        favorite = await self.favorites_repository\
            .update_favorite(favorite_id=favorite_id, user_id=user_id, content_id=content_id)

        if not favorite: raise ValueError("Favorite not found")

        return {"favorite_id": favorite.favorite_id, "user_id": favorite.user_id, "content_id": favorite.content_id}

    async def delete_favorite(self, favorite_id: int):
        if not await self.favorites_repository.delete_favorite(favorite_id=favorite_id):
            raise ValueError("Favorite not found")
