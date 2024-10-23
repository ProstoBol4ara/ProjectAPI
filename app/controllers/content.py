from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentRepository
from database import AsyncSession, get_db
from services import ContentService

router = APIRouter(
    prefix="/contents",
    tags=["contents"]
)

@router.get('/')
async def get_contents(db: AsyncSession = Depends(get_db)):
    contents = await ContentService(ContentRepository(db)).get_contents()
    if contents is None:
        raise HTTPException(status_code=400, detail="Contents not found")
    return contents

@router.get('/{content_id}')
async def get_content(content_id: int, db: AsyncSession = Depends(get_db)):
    content = await ContentService(ContentRepository(db)).get_content(content_id=content_id)
    if content is None:
        raise HTTPException(status_code=400, detail="Content not found")
    return content

@router.post('/')
async def create_content(title: str, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None, db: AsyncSession = Depends(get_db)):
    try:
        new_content = await ContentService(ContentRepository(db)).create_content(title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content

@router.put('/{content_id}')
async def update_content(content_id: int, title: str = None, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None, db: AsyncSession = Depends(get_db)):
    content = await ContentService(ContentRepository(db)).update_content(content_id=content_id, title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)
    if content is None:
        raise HTTPException(status_code=400, detail="Content not found")
    return content

@router.delete('/{content_id}')
async def delete_content(content_id: int, db: AsyncSession = Depends(get_db)):
    if not await ContentService(ContentRepository(db)):
        raise HTTPException(status_code=400, detail="Content not found")
    return {"message": "Content deleted successfully"}