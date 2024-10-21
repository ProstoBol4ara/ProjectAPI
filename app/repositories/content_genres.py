from database import AsyncSession
from models import ContentGenres

class ContentGenresRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_content_genres(self):
        content_genres = await self.db.execute(select(ContentGenres))
        return content_genres.scalar().all()

    async def get_content_genre(self, content_genre_id: int):
        content_genre = await self.db.execute(
            select(ContentGenres).filter(ContentGenres.content_genre_id == content_genre_id)
        )
        return content_genre.scalar_one_or_none()

    async def create_content_genre(self, content_id: int, genres_id: int):
        new_content_genre = ContentGenres(content_id=content_id, genres_id=genres_id)
        self.db.add(new_content_genre)
        await self.db.commit()
        await self.db.refresh(new_content_genre)
        return new_content_genre

    async def update_content_genre(self, content_genre_id: int, content_id: int = None, genres_id: int = None):
        content_genre = await self.db.execute(
            select(ContentGenres).filter(ContentGenres.content_genre_id == content_genre_id)
        )
        content_genre = content_genre.scalar_one_or_none()

        if content_id:
            content_genre.email = content_id
        if genres_id:
            content_genre.genres_id = genres_id

        await self.db.commit()
        await self.db.refresh(content_genre)
        return content_genre

    async def delete_content_genre(self, content_genre_id: int):
        await self.db.execute(
            delete(ContentGenres).where(ContentGenres.content_genre_id == content_genre_id)
        )
        await self.db.commit()
