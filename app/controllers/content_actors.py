from fastapi import APIRouter, HTTPException, Depends
from repositories import ContentActorsRepository
from services import ContentActorsService
from database import AsyncSession, get_db
from responses.content_actors import *

router = APIRouter(
    prefix="/content_actors",
    tags=["content_actors"]
)

@router.get('/', summary="Fetch all content actors", responses=get_content_actors)
async def get_content_actors(db: AsyncSession = Depends(get_db)):
    """
    Query example:
        
        GET /api/content_actors
    """

    content_actors = await ContentActorsService(ContentActorsRepository(db)).get_content_actors()
    if content_actors is None:
        raise HTTPException(status_code=400, detail="Сontent actors not found")
    return content_actors

@router.get('/{content_actor_id}', summary="Fetch content actor by id", responses=get_content_actor)
async def get_content_actors(content_actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_actors/1
    """    
    
    content_actor = await ContentActorsService(ContentActorsRepository(db)).get_content_actor(content_actor_id=content_actor_id)
    if content_actor is None:
        raise HTTPException(status_code=400, detail="Content actor not found")
    return content_actor

@router.post('/', summary="Create content actor", responses=create_content_actor)
async def create_content_actors(content_id: int, actor_id: int, role: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/content_actors/
        {
            "content_actor_id": 1, 
            "content_id": 1, 
            "actor_id": 1, 
            "role": "Loser"
        }
    """    
    
    try:
        new_content_actor = await ContentActorsService(ContentActorsRepository(db)).create_content_actors(content_id=content_id, actor_id=actor_id, role=role)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_content_actor

@router.put('/{content_actor_id}', summary="Update content actor by id", responses=update_content_actor)
async def update_content_actors(content_actor_id: int, content_id: int = None, actor_id: int = None, role: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/content_actors/1
        {
            "content_actor_id": 1, 
            "content_id": 2, 
        }
    """

    try:
        content_actor = await ContentActorsService(ContentActorsRepository(db)).update_content_actors(content_actor_id=content_actor_id, content_id=content_id, actor_id=actor_id, role=role)
        if content_actor is None:
            raise HTTPException(status_code=400, detail="Content actor not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return content_actor

@router.delete('/{content_actor_id}', summary="Delete content actor by id", responses=delete_content_actor)
async def delete_content_actors(content_actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_actors/1
    """

    if not await ContentActorsService(ContentActorsRepository(db)).delete_content_actors(content_actor_id=content_actor_id):
        raise HTTPException(status_code=400, detail="Content actor not found")
    return {"message": "Сontent actor deleted successfully"}