from repositories import CountriesRepository

class CountriesService:
    def __init__(self, countries_repository: CountriesRepository):
        self.countries_repository = countries_repository

    async def get_countries(self):
        countries = await self.countries_repository.get_countries()
        return None if countries is None else [{"country_id": country.country_id, "country_name": country.country_name} for country in countries]

    async def get_country(self, country_id: int):
        country = await self.countries_repository.get_country(country_id=country_id)
        return None if country is None else {"country_id": country.country_id, "country_name": country.country_name}
    
    async def create_country(self, country_name: str):
        new_country = await self.countries_repository.create_country(country_name=country_name)
        return {"country_id": new_country.country_id, "country_name": new_country.country_name}
    
    async def update_country(self, country_id: int, country_name: str = None):
        country = await self.countries_repository.update_country(country_id=country_id, country_name=country_name)
        return None if country is None else {"country_id": country.country_id, "country_name": country.country_name}

    async def delete_country(self, country_id: int):
        return await self.countries_repository.delete_country(country_id=country_id)