from fastapi import APIRouter, HTTPException, Depends
from repositories import ReviewsRepository
from database import AsyncSession, get_db
from services import ReviewsService
from responses.reviews import *

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.get('/', summary="Fetch all reviews", responses=get_reviews)
async def get_reviews(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/reviews
    """

    reviews = await ReviewsService(ReviewsRepository(db)).get_reviews()
    if reviews is None:
        raise HTTPException(status_code=400, detail="Reviews not found")
    return reviews

@router.get('/{review_id}', summary="Fetch review by id", responses=get_review)
async def get_review(review_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/reviews/1
    """

    review = await ReviewsService(ReviewsRepository(db)).get_review(review_id=review_id)
    if review is None:
        raise HTTPException(status_code=400, detail="Review not found")
    return review

@router.post('/', summary="Create review", responses=create_review)
async def create_review(content_id: int, user_id: int, rating: int, comment: str, db: AsyncSession = Depends(get_db)):
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

    try:
        new_review = await ReviewsService(ReviewsRepository(db)).create_review(content_id=content_id, user_id=user_id, rating=rating, comment=comment)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_review

@router.put('/{review_id}', summary="Update review by id", responses=update_review)
async def update_review(review_id: int, content_id: int = None, user_id: int = None, rating: int = None, comment: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/reviews/1
        {
            "review_id": 1,
            "rating": 5,
        }
    """

    try:
        review = await ReviewsService(ReviewsRepository(db)).update_review(review_id=review_id, content_id=content_id, user_id=user_id, rating=rating, comment=comment)
        if review is None:
            raise HTTPException(status_code=400, detail="Review not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return review

@router.delete('/{review_id}', summary="Delete review by id", responses=delete_review)
async def delete_review(review_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/reviews/1
    """

    if not await ReviewsService(ReviewsRepository(db)).delete_review(review_id=review_id):
        raise HTTPException(status_code=400, detail="Review not found")
    return {"message": "Review deleted successfully"}
