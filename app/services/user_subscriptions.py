from repositories import UserSubscriptionsRepository
from constants import date_pattern
from re import match


class UserSubscriptionsService:
    def __init__(self, repository: UserSubscriptionsRepository):
        self.repository = repository

    async def get_all(self):
        user_subscriptions = await self.repository.get_all()

        return (
            None
            if user_subscriptions is None
            else [
                {
                    "user_subscription_id": user_subscription.user_subscription_id,
                    "start_date": user_subscription.start_date,
                    "end_date": user_subscription.end_date,
                    "user_id": user_subscription.user_id,
                    "plan_id": user_subscription.plan_id,
                }
                for user_subscription in user_subscriptions
            ]
        )

    async def get_one(self, user_subscription_id: int):
        if not user_subscription_id:
            raise ValueError("user_subscription_id cannot be empty")

        user_subscription = await self.repository.get_one(
            user_subscription_id=user_subscription_id
        )

        if not user_subscription:
            raise ValueError("User subscription not found")

        return {
            "user_subscription_id": user_subscription.user_subscription_id,
            "start_date": user_subscription.start_date,
            "end_date": user_subscription.end_date,
            "user_id": user_subscription.user_id,
            "plan_id": user_subscription.plan_id,
        }

    async def create(self, start_date: str, end_date: str, user_id: int, plan_id: int):
        if not start_date or not end_date or not user_id or not plan_id:
            raise ValueError(
                "start_date and end_date and user_id and plan_id cannot be empty"
            )

        if start_date and not match(date_pattern, start_date):
            raise ValueError("Invalid start_date! Date format: day.month.year")

        if end_date and not match(date_pattern, end_date):
            raise ValueError("Invalid end_date! Date format: day.month.year")

        new_user_subscription = await self.repository.create(
            start_date=start_date, end_date=end_date, user_id=user_id, plan_id=plan_id
        )

        return {
            "user_subscription_id": new_user_subscription.user_subscription_id,
            "start_date": new_user_subscription.start_date,
            "end_date": new_user_subscription.end_date,
            "user_id": new_user_subscription.user_id,
            "plan_id": new_user_subscription.plan_id,
        }

    async def update(
        self,
        user_subscription_id: int,
        start_date: str = None,
        end_date: str = None,
        user_id: int = None,
        plan_id: int = None,
    ):

        if not user_subscription_id:
            raise ValueError("user_subscription_id cannot be empty")

        user_subscription = await self.repository.update(
            user_subscription_id=user_subscription_id,
            start_date=start_date,
            end_date=end_date,
            user_id=user_id,
            plan_id=plan_id,
        )

        if not user_subscription:
            raise ValueError("User subscription not found")

        return {
            "user_subscription_id": user_subscription.user_subscription_id,
            "start_date": user_subscription.start_date,
            "end_date": user_subscription.end_date,
            "user_id": user_subscription.user_id,
            "plan_id": user_subscription.plan_id,
        }

    async def delete(self, user_subscription_id: int):
        if not user_subscription_id:
            raise ValueError("user_subscription_id cannot be empty")

        if not (
            delete_user_subscription := await self.repository.delete(
                user_subscription_id=user_subscription_id
            )
        ):
            raise ValueError("User subscription not found")
        return delete_user_subscription
