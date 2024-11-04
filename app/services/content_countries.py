from repositories import ContentCountriesRepository


class ContentCountriesService:
    def __init__(self, repository: ContentCountriesRepository):
        self.repository = repository

    async def get_all(self):
        content_countries = await self.repository.get_all()

        return (
            None
            if content_countries is None
            else [
                {
                    "content_country_id": content_country.content_country_id,
                    "content_id": content_country.content_id,
                    "country_id": content_country.country_id,
                }
                for content_country in content_countries
            ]
        )

    async def get_one(self, content_country_id: int):
        if not content_country_id:
            raise ValueError("content_country_id cannot be empty")

        content_country = await self.repository.get_one(
            content_country_id=content_country_id
        )

        if not content_country:
            raise ValueError("Content country not found")

        return {
            "content_country_id": content_country.content_country_id,
            "content_id": content_country.content_id,
            "country_id": content_country.country_id,
        }

    async def create(self, content_id: int, country_id: int):
        if not content_id or not content_id:
            raise ValueError("content_id and country_id cannot be empty")

        new_content_country = await self.repository.create(
            content_id=content_id, country_id=country_id
        )

        return {
            "content_country_id": new_content_country.content_country_id,
            "content_id": new_content_country.content_id,
            "country_id": new_content_country.country_id,
        }

    async def update(
        self, content_country_id: int, content_id: int = None, country_id: int = None
    ):
        if not content_country_id:
            raise ValueError("content_country_id cannot be empty")

        content_country = await self.repository.update(
            content_country_id=content_country_id,
            content_id=content_id,
            country_id=country_id,
        )

        if not content_country:
            raise ValueError("Content country not found")

        return {
            "content_country_id": content_country.content_country_id,
            "content_id": content_country.content_id,
            "country_id": content_country.country_id,
        }

    async def delete(self, content_country_id: int):
        if not content_country_id:
            raise ValueError("content_country_id cannot be empty")

        if not (
            delete_content_country := await self.repository.delete(
                content_country_id=content_country_id
            )
        ):
            raise ValueError("Content country not found")
        return delete_content_country
