from repositories import ContentRepository
from constants import date_pattern
from re import match


class ContentService:
    def __init__(self, repository: ContentRepository):
        self.repository = repository

    async def get_all(self):
        contents = await self.repository.get_all()

        return (
            None
            if contents is None
            else [
                {
                    "content_id": content.content_id,
                    "title": content.title,
                    "preview_path": content.preview_path,
                    "description": content.description,
                    "release_date": content.release_date,
                    "content_type": content.content_type,
                    "content_path": content.content_path,
                }
                for content in contents
            ]
        )

    async def get_one(self, content_id: int):
        if not content_id:
            raise ValueError("content_id cannot be empty")

        content = await self.repository.get_one(content_id=content_id)

        if not content:
            raise ValueError("Content not found")

        return {
            "content_id": content.content_id,
            "title": content.title,
            "preview_path": content.preview_path,
            "description": content.description,
            "release_date": content.release_date,
            "content_type": content.content_type,
            "content_path": content.content_path,
        }

    async def create(
        self,
        title: str,
        preview_path: str = None,
        description: str = None,
        release_date: str = None,
        content_type: str = None,
        content_path: str = None,
    ):

        if not title:
            raise ValueError("title cannot be empty")

        if not release_date or not match(date_pattern, release_date):
            raise ValueError("Invalid release_date! Date format: day.month.year")

        if content_type not in ["Movie", "TV Show", "Documentary"]:
            raise ValueError(
                "Invalid content_type! content_type: Movie or TV Show or Documentary"
            )

        new_content = await self.repository.create(
            title=title,
            preview_path=preview_path,
            description=description,
            release_date=release_date,
            content_type=content_type,
            content_path=content_path,
        )

        return {
            "content_id": new_content.content_id,
            "title": new_content.title,
            "preview_path": new_content.preview_path,
            "description": new_content.description,
            "release_date": new_content.release_date,
            "content_type": new_content.content_type,
            "content_path": new_content.content_path,
        }

    async def update(
        self,
        content_id: int,
        title: str = None,
        preview_path: str = None,
        description: str = None,
        release_date: str = None,
        content_type: str = None,
        content_path: str = None,
    ):

        if not content_id:
            raise ValueError("content_id cannot be empty")

        if not release_date or not match(date_pattern, release_date):
            raise ValueError("Invalid release_date! Date format: day.month.year")

        content = await self.repository.update(
            content_id=content_id,
            title=title,
            preview_path=preview_path,
            description=description,
            release_date=release_date,
            content_type=content_type,
            content_path=content_path,
        )

        if not content:
            raise ValueError("Content not found")

        return {
            "content_id": content.content_id,
            "title": content.title,
            "preview_path": content.preview_path,
            "description": content.description,
            "release_date": content.release_date,
            "content_type": content.content_type,
            "content_path": content.content_path,
        }

    async def delete(self, content_id: int):
        if not content_id:
            raise ValueError("content_id cannot be empty")

        if not (delete_content := await self.repository.delete(content_id=content_id)):
            raise ValueError("Content not found")
        return delete_content
