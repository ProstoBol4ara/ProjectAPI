from repositories import ContentLanguagesRepository

class ContentLanguagesService:
    def __init__(self, content_languages_repository: ContentLanguagesRepository):
        self.content_languages_repository = content_languages_repository

    async def get_content_languages(self):
        return await self.content_languages_repository.get_content_languages()

    async def get_content_language(self, content_language_id: int):
        return await self.content_languages_repository.get_content_language(content_language_id=content_language_id)

    async def create_content_language(self, content_id: int, language_id: int):
        return await self.content_languages_repository.create_content_language(content_id=content_id, language_id=language_id)

    async def update_content_language(self, content_language_id: int, content_id: int = None, language_id: int = None):
        return await self.content_languages_repository.update_content_language(content_language_id=content_language_id, content_id=content_id, language_id=language_id)

    async def delete_content_language(self, content_language_id: int):
        await self.content_languages_repository.delete_content_language(content_language_id=content_language_id)
    