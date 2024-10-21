from repositories import ContentRepository

class ContentService:
    def __init__(self, content_repository: ContentRepository):
        self.content_repository = content_repository

    async def get_contents(self):
        return await self.content_repository.get_contents()

    async def get_content(self, content_id: int):
        return await self.content_repository.get_content(content_id=content_id)

    async def create_content(self, title: str, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None):
        return await self.content_repository.create_content(title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)

    async def update_content(self, content_id: int, title: str = None, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None):
        return await self.content_repository.update_content(content_id=content_id, title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)

    async def delete_content(self, content_id: int):
        await self.content_repository.delete_content(content_id=content_id)
    