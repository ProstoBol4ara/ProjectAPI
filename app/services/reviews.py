from repositories import ReviewsRepository

class ReviewsService:
    def __init__(self, reviews_repository: ReviewsRepository):
        self.reviews_repository = reviews_repository

    async def get_reviews(self):
        return await self.reviews_repository.get_reviews()

    async def get_review(self, review_id: int):
        return await self.reviews_repository.get_review(review_id=review_id)

    async def create_review(self, content_id: int, user_id: int, rating: int, comment: str):
        return await self.reviews_repository.create_review(content_id=content_id, user_id=user_id, rating=rating, comment=comment)

    async def update_review(self, review_id: int, content_id: int = None, user_id: int = None, rating: int = None, comment: str = None):
        return await self.reviews_repository.update_review(review_id=review_id, content_id=content_id, user_id=user_id, rating=rating, comment=comment)

    async def delete_review(self, review_id: int):
        await self.reviews_repository.delete_review(review_id=review_id)
    