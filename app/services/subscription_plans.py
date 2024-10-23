from repositories import SubscriptionPlansRepository

class SubscriptionPlansService:
    def __init__(self, subscription_plans_repository: SubscriptionPlansRepository):
        self.subscription_plans_repository = subscription_plans_repository

    async def get_subscription_plans(self):
        subscription_plans = await self.subscription_plans_repository.get_subscription_plans()
        return None if subscription_plans is None else [{"plan_id": subscription_plan.plan_id, "plan_name": subscription_plan.plan_name, "plan_price": subscription_plan.plan_price} for subscription_plan in subscription_plans]

    async def get_subscription_plan(self, plan_id: int):
        subscription_plan = await self.subscription_plans_repository.get_subscription_plan(plan_id=plan_id)
        return None if subscription_plan is None else {"plan_id": subscription_plan.plan_id, "plan_name": subscription_plan.plan_name, "plan_price": subscription_plan.plan_price}

    async def create_subscription_plan(self, plan_name: str, plan_price: float):
        new_subscription_plan = await self.subscription_plans_repository.create_subscription_plan(plan_name=plan_name, plan_price=plan_price)
        return {"plan_id": new_subscription_plan.plan_id, "plan_name": new_subscription_plan.plan_name, "plan_price": new_subscription_plan.plan_price}

    async def update_subscription_plan(self, subscription_plan_id: int, plan_name: str = None, plan_price: float = None):
        subscription_plan = await self.subscription_plans_repository.update_subscription_plan(subscription_plan_id=subscription_plan_id, plan_name=plan_name, plan_price=plan_price)
        return None if subscription_plan is None else {"plan_id": subscription_plan.plan_id, "plan_name": subscription_plan.plan_name, "plan_price": subscription_plan.plan_price}

    async def delete_subscription_plan(self, subscription_plan_id: int):
        return await self.subscription_plans_repository.delete_subscription_plan(subscription_plan_id=subscription_plan_id)