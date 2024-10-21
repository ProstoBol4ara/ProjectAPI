from repositories import UserSubscriptionsRepository

class UserSubscriptionsService:
    def __init__(self, user_subscriptions_repository: UserSubscriptionsRepository):
        self.user_subscriptions_repository = user_subscriptions_repository

    async def get_user_subscriptions(self):
        return await self.user_subscriptions_repository.get_user_subscriptions()

    async def get_user_subscription(self, user_subscription_id: int):
        return await self.user_subscriptions_repository.get_user_subscription(user_subscription_id=user_subscription_id)

    async def create_user_subscription(self, start_date: str, end_date: str, user_id: int, plan_id: int):
        return await self.user_subscriptions_repository.create_user_subscription(start_date=start_date, end_date=end_date, user_id=user_id, plan_id=plan_id)

    async def update_user_subscription(self, user_subscription_id: int, start_date: str, end_date: str, user_id: int, plan_id: int):
        return await self.user_subscriptions_repository.update_user_subscription(user_subscription_id=user_subscription_id, start_date=start_date, end_date=end_date, user_id=user_id, plan_id=plan_id)

    async def delete_user_subscription(self, user_subscription_id: int):
        await self.user_subscriptions_repository.delete_user_subscription(user_subscription_id=user_subscription_id)
    