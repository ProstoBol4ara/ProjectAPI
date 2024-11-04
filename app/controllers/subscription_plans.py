from repositories import SubscriptionPlansRepository
from services import SubscriptionPlansService
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from responses.subscription_plans import *
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/subscription_plans", tags=["subscription_plans"])


@router.get(
    "/", summary="Fetch all subscription plans", responses=get_subscription_plans
)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/subscription_plans
    """

    subscription_plans = await SubscriptionPlansService(
        SubscriptionPlansRepository(db)
    ).get_all()
    return subscription_plans


@router.get(
    "/{plan_id}",
    summary="Fetch subscription plan by id",
    responses=get_subscription_plan,
)
@handle_exceptions(status_code=400)
async def get_one(plan_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/subscription_plans/1
    """

    subscription_plan = await SubscriptionPlansService(
        SubscriptionPlansRepository(db)
    ).get_one(plan_id=plan_id)
    return subscription_plan


@router.post(
    "/", summary="Create subscription plan", responses=create_subscription_plan
)
@handle_exceptions(status_code=400)
async def create(plan_name: str, plan_price: float, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/subscription_plans/
        {
            "plan_id": 1,
            "plan_name": "aaa",
            "plan_price": 100
        }
    """

    new_subscription_plan = await SubscriptionPlansService(
        SubscriptionPlansRepository(db)
    ).create(plan_name=plan_name, plan_price=plan_price)
    return new_subscription_plan


@router.put(
    "/{plan_id}",
    summary="Update subscription plan by id",
    responses=update_subscription_plan,
)
@handle_exceptions(status_code=400)
async def update(
    subscription_plan_id: int,
    plan_name: str = None,
    plan_price: float = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/subscription_plans/1
        {
            "plan_id": 1,
            "plan_name": "bbb"
        }
    """

    subscription_plan = await SubscriptionPlansService(
        SubscriptionPlansRepository(db)
    ).update(
        subscription_plan_id=subscription_plan_id,
        plan_name=plan_name,
        plan_price=plan_price,
    )
    return subscription_plan


@router.delete(
    "/{subscription_plan_id}",
    summary="Delete subscription plan by id",
    responses=delete_subscription_plan,
)
@handle_exceptions(status_code=400)
async def delete(subscription_plan_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/subscription_plans/1
    """

    await SubscriptionPlansService(SubscriptionPlansRepository(db)).delete(
        subscription_plan_id=subscription_plan_id
    )
    return {"message": "Subscription plan deleted successfully"}
