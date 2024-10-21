from database import AsyncSession
from models import SubscriptionPlans

class SubscriptionPlansRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_subscription_plans(self):
        subscription_plans = await self.db.execute(select(SubscriptionPlans))
        return subscription_plans.scalar().all()

    async def get_subscription_plan(self, plan_id: int):
        subscription_plan = await self.db.execute(
            select(SubscriptionPlans).where(SubscriptionPlans.plan_id == plan_id)
        )
        return subscription_plan.scalar_one_or_none()

    async def create_subscription_plan(self, plan_name: str, plan_price: float):
        new_subscription_plan = SubscriptionPlans(plan_name=plan_name, plan_price=plan_price)
        self.db.add(new_subscription_plan)
        await self.db.commit()
        await self.db.refresh(new_subscription_plan)
        return new_subscription_plan

    async def update_subscription_plan(self, subscription_plan_id: int, plan_name: str = None, plan_price: float = None):
        subscription_plan = await self.db.execute(
            select(SubscriptionPlans).where(SubscriptionPlans.plan_id == plan_id)
        )
        subscription_plan = subscription_plan.scalar_one_or_none()

        if plan_name:
            subscription_plan.plan_name = plan_name
        if plan_price:
            subscription_plan.plan_price = plan_price

        await self.db.commit()
        await self.db.refresh(subscription_plan)
        return subscription_plan

    async def delete_subscription_plan(self, subscription_plan_id: int):
        await self.db.execute(
            delete(SubscriptionPlans).where(SubscriptionPlans.subscription_plan_id == subscription_plan_id)
        )
        await self.db.commit()