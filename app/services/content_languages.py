from repositories import ContentLanguagesRepository

class ContentLanguagesService:
    def __init__(self, content_languages_repository: ContentLanguagesRepository):
        self.content_languages_repository = content_languages_repository

    async def get_content_languages(self):
        content_languages = await self.content_languages_repository.get_content_languages()
        return None if content_languages is None else [{"content_language_id": content_language.content_language_id, "content_id": content_language.content_id, "language_id": content_language.language_id} for content_language in content_languages]

    async def get_content_language(self, content_language_id: int):
        content_language = await self.content_languages_repository.get_content_language(content_language_id=content_language_id)
        return None if content_language is None else {"content_language_id": content_language.content_language_id, "content_id": content_language.content_id, "language_id": content_language.language_id}

    async def create_content_language(self, content_id: int, language_id: int):
        new_content_language = await self.content_languages_repository.create_content_language(content_id=content_id, language_id=language_id)
        return {"content_language_id": new_content_language.content_language_id, "content_id": new_content_language.content_id, "language_id": new_content_language.language_id}

    async def update_content_language(self, content_language_id: int, content_id: int = None, language_id: int = None):
        content_language = await self.content_languages_repository.update_content_language(content_language_id=content_language_id, content_id=content_id, language_id=language_id)
        return None if content_language is None else {"content_genre_id": content_language.content_genre_id, "content_id": content_language.content_id, "genres_id": content_language.genres_id}

    async def delete_content_language(self, content_language_id: int):
        return await self.content_languages_repository.delete_content_language(content_language_id=content_language_id)
