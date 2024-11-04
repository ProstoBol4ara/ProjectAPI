from repositories import SubscriptionPlansRepository


class SubscriptionPlansService:
    def __init__(self, repository: SubscriptionPlansRepository):
        self.repository = repository

    async def get_all(self):
        subscription_plans = await self.repository.get_all()

        return (
            None
            if subscription_plans is None
            else [
                {
                    "plan_id": subscription_plan.plan_id,
                    "plan_name": subscription_plan.plan_name,
                    "plan_price": subscription_plan.plan_price,
                }
                for subscription_plan in subscription_plans
            ]
        )

    async def get_one(self, plan_id: int):
        if not plan_id:
            raise ValueError("plan_id cannot be empty")

        subscription_plan = await self.repository.get_one(plan_id=plan_id)

        if not subscription_plan:
            raise ValueError("Subscription plan not found")

        return {
            "plan_id": subscription_plan.plan_id,
            "plan_name": subscription_plan.plan_name,
            "plan_price": subscription_plan.plan_price,
        }

    async def create(self, plan_name: str, plan_price: float):
        if not plan_name or not plan_name:
            raise ValueError("plan_name and plan_price cannot be empty")

        if plan_price < 0:
            raise ValueError("plan_price can be greater than 0")

        new_subscription_plan = await self.repository.create(
            plan_name=plan_name, plan_price=plan_price
        )

        return {
            "plan_id": new_subscription_plan.plan_id,
            "plan_name": new_subscription_plan.plan_name,
            "plan_price": new_subscription_plan.plan_price,
        }

    async def update(
        self, plan_id: int, plan_name: str = None, plan_price: float = None
    ):
        if not plan_id:
            raise ValueError("subscription_plan_id cannot be empty")

        if plan_price < 0:
            raise ValueError("plan_price can be greater than 0")

        subscription_plan = await self.repository.update(
            plan_id=plan_id, plan_name=plan_name, plan_price=plan_price
        )

        if not subscription_plan:
            raise ValueError("Subscription plan not found")

        return {
            "plan_id": subscription_plan.plan_id,
            "plan_name": subscription_plan.plan_name,
            "plan_price": subscription_plan.plan_price,
        }

    async def delete(self, plan_id: int):
        if not plan_id:
            raise ValueError("subscription_plan_id cannot be empty")

        if not (
            delete_subscription_plan := await self.repository.delete(plan_id=plan_id)
        ):
            raise ValueError("Subscription plan not found")
        return delete_subscription_plan
