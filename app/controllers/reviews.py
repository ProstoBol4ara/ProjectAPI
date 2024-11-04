from api_decorators import handle_exceptions
from repositories import ReviewsRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import ReviewsService
from responses.reviews import *

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.get("/", summary="Fetch all reviews", responses=get_reviews)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/reviews
    """

    reviews = await ReviewsService(ReviewsRepository(db)).get_all()
    return reviews


@router.get("/{review_id}", summary="Fetch review by id", responses=get_review)
@handle_exceptions(status_code=400)
async def get_review(review_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/reviews/1
    """

    review = await ReviewsService(ReviewsRepository(db)).get_one(review_id=review_id)
    return review


@router.post("/", summary="Create review", responses=create_review)
@handle_exceptions(status_code=400)
async def create(
    content_id: int,
    user_id: int,
    rating: int,
    comment: str,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        POST /api/reviews/
        {
            "review_id": 1,
            "content_id": 1,
            "user_id": 1,
            "rating": 1,
            "comment": "aaa"
        }
    """

    new_review = await ReviewsService(ReviewsRepository(db)).create(
        content_id=content_id, user_id=user_id, rating=rating, comment=comment
    )

    return new_review


@router.put("/{review_id}", summary="Update review by id", responses=update_review)
@handle_exceptions(status_code=400)
async def update(
    review_id: int,
    content_id: int = None,
    user_id: int = None,
    rating: int = None,
    comment: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/reviews/1
        {
            "review_id": 1,
            "rating": 5,
        }
    """

    review = await ReviewsService(ReviewsRepository(db)).update(
        review_id=review_id,
        content_id=content_id,
        user_id=user_id,
        rating=rating,
        comment=comment,
    )

    return review


@router.delete("/{review_id}", summary="Delete review by id", responses=delete_review)
@handle_exceptions(status_code=400)
async def delete(review_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/reviews/1
    """

    await ReviewsService(ReviewsRepository(db)).delete(review_id=review_id)
    return {"message": "Review deleted successfully"}
