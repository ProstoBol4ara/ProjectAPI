from database import AsyncSession, select, delete
from models import Genres

class GenresRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_genres(self):
        genres = await self.db.execute(select(Genres))
        return genres.scalars().all()

    async def get_genre(self, genre_id: int):
        genre = await self.db.execute(
            select(Genres).where(Genres.genre_id == genre_id)
        )
        return genre.scalar_one_or_none()

    async def create_genre(self, genre_name: str):
        new_genre = Genres(genre_name=genre_name)
        self.db.add(new_genre)
        await self.db.commit()
        await self.db.refresh(new_genre)
        return new_genre

    async def update_genre(self, genre_id: int, genre_name: str = None):
        genre = await self.db.execute(
            select(Genres).where(Genres.genre_id == genre_id)
        )
        genre = genre.scalar_one_or_none()

        if genre_name:
            genre.genre_name = genre_name

        await self.db.commit()
        await self.db.refresh(genre)
        return genre

    async def delete_genre(self, genre_id: int):
        result = await self.db.execute(
            delete(Genres).where(Genres.genre_id == genre_id)
        )
        await self.db.commit()
        return result.rowcount > 0
