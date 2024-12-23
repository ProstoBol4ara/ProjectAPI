from database import AsyncSession, select, delete
from models import ContentCountries


class ContentCountriesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        content_countries = await self.db.execute(select(ContentCountries))
        return content_countries.scalars().all()

    async def get_one(self, content_country_id: int):
        content_country = await self.db.execute(
            select(ContentCountries).where(
                ContentCountries.content_country_id == content_country_id
            )
        )
        return content_country.scalar_one_or_none()

    async def create(self, content_id: int, country_id: int):
        new_content_country = ContentCountries(
            content_id=content_id, country_id=country_id
        )
        self.db.add(new_content_country)
        await self.db.commit()
        await self.db.refresh(new_content_country)
        return new_content_country

    async def update(
        self, content_country_id: int, content_id: int = None, country_id: int = None
    ):
        content_country = await self.db.execute(
            select(ContentCountries).where(
                ContentCountries.content_country_id == content_country_id
            )
        )
        content_country = content_country.scalar_one_or_none()

        if content_id:
            content_country.content_id = content_id
        if country_id:
            content_country.country_id = country_id

        await self.db.commit()
        await self.db.refresh(content_country)
        return content_country

    async def delete(self, content_country_id: int):
        result = await self.db.execute(
            delete(ContentCountries).where(
                ContentCountries.content_country_id == content_country_id
            )
        )
        await self.db.commit()
        return result.rowcount > 0
