from repositories import FavoritesRepository


class FavoritesService:
    def __init__(self, repository: FavoritesRepository):
        self.repository = repository

    async def get_all(self):
        favorites = await self.repository.get_all()

        return (
            None
            if favorites is None
            else [
                {
                    "favorite_id": favorite.favorite_id,
                    "user_id": favorite.user_id,
                    "content_id": favorite.content_id,
                }
                for favorite in favorites
            ]
        )

    async def get_one(self, favorite_id: int):
        if not favorite_id:
            raise ValueError("favorite_id cannot be empty")

        favorite = await self.repository.get_one(favorite_id=favorite_id)

        if not favorite:
            raise ValueError("Favorite not found")

        return {
            "favorite_id": favorite.favorite_id,
            "user_id": favorite.user_id,
            "content_id": favorite.content_id,
        }

    async def create(self, user_id: int, content_id: int):
        if not user_id or not content_id:
            raise ValueError("user_id and content_id cannot be empty")

        new_favorite = await self.repository.create(
            user_id=user_id, content_id=content_id
        )
        return {
            "favorite_id": new_favorite.favorite_id,
            "user_id": new_favorite.user_id,
            "content_id": new_favorite.content_id,
        }

    async def update(self, favorite_id: int, user_id: int = None, content_id=None):
        if not favorite_id:
            raise ValueError("favorite_id cannot be empty")

        favorite = await self.repository.update(
            favorite_id=favorite_id, user_id=user_id, content_id=content_id
        )

        if not favorite:
            raise ValueError("Favorite not found")

        return {
            "favorite_id": favorite.favorite_id,
            "user_id": favorite.user_id,
            "content_id": favorite.content_id,
        }

    async def delete(self, favorite_id: int):
        if not favorite_id:
            raise ValueError("favorite_id cannot be empty")

        if not (
            delete_favorite := await self.repository.delete(favorite_id=favorite_id)
        ):
            raise ValueError("Favorite not found")
        return delete_favorite
