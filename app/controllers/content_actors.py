from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentActorsRepository
from services import ContentActorsService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/content_actors",
    tags=["content_actors"]
)

@router.get('/')
async def get_content_actors(db: AsyncSession = Depends(get_db)):
    content_actors = await ContentActorsService(ContentActorsRepository(db)).get_content_actors()
    if content_actors is None:
        raise HTTPException(status_code=400, detail="Сontent actors not found")
    return content_actors

@router.get('/{content_actor_id}')
async def get_content_actors(content_actor_id: int, db: AsyncSession = Depends(get_db)):
    content_actor = await ContentActorsService(ContentActorsRepository(db)).get_content_actor(content_actor_id=content_actor_id)
    if content_actor is None:
        raise HTTPException(status_code=400, detail="Content actor not found")
    return content_actor

@router.post('/')
async def create_content_actors(content_id: int, actor_id: int, role: str = None, db: AsyncSession = Depends(get_db)):
    try:
        new_content_actor = await ContentActorsService(ContentActorsRepository(db)).create_content_actors(content_id=content_id, actor_id=actor_id, role=role)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_actor

@router.put('/{content_actor_id}')
async def update_content_actors(content_actor_id: int, content_id: int = None, actor_id: int = None, role: str = None, db: AsyncSession = Depends(get_db)):
    try:
        content_actor = await ContentActorsService(ContentActorsRepository(db)).update_content_actors(content_actor_id=content_actor_id, content_id=content_id, actor_id=actor_id, role=role)
        if content_actor is None:
            raise HTTPException(status_code=400, detail="Content actor not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return content_actor

@router.delete('/{content_actor_id}')
async def delete_content_actors(content_actor_id: int, db: AsyncSession = Depends(get_db)):
    if not await ContentActorsService(ContentActorsRepository(db)).delete_content_actors(content_actor_id=content_actor_id):
        raise HTTPException(status_code=400, detail="Content actor not found")
    return {"message": "Сontent actor deleted successfully"}