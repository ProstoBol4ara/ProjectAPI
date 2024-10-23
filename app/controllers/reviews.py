from fastapi import APIRouter, HTTPException, Depends
from repositories import ReviewsRepository
from database import AsyncSession, get_db
from services import ReviewsService

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.get('/')
async def get_reviews(db: AsyncSession = Depends(get_db)):
    reviews = await ReviewsService(ReviewsRepository(db)).get_reviews()
    if reviews is None:
        raise HTTPException(status_code=400, detail="Reviews not found")
    return reviews

@router.get('/{review_id}')
async def get_review(review_id: int, db: AsyncSession = Depends(get_db)):
    review = await ReviewsService(ReviewsRepository(db)).get_review(review_id=review_id)
    if review is None:
        raise HTTPException(status_code=400, detail="Review not found")
    return review

@router.post('/')
async def create_review(content_id: int, user_id: int, rating: int, comment: str, db: AsyncSession = Depends(get_db)):
    try:
        new_review = await ReviewsService(ReviewsRepository(db)).create_review(content_id=content_id, user_id=user_id, rating=rating, comment=comment)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_review

@router.put('/{review_id}')
async def update_review(review_id: int, content_id: int = None, user_id: int = None, rating: int = None, comment: str = None, db: AsyncSession = Depends(get_db)):
    try:
        review = await ReviewsService(ReviewsRepository(db)).update_review(review_id=review_id, content_id=content_id, user_id=user_id, rating=rating, comment=comment)
        if review is None:
            raise HTTPException(status_code=400, detail="Review not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return review

@router.delete('/{review_id}')
async def delete_review(review_id: int, db: AsyncSession = Depends(get_db)):
    if not await ReviewsService(ReviewsRepository(db)).delete_review(review_id=review_id):
        raise HTTPException(status_code=400, detail="Review not found")
    return {"message": "Review deleted successfully"}