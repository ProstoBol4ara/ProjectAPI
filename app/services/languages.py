from repositories import LanguagesRepository


class LanguagesService:
    def __init__(self, repository: LanguagesRepository):
        self.repository = repository

    async def get_all(self):
        languages = await self.repository.get_all()

        return (
            None
            if languages is None
            else [
                {
                    "language_id": language.language_id,
                    "language_name": language.language_name,
                }
                for language in languages
            ]
        )

    async def get_one(self, language_id: int):
        if not language_id:
            raise ValueError("language_id cannot be empty")

        language = await self.repository.get_one(language_id=language_id)

        if not language:
            raise ValueError("Language not found")

        return (
            None
            if language is None
            else {
                "language_id": language.language_id,
                "language_name": language.language_name,
            }
        )

    async def create(self, language_name: str):
        if not language_name:
            raise ValueError("language_name cannot be empty")

        new_language = await self.repository.create(language_name=language_name)
        return {
            "language_id": new_language.language_id,
            "language_name": new_language.language_name,
        }

    async def update(self, language_id: int, language_name: str = None):
        if not language_id:
            raise ValueError("language_id cannot be empty")

        language = await self.repository.update(
            language_id=language_id, language_name=language_name
        )

        if not language:
            raise ValueError("Language not found")

        return (
            None
            if language is None
            else {
                "language_id": language.language_id,
                "language_name": language.language_name,
            }
        )

    async def delete(self, language_id: int):
        if not language_id:
            raise ValueError("language_id cannot be empty")

        if not (
            delete_language := await self.repository.delete(language_id=language_id)
        ):
            raise ValueError("Language not found")
        return delete_language
