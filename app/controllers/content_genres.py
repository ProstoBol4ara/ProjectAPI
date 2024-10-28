from repositories import ContentGenresRepository
from api_decorators import handle_exceptions
from services import ContentGenresService
from database import AsyncSession, get_db
from responses.content_genres import *
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/content_genres",
    tags=["content_genres"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all content genres", responses=get_content_genres)
async def get_content_genres(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_genres
    """

    content_genres = await ContentGenresService(ContentGenresRepository(db)).get_content_genres()
    return content_genres

@handle_exceptions(status_code=400)
@router.get('/{content_genre_id}', summary="Fetch content genre by id", responses=get_content_genre)
async def get_content_genre(content_genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/content_genres/1
    """

    content_genre = await ContentGenresService(ContentGenresRepository(db)).get_content_genre(content_genre_id=content_genre_id)
    return content_genre

@handle_exceptions(status_code=400)
@router.post('/', summary="Create content genre", responses=create_content_genre)
async def create_content_genre(content_id: int, genres_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/content_genres/
        {
            "content_genre_id": 1,
            "content_id": 1,
            "genre_id": 1
        }
    """

    new_content_genre = await ContentGenresService(ContentGenresRepository(db)).create_content_genre(content_id=content_id, genres_id=genres_id)
    return new_content_genre

@handle_exceptions(status_code=400)
@router.put('/{content_genre_id}', summary="Update content genre by id", responses=update_content_genre)
async def update_content_genre(content_genre_id: int, content_id: int = None, genres_id: int = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/content_genres/1
        {
            "content_genre_id": 1,
            "genre_id": 2
        }
    """

    content_genre = await ContentGenresService(ContentGenresRepository(db)).update_content_genre(content_genre_id=content_genre_id, content_id=content_id, genres_id=genres_id)
    return content_genre

@handle_exceptions(status_code=400)
@router.delete('/{content_genre_id}', summary="Delete content genre by id", responses=delete_content_genre)
async def delete_content_genre(content_genre_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/content_genres/1
    """

    await ContentGenresService(ContentGenresRepository(db)).delete_content_genre(content_genre_id=content_genre_id)
    return {"message": "Content genre deleted successfully"}
