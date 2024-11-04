from database import AsyncSession, select, delete
from models import Languages


class LanguagesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        languages = await self.db.execute(select(Languages))
        return languages.scalars().all()

    async def get_one(self, language_id: int):
        language = await self.db.execute(
            select(Languages).where(Languages.language_id == language_id)
        )
        return language.scalar_one_or_none()

    async def create(self, language_name: str):
        new_language = Languages(language_name=language_name)
        self.db.add(new_language)
        await self.db.commit()
        await self.db.refresh(new_language)
        return new_language

    async def update(self, language_id: int, language_name: str = None):
        language = await self.db.execute(
            select(Languages).where(Languages.language_id == language_id)
        )
        language = language.scalar_one_or_none()

        if language_name:
            language.language_name = language_name

        await self.db.commit()
        await self.db.refresh(language)
        return {"language_id": language.language_id, "name": language.language_name}

    async def delete(self, language_id: int):
        result = await self.db.execute(
            delete(Languages).where(Languages.language_id == language_id)
        )
        await self.db.commit()
        return result.rowcount > 0
