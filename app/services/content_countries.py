from repositories import ContentCountriesRepository

class ContentCountriesService:
    def __init__(self, content_countries_repository: ContentCountriesRepository):
        self.content_countries_repository = content_countries_repository

    async def get_content_countries(self):
        content_countries = await self.content_countries_repository.get_content_countries()
        return None if content_countries is None else [{"content_country_id": content_country.content_actor_id, "content_id": content_country.content_id, "country_id": content_country.country_id} for content_country in content_countries]

    async def get_content_country(self, content_country_id: int):
        content_country = await self.content_countries_repository.get_content_country(content_country_id=content_country_id)
        return None if content_country is None else {"content_country_id": content_country.content_actor_id, "content_id": content_country.content_id, "country_id": content_country.country_id}

    async def create_content_country(self, content_id: int, country_id: int):
        new_content_country = await self.content_countries_repository.create_content_country(content_id=content_id, country_id=country_id)
        return {"content_country_id": new_content_country.content_country_id, "content_id": new_content_country.content_id, "country_id": new_content_country.country_id}

    async def update_content_country(self, content_country_id: int, content_id: int = None, country_id: int = None):
        content_country = await self.content_countries_repository.update_content_country(content_country_id=content_country_id, content_id=content_id, country_id=country_id)
        return None if content_country is None else {"content_country_id": content_country.content_country_id, "content_id": content_countrie.content_id, "country_id": content_countrie.country_id}

    async def delete_content_country(self, content_country_id: int):
        return await self.content_countries_repository.delete_content_country(content_country_id=content_country_id)
    