from database import AsyncSession
from models import UserSubscriptions

class UserSubscriptionsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_subscriptions(self):
        user_subscriptions = await self.db.execute(select(UserSubscriptions))
        return user_subscriptions.scalar().all()

    async def get_user_subscription(self, user_subscription_id: int, db: Session = Depends(get_db)):
        user_subscription = await self.db.execute(
            select(UserSubscriptions).where(UserSubscriptions.user_subscription_id == user_subscription_id)
        )
        return user_subscription.scalar_one_or_none()

    async def create_user_subscription(self, plan_name: str, plan_price: float, db: Session = Depends(get_db)):
        new_user_subscription = UserSubscriptions(plan_name=plan_name, plan_price=plan_price)
        self.db.add(new_user_subscription)
        await self.db.commit()
        await self.db.refresh(new_user_subscription)
        return new_user_subscription

    async def update_user_subscription(self, user_subscription_id: int, plan_name: str = None, plan_price: float = None, db: Session = Depends(get_db)):
        user_subscription = await self.db.execute(
            select(UserSubscriptions).where(UserSubscriptions.user_subscription_id == user_subscription_id)
        )
        user_subscription = user_subscription.scalar_one_or_none()

        if plan_name:
            user_subscription.plan_name = plan_name
        if plan_price:
            user_subscription.plan_price = plan_price
        
        db.commit()
        db.refresh(user_subscription)
        return user_subscription

    async def delete_user_subscription(self, user_subscription_id: int, db: Session = Depends(get_db)):
        await self.db.execute(
            delete(UserSubscriptions).where(UserSubscriptions.user_subscription_id == user_subscription_id)
        )
        await self.db.commit()