from repositories import ReviewsRepository


class ReviewsService:
    def __init__(self, repository: ReviewsRepository):
        self.repository = repository

    async def get_all(self):
        reviews = await self.repository.get_all()

        return (
            None
            if reviews is None
            else [
                {
                    "review_id": review.review_id,
                    "content_id": review.content_id,
                    "user_id": review.user_id,
                    "rating": review.rating,
                    "comment": review.comment,
                }
                for review in reviews
            ]
        )

    async def get_one(self, review_id: int):
        if not review_id:
            raise ValueError("review_id cannot be empty")

        review = await self.repository.get_one(review_id=review_id)

        if not review:
            raise ValueError("Review not found")

        return {
            "review_id": review.review_id,
            "content_id": review.content_id,
            "user_id": review.user_id,
            "rating": review.rating,
            "comment": review.comment,
        }

    async def create(self, content_id: int, user_id: int, rating: int, comment: str):
        if not content_id or not user_id or not rating or not comment:
            raise ValueError(
                "content_id and user_id and rating and comment cannot be empty"
            )

        if not rating or not 0 < rating < 6:
            raise ValueError("rating can be greater than 0 and less than 6.")

        new_review = await self.repository.create(
            content_id=content_id, user_id=user_id, rating=rating, comment=comment
        )

        return {
            "review_id": new_review.review_id,
            "content_id": new_review.content_id,
            "user_id": new_review.user_id,
            "rating": new_review.rating,
            "comment": new_review.comment,
        }

    async def update(
        self,
        review_id: int,
        content_id: int = None,
        user_id: int = None,
        rating: int = None,
        comment: str = None,
    ):

        if not review_id:
            raise ValueError("review_id cannot be empty")

        if not rating or not 0 < rating < 6:
            raise ValueError(
                "rating cannot be empty and can be greater than 0 and less than 6."
            )

        review = await self.repository.update(
            review_id=review_id,
            content_id=content_id,
            user_id=user_id,
            rating=rating,
            comment=comment,
        )

        if not review:
            raise ValueError("Review not found")

        return {
            "review_id": review.review_id,
            "content_id": review.content_id,
            "user_id": review.user_id,
            "rating": review.rating,
            "comment": review.comment,
        }

    async def delete(self, review_id: int):
        if not review_id:
            raise ValueError("review_id cannot be empty")

        if not (delete_review := await self.repository.delete(review_id=review_id)):
            raise ValueError("Review not found")
        return delete_review
