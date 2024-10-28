from database import AsyncSession, select, delete
from models import Reviews

class ReviewsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_reviews(self):
        reviews = await self.db.execute(select(Reviews))
        return reviews.scalars().all()

    async def get_review(self, review_id: int):
        review = await self.db.execute(
            select(Reviews).where(Reviews.review_id == review_id)
        )
        return review.scalar_one_or_none()

    async def create_review(self, content_id: int, user_id: int, rating: int, comment: str):
        new_review = Reviews(content_id=content_id, user_id=user_id, rating=rating, comment=comment)
        self.db.add(new_review)
        await self.db.commit()
        await self.db.refresh(new_review)
        return new_review

    async def update_review(self, review_id: int, content_id: int = None, user_id: int = None, rating: int = None, comment: str = None):
        review = await self.db.execute(
            select(Reviews).where(Reviews.review_id == review_id)
        )
        review = review.scalar_one_or_none()

        if content_id:
            review.content_id = content_id
        if user_id:
            review.user_id = user_id
        if rating:
            review.rating = rating
        if comment:
            review.comment = comment

        await self.db.commit()
        await self.db.refresh(review)
        return review

    async def delete_review(self, review_id: int):
        result = await self.db.execute(
            delete(Reviews).where(Reviews.review_id == review_id)
        )
        await self.db.commit()
        return result.rowcount > 0
