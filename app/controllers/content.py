from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentRepository
from database import AsyncSession, get_db
from services import ContentService
from responses.content import *

router = APIRouter(
    prefix="/contents",
    tags=["contents"]
)

@router.get('/', summary="Fetch all contents", responses=get_contents)
async def get_contents(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/contents
    """

    contents = await ContentService(ContentRepository(db)).get_contents()
    if contents is None:
        raise HTTPException(status_code=400, detail="Contents not found")
    return contents

@router.get('/{content_id}', summary="Fetch content by id", responses=get_content)
async def get_content(content_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/contents/1
    """

    content = await ContentService(ContentRepository(db)).get_content(content_id=content_id)
    if content is None:
        raise HTTPException(status_code=400, detail="Content not found")
    return content

@router.post('/', summary="Create content", responses=create_content)
async def create_content(title: str, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None, db: AsyncSession = Depends(get_db)):
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

    try:
        new_content = await ContentService(ContentRepository(db)).create_content(title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content

@router.put('/{content_id}', summary="Update content by id", responses=update_content)
async def update_content(content_id: int, title: str = None, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None, db: AsyncSession = Depends(get_db)):
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

    content = await ContentService(ContentRepository(db)).update_content(content_id=content_id, title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)
    if content is None:
        raise HTTPException(status_code=400, detail="Content not found")
    return content

@router.delete('/{content_id}', summary="Delete content by id", responses=delete_content)
async def delete_content(content_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/contents/1
    """

    if not await ContentService(ContentRepository(db)):
        raise HTTPException(status_code=400, detail="Content not found")
    return {"message": "Content deleted successfully"}
