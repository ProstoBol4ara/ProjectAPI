from repositories import CountriesRepository

class CountriesService:
    def __init__(self, countries_repository: CountriesRepository):
        self.countries_repository = countries_repository

    async def get_countries(self):
        return await self.countries_repository.get_countries()

    async def get_country(self, country_id: int):
        return await self.countries_repository.get_country(country_id=country_id)

    async def create_country(self, country_name: str):
        return await self.countries_repository.create_country(country_name=country_name)

    async def update_country(self, country_id: int, country_name: str = None):
        return await self.countries_repository.update_country(country_id=country_id, country_name=country_name)

    async def delete_country(self, country_id: int):
        await self.countries_repository.delete_country(country_id=country_id)