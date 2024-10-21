from repositories import LanguagesRepository

class LanguagesService:
    def __init__(self, languages_repository: LanguagesRepository):
        self.languages_repository = languages_repository

    async def get_languages(self):
        return await self.languages_repository.get_languages()

    async def get_language(self, language_id: int):
        return await self.languages_repository.get_language(language_id=language_id)

    async def create_language(self, language_name: str):
        return await self.languages_repository.create_language(language_name=language_name)

    async def update_language(self, language_id: int, language_name: str = None):
        return await self.languages_repository.update_language(language_id=language_id, language_name=language_name)

    async def delete_language(self, language_id: int):
        await self.languages_repository.delete_language(language_id=language_id)