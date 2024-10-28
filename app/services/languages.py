from repositories import LanguagesRepository

class LanguagesService:
    def __init__(self, languages_repository: LanguagesRepository):
        self.languages_repository = languages_repository

    async def get_languages(self):
        languages = await self.languages_repository.get_languages()
        return None if languages is None else [{"language_id": language.language_id, "name": language.language_name} for language in languages]

    async def get_language(self, language_id: int):
        language = await self.languages_repository.get_language(language_id=language_id)
        return None if language is None else {"language_id": language.language_id, "name": language.language_name}

    async def create_language(self, language_name: str):
        new_language = await self.languages_repository.create_language(language_name=language_name)
        return {"language_id": new_language.language_id, "name": new_language.language_name}

    async def update_language(self, language_id: int, language_name: str = None):
        language = await self.languages_repository.update_language(language_id=language_id, language_name=language_name)
        return None if language is None else {"language_id": language.language_id, "name": language.language_name}

    async def delete_language(self, language_id: int):
        return await self.languages_repository.delete_language(language_id=language_id)
