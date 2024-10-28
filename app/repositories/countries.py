from database import AsyncSession, select, delete
from models import Countries

class CountriesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_countries(self):
        countries = await self.db.execute(select(Countries))
        return countries.scalars().all()

    async def get_country(self, country_id: int):
        country = await self.db.execute(
            select(Countries).where(Countries.country_id == country_id)
        )
        return country.scalar_one_or_none()

    async def create_country(self, country_name: str):
        new_country = Countries(country_name=country_name)
        self.db.add(new_country)
        await self.db.commit()
        await self.db.refresh(new_country)
        return new_country

    async def update_country(self, country_id: int, country_name: str = None):
        country = await self.db.execute(
            select(Countries).where(Countries.country_id == country_id)
        )
        country = country.scalar_one_or_none()

        if country_name:
            country.country_name = country_name

        await self.db.commit()
        await self.db.refresh(country)
        return country

    async def delete_country(self, country_id: int):
        result = await self.db.execute(
            delete(Countries).where(Countries.country_id == country_id)
        )
        await self.db.commit()
        return result.rowcount > 0
