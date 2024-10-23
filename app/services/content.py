from repositories import ContentRepository

class ContentService:
    def __init__(self, content_repository: ContentRepository):
        self.content_repository = content_repository

    async def get_contents(self):
        contents = await self.content_repository.get_contents()
        return None if contents is None else [{"content_id": content.content_id, "title": content.title, "preview_path": content.preview_path, "description": content.description, "release_date": content.release_date, "content_type": content.content_type, "content_path": content.content_path} for content in contents]

    async def get_content(self, content_id: int):
        content = await self.content_repository.get_content(content_id=content_id)
        return None if content is None else {"content_id": content.content_id, "title": content.title, "preview_path": content.preview_path, "description": content.description, "release_date": content.release_date, "content_type": content.content_type, "content_path": content.content_path}

    async def create_content(self, title: str, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None):
        new_content = await self.content_repository.create_content(title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)
        return {"content_id": new_content.content_id, "title": new_content.title, "preview_path": new_content.preview_path, "description": new_content.description, "release_date": new_content.release_date, "content_type": new_content.content_type, "content_path": new_content.content_path}

    async def update_content(self, content_id: int, title: str = None, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None):
        content = await self.content_repository.update_content(content_id=content_id, title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)
        return None if content is None else {"content_id": content.content_id, "title": content.title, "preview_path": content.preview_path, "description": content.description, "release_date": content.release_date, "content_type": content.content_type, "content_path": content.content_path}

    async def delete_content(self, content_id: int):
        return await self.content_repository.delete_content(content_id=content_id)
    