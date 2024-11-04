from api_decorators import handle_exceptions
from repositories import ContentRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import ContentService
from responses.content import *

router = APIRouter(prefix="/contents", tags=["contents"])


@router.get("/", summary="Fetch all contents", responses=get_contents)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/contents
    """

    contents = await ContentService(ContentRepository(db)).get_all()
    return contents


@router.get("/{content_id}", summary="Fetch content by id", responses=get_content)
@handle_exceptions(status_code=400)
async def get_one(content_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/contents/1
    """

    content = await ContentService(ContentRepository(db)).get_one(content_id=content_id)
    return content


@router.post("/", summary="Create content", responses=create_content)
@handle_exceptions(status_code=400)
async def create(
    title: str,
    preview_path: str = None,
    description: str = None,
    release_date: str = None,
    content_type: str = None,
    content_path: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        POST /api/contents/
        {
            "content_id": 1,
            "title": "aaa",
            "preview_path": "/preview1.jpg",
            "description": "aaa",
            "release_date": "2002-10-11",
            "content_type": "Movie",
            "content_path": "/1"
        }
    """

    new_content = await ContentService(ContentRepository(db)).create(
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )

    return new_content


@router.put("/{content_id}", summary="Update content by id", responses=update_content)
@handle_exceptions(status_code=400)
async def update(
    content_id: int,
    title: str = None,
    preview_path: str = None,
    description: str = None,
    release_date: str = None,
    content_type: str = None,
    content_path: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/contents/1
        {
            "content_id": 1,
            "title": "aaa",
            "preview_path": "/preview1.jpg",
            "description": "bbb",
            "release_date": "2002-10-11",
            "content_type": "Movie",
            "content_path": "/1"
        }
    """

    content = await ContentService(ContentRepository(db)).update(
        content_id=content_id,
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )
    return content


@router.delete(
    "/{content_id}", summary="Delete content by id", responses=delete_content
)
@handle_exceptions(status_code=400)
async def delete(content_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/contents/1
    """

    await ContentService(ContentRepository(db)).delete(content_id=content_id)
    return {"message": "Content deleted successfully"}
