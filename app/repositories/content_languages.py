from database import AsyncSession, select, delete
from models import ContentLanguages

class ContentLanguagesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_content_languages(self):
        content_languages = await self.db.execute(select(ContentLanguages))
        return content_languages.scalars().all()

    async def get_content_language(self, content_language_id: int):
        content_language = await self.db.execute(
            select(ContentLanguages).where(ContentLanguages.content_language_id == content_language_id)
        )
        return content_language.scalar_one_or_none()

    async def create_content_language(self, content_id: int, language_id: int):
        new_content_language = ContentLanguages(content_id=content_id, language_id=language_id)
        self.db.add(new_content_language)
        await self.db.commit()
        await self.db.refresh(new_content_language)
        return new_content_language

    async def update_content_language(self, content_language_id: int, content_id: int = None, language_id: int = None):
        content_language = await self.db.execute(
            select(ContentLanguages).where(ContentLanguages.content_language_id == content_language_id)
        )
        content_language = content_language.scalar_one_or_none()

        if content_id:
            content_language.email = content_id
        if language_id:
            content_language.language_id = language_id

        await self.db.commit()
        await self.db.refresh(content_language)
        return content_language

    async def delete_content_language(self, content_language_id: int):
        result = await self.db.execute(
            delete(ContentLanguages).where(ContentLanguages.content_language_id == content_language_id)
        )
        await self.db.commit()
        return result.rowcount > 0
