from database import AsyncSession, select, delete
from models import UserSubscriptions
from datetime import datetime

class UserSubscriptionsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_subscriptions(self):
        user_subscriptions = await self.db.execute(select(UserSubscriptions))
        return user_subscriptions.scalars().all()

    async def get_user_subscription(self, user_subscription_id: int):
        user_subscription = await self.db.execute(
            select(UserSubscriptions).where(UserSubscriptions.user_subscription_id == user_subscription_id)
        )
        return user_subscription.scalar_one_or_none()

    async def create_user_subscription(self, start_date: str, end_date: str, user_id: int, plan_id: int):
        start_date = datetime.strptime(start_date, '%d.%m.%Y').date()
        end_date = datetime.strptime(end_date, '%d.%m.%Y').date()
        new_user_subscription = UserSubscriptions(start_date=start_date, end_date=end_date, user_id=user_id, plan_id=plan_id)
        self.db.add(new_user_subscription)
        await self.db.commit()
        await self.db.refresh(new_user_subscription)
        return new_user_subscription

    async def update_user_subscription(self, user_subscription_id: int, start_date: str = None, end_date: str = None, user_id: int = None, plan_id: int = None):
        user_subscription = await self.db.execute(
            select(UserSubscriptions).where(UserSubscriptions.user_subscription_id == user_subscription_id)
        )
        user_subscription = user_subscription.scalar_one_or_none()

        if start_date:
            user_subscription.start_date = datetime.strptime(start_date, '%d.%m.%Y').date()
        if end_date:
            user_subscription.end_date = datetime.strptime(end_date, '%d.%m.%Y').date()
        if user_id:
            user_subscription.user_id = user_id
        if plan_id:
            user_subscription.plan_id = plan_id

        await self.db.commit()
        await self.db.refresh(user_subscription)
        return user_subscription

    async def delete_user_subscription(self, user_subscription_id: int):
        result = await self.db.execute(
            delete(UserSubscriptions).where(UserSubscriptions.user_subscription_id == user_subscription_id)
        )
        await self.db.commit()
        return result.rowcount > 0
