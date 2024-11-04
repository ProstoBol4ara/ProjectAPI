from database import AsyncSession, select, delete
from models import SubscriptionPlans


class SubscriptionPlansRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        subscription_plans = await self.db.execute(select(SubscriptionPlans))
        return subscription_plans.scalars().all()

    async def get_one(self, plan_id: int):
        subscription_plan = await self.db.execute(
            select(SubscriptionPlans).where(SubscriptionPlans.plan_id == plan_id)
        )
        return subscription_plan.scalar_one_or_none()

    async def create(self, plan_name: str, plan_price: float):
        new_subscription_plan = SubscriptionPlans(
            plan_name=plan_name, plan_price=plan_price
        )
        self.db.add(new_subscription_plan)
        await self.db.commit()
        await self.db.refresh(new_subscription_plan)
        return new_subscription_plan

    async def update(
        self, plan_id: int, plan_name: str = None, plan_price: float = None
    ):
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

    async def delete(self, plan_id: int):
        result = await self.db.execute(
            delete(SubscriptionPlans).where(SubscriptionPlans.plan_id == plan_id)
        )
        await self.db.commit()
        return result.rowcount > 0
