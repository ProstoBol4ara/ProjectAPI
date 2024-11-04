from repositories import ContentLanguagesRepository


class ContentLanguagesService:
    def __init__(self, repository: ContentLanguagesRepository):
        self.repository = repository

    async def get_all(self):
        content_languages = await self.repository.get_all()

        return (
            None
            if content_languages is None
            else [
                {
                    "content_language_id": content_language.content_language_id,
                    "content_id": content_language.content_id,
                    "language_id": content_language.language_id,
                }
                for content_language in content_languages
            ]
        )

    async def get_one(self, content_language_id: int):
        if not content_language_id:
            raise ValueError("content_language_id cannot be empty")

        content_language = await self.repository.get_one(
            content_language_id=content_language_id
        )

        if not content_language:
            raise ValueError("Content language not found")

        return {
            "content_language_id": content_language.content_language_id,
            "content_id": content_language.content_id,
            "language_id": content_language.language_id,
        }

    async def create(self, content_id: int, language_id: int):
        if not content_id or not language_id:
            raise ValueError("content_id and language_id cannot be empty")

        new_content_language = await self.repository.create(
            content_id=content_id, language_id=language_id
        )

        return {
            "content_language_id": new_content_language.content_language_id,
            "content_id": new_content_language.content_id,
            "language_id": new_content_language.language_id,
        }

    async def update(
        self, content_language_id: int, content_id: int = None, language_id: int = None
    ):
        if not content_language_id:
            raise ValueError("content_language_id cannot be empty")

        content_language = await self.repository.update(
            content_language_id=content_language_id,
            content_id=content_id,
            language_id=language_id,
        )

        if not content_language:
            raise ValueError("Content language not found")

        return {
            "content_language_id": content_language.content_language_id,
            "content_id": content_language.content_id,
            "language_id": content_language.language_id,
        }

    async def delete(self, content_language_id: int):
        if not content_language_id:
            raise ValueError("content_language_id cannot be empty")

        if not (
            delete_content_language := await self.repository.delete(
                content_language_id=content_language_id
            )
        ):
            raise ValueError("Content language not found")
        return delete_content_language
