from repositories import ContentDirectorsRepository
from api_decorators import handle_exceptions
from services import ContentDirectorsService
from database import AsyncSession, get_db
from responses.content_directors import *
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/content_directors", tags=["content_directors"])


@router.get("/", summary="Fetch all content directors", responses=get_content_directors)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_directors
    """

    content_directors = await ContentDirectorsService(
        ContentDirectorsRepository(db)
    ).get_all()
    return content_directors


@router.get(
    "/{content_director_id}",
    summary="Fetch content director by id",
    responses=get_content_director,
)
@handle_exceptions(status_code=400)
async def get_one(content_director_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_directors/1
    """

    content_director = await ContentDirectorsService(
        ContentDirectorsRepository(db)
    ).get_one(content_director_id=content_director_id)

    return content_director


@router.post("/", summary="Create content director", responses=create_content_director)
@handle_exceptions(status_code=400)
async def create(content_id: int, director_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/content_directors/
        {
            "content_director_id": 1,
            "content_id": 1,
            "director_id": 1
        }
    """

    new_content_director = await ContentDirectorsService(
        ContentDirectorsRepository(db)
    ).create(content_id=content_id, director_id=director_id)

    return new_content_director


@router.put(
    "/{content_director_id}",
    summary="Update content director by id",
    responses=update_content_director,
)
@handle_exceptions(status_code=400)
async def update(
    content_director_id: int,
    content_id: int = None,
    director_id: int = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/content_directors/1
        {
            "content_director_id": 1,
            "director_id": 2
        }
    """

    content_director = await ContentDirectorsService(
        ContentDirectorsRepository(db)
    ).update(
        content_director_id=content_director_id,
        content_id=content_id,
        director_id=director_id,
    )

    return content_director


@router.delete(
    "/{content_director_id}",
    summary="Delete content director by id",
    responses=delete_content_director,
)
@handle_exceptions(status_code=400)
async def delete(content_director_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_directors/1
    """

    await ContentDirectorsService(ContentDirectorsRepository(db)).delete(
        content_director_id=content_director_id
    )
    return {"message": "Content director deleted successfully"}
