from repositories import CountriesRepository


class CountriesService:
    def __init__(self, repository: CountriesRepository):
        self.repository = repository

    async def get_all(self):
        countries = await self.repository.get_all()

        return (
            None
            if countries is None
            else [
                {"country_id": country.country_id, "country_name": country.country_name}
                for country in countries
            ]
        )

    async def get_one(self, country_id: int):
        if not country_id:
            raise ValueError("country_id cannot be empty")

        country = await self.repository.get_one(country_id=country_id)

        if not country:
            raise ValueError("Country not found")

        return {"country_id": country.country_id, "country_name": country.country_name}

    async def create(self, country_name: str):
        if not country_name:
            raise ValueError("country_name cannot be empty")

        new_country = await self.repository.create(country_name=country_name)
        return {
            "country_id": new_country.country_id,
            "country_name": new_country.country_name,
        }

    async def update(self, country_id: int, country_name: str = None):
        if not country_id:
            raise ValueError("country_id cannot be empty")

        country = await self.repository.update(
            country_id=country_id, country_name=country_name
        )

        if not country:
            raise ValueError("Country not found")

        return {"country_id": country.country_id, "country_name": country.country_name}

    async def delete(self, country_id: int):
        if not country_id:
            raise ValueError("country_id cannot be empty")

        if not (delete_country := await self.repository.delete(country_id=country_id)):
            raise ValueError("Country not found")
        return delete_country
