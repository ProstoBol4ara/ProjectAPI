from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Reviews

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.get('/', response_model=list[dict])
async def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(Reviews).all()
    if reviews is None:
        raise HTTPException(status_code=400, detail="Reviews not found")
    return [{"review_id": review.review_id, "content_id": review.content_id, "user_id": review.user_id, "rating": review.rating, "comment": review.comment} for review in reviews]

@router.get('/{review_id}', response_model=dict)
async def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Reviews).filter(Reviews.review_id == review_id).first()
    if review is None:
        raise HTTPException(status_code=400, detail="Review not found")
    return {"review_id": review.review_id, "content_id": review.content_id, "user_id": review.user_id, "rating": review.rating, "comment": review.comment}

@router.post('/', response_model=dict)
async def create_review(content_id: int, user_id: int, rating: int, comment: str, db: Session = Depends(get_db)):
    try:
        new_review = Reviews(content_id=content_id, user_id=user_id, rating=rating, comment=comment)
        db.add(new_review)
        db.commit()
        db.refresh(new_review)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"review_id": new_review.review_id, "content_id": new_review.content_id, "user_id": new_review.user_id, "rating": new_review.rating, "comment": new_review.comment}

@router.put('/{review_id}', response_model=dict)
async def update_review(review_id: int, content_id: int = None, user_id: int = None, rating: int = None, comment: str = None, db: Session = Depends(get_db)):
    review = db.query(Reviews).filter(Reviews.review_id == review_id).first()
    if review is None:
        raise HTTPException(status_code=400, detail="Review not found")

    if content_id:
        review.content_id = content_id
    if user_id:
        review.user_id = user_id
    if rating:
        review.rating = rating
    if comment:
        review.comment = comment

    db.commit()
    db.refresh(review)
    return {"review_id": review.review_id, "content_id": review.content_id, "user_id": review.user_id, "rating": review.rating, "comment": review.comment}

@router.delete('/{review_id}', response_model=dict)
async def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Reviews).filter(Reviews.review_id == review_id).first()
    if review is None:
        raise HTTPException(status_code=400, detail="Review not found")

    db.delete(review)
    db.commit()
    return {"message": "Review deleted successfully"}