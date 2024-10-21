from database import AsyncSession
from models import ContentCountries

class ContentCountriesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_content_countries(self):
        content_countries = await self.db.execute(select(ContentCountries))
        return content_countries.scalar().all()

    async def get_content_country(self, content_country_id: int):
        content_country = await self.db.execute(
            select(ContentCountries).where(ContentCountries.content_country_id == content_country_id)
        )
        return content_country.scalar_one_or_none()

    async def create_content_country(self, content_id: int, country_id: int):
        new_content_country = ContentCountries(content_id=content_id, country_id=country_id)
        self.db.add(new_content_country)
        await self.db.commit()
        await self.db.refresh(new_content_country)
        return new_content_country

    async def update_content_country(self, content_country_id: int, content_id: int = None, country_id: int = None):
        content_country = await self.db.execute(
            select(ContentCountries).where(ContentCountries.content_country_id == content_country_id)
        )
        content_country = content_country.scalar_one_or_none()

        if content_id:
            content_country.content_id = content_id
        if country_id:
            content_country.country_id = country_id
        
        await self.db.commit()
        await self.db.refresh(content_country)
        return content_country

    async def delete_content_country(self, content_country_id: int):
        await self.db.execute(
            delete(ContentCountries).where(ContentCountries.content_country_id == content_country_id)
        )
        await self.db.commit()