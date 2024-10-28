from repositories import ContentActorsRepository
from api_decorators import handle_exceptions
from services import ContentActorsService
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from responses.content_actors import *

router = APIRouter(
    prefix="/content_actors",
    tags=["content_actors"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all content actors", responses=get_content_actors)
async def get_content_actors(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_actors
    """

    content_actors = await ContentActorsService(ContentActorsRepository(db)).get_content_actors()
    return content_actors

@handle_exceptions(status_code=400)
@router.get('/{content_actor_id}', summary="Fetch content actor by id", responses=get_content_actor)
async def get_content_actors(content_actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_actors/1
    """

    content_actor = await ContentActorsService(ContentActorsRepository(db)).get_content_actor(content_actor_id=content_actor_id)
    return content_actor

@handle_exceptions(status_code=400)
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

    new_content_actor = await ContentActorsService(ContentActorsRepository(db)).create_content_actors(content_id=content_id, actor_id=actor_id, role=role)
    return new_content_actor

@handle_exceptions(status_code=400)
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

    content_actor = await ContentActorsService(ContentActorsRepository(db)).update_content_actors(content_actor_id=content_actor_id, content_id=content_id, actor_id=actor_id, role=role)
    return content_actor

@handle_exceptions(status_code=400)
@router.delete('/{content_actor_id}', summary="Delete content actor by id", responses=delete_content_actor)
async def delete_content_actors(content_actor_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_actors/1
    """

    await ContentActorsService(ContentActorsRepository(db)).delete_content_actors(content_actor_id=content_actor_id)
    return {"message": "Сontent actor deleted successfully"}
