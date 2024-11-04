from database import AsyncSession, select, delete
from datetime import datetime
from models import Content


class ContentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        contents = await self.db.execute(select(Content))
        return contents.scalars().all()

    async def get_one(self, content_id: int):
        content = await self.db.execute(
            select(Content).where(Content.content_id == content_id)
        )
        return content.scalar_one_or_none()

    async def create(
        self,
        title: str,
        preview_path: str = None,
        description: str = None,
        release_date: str = None,
        content_type: str = None,
        content_path: str = None,
    ):

        if not release_date is None:
            release_date = datetime.strptime(release_date, "%d.%m.%Y").date()

        new_content = Content(
            title=title,
            preview_path=preview_path,
            description=description,
            release_date=release_date,
            content_type=content_type,
            content_path=content_path,
        )

        self.db.add(new_content)
        await self.db.commit()
        await self.db.refresh(new_content)
        return new_content

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

        content = await self.db.execute(
            select(Content).where(Content.content_id == content_id)
        )

        content = content.scalar_one_or_none()

        if title:
            content.title = title
        if preview_path:
            content.preview_path = preview_path
        if description:
            content.description = description
        if release_date:
            content.release_date = datetime.strptime(release_date, "%d.%m.%Y").date()
        if content_type:
            content.content_type = content_type
        if content_path:
            content.content_path = content_path

        await self.db.commit()
        await self.db.refresh(content)
        return content

    async def delete(self, content_id: int):
        result = await self.db.execute(
            delete(Content).where(Content.content_id == content_id)
        )
        await self.db.commit()
        return result.rowcount > 0
