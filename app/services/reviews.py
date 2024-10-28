from repositories import ReviewsRepository

class ReviewsService:
    def __init__(self, reviews_repository: ReviewsRepository):
        self.reviews_repository = reviews_repository

    async def get_reviews(self):
        reviews = await self.reviews_repository.get_reviews()
        return None if reviews is None else [{"review_id": review.review_id, "content_id": review.content_id, "user_id": review.user_id, "rating": review.rating, "comment": review.comment} for review in reviews]

    async def get_review(self, review_id: int):
        review = await self.reviews_repository.get_review(review_id=review_id)
        return None if review is None else {"review_id": review.review_id, "content_id": review.content_id, "user_id": review.user_id, "rating": review.rating, "comment": review.comment}

    async def create_review(self, content_id: int, user_id: int, rating: int, comment: str):
        new_review = await self.reviews_repository.create_review(content_id=content_id, user_id=user_id, rating=rating, comment=comment)
        return {"review_id": new_review.review_id, "content_id": new_review.content_id, "user_id": new_review.user_id, "rating": new_review.rating, "comment": new_review.comment}

    async def update_review(self, review_id: int, content_id: int = None, user_id: int = None, rating: int = None, comment: str = None):
        review = await self.reviews_repository.update_review(review_id=review_id, content_id=content_id, user_id=user_id, rating=rating, comment=comment)
        return None if review is None else {"review_id": review.review_id, "content_id": review.content_id, "user_id": review.user_id, "rating": review.rating, "comment": review.comment}

    async def delete_review(self, review_id: int):
        return await self.reviews_repository.delete_review(review_id=review_id)
