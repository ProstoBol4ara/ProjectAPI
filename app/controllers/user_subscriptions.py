from repositories import UserSubscriptionsRepository
from services import UserSubscriptionsService
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from responses.user_subscriptions import *
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/user_subscriptions", tags=["user_subscriptions"])


@router.get(
    "/", summary="Fetch all user subscriptions", responses=get_user_subscriptions
)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/user_subscriptions
    """

    user_subscriptions = UserSubscriptionsService(
        UserSubscriptionsRepository(db)
    ).get_all()
    return user_subscriptions


@router.get(
    "/{user_subscription_id}",
    summary="Fetch user subscription by id",
    responses=get_user_subscription,
)
@handle_exceptions(status_code=400)
async def get_one(user_subscription_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/user_subscriptions/1
    """

    user_subscription = UserSubscriptionsService(
        UserSubscriptionsRepository(db)
    ).get_one(user_subscription_id=user_subscription_id)

    return user_subscription


@router.post(
    "/", summary="Create user subscription", responses=create_user_subscription
)
@handle_exceptions(status_code=400)
async def create(plan_name: str, plan_price: float, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/user_subscriptions/
        {
            "user_subscription_id": 1,
            "plan_name": "aaa",
            "plan_price": 100
        }
    """

    new_user_subscription = UserSubscriptionsService(
        UserSubscriptionsRepository(db)
    ).create(plan_name=plan_name, plan_price=plan_price)

    return new_user_subscription


@router.put(
    "/{user_subscription_id}",
    summary="Update user subscription by id",
    responses=update_user_subscription,
)
@handle_exceptions(status_code=400)
async def update(
    user_subscription_id: int,
    plan_name: str = None,
    plan_price: float = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/user_subscriptions/1
        {
            "user_subscription_id": 1,
            "plan_name": "bbb"
        }
    """

    user_subscription = UserSubscriptionsService(
        UserSubscriptionsRepository(db)
    ).update(
        user_subscription_id=user_subscription_id,
        plan_name=plan_name,
        plan_price=plan_price,
    )

    return user_subscription


@router.delete(
    "/{user_subscription_id}",
    summary="Delete user subscription by id",
    responses=delete_user_subscription,
)
@handle_exceptions(status_code=400)
async def delete(user_subscription_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/user_subscriptions/1
    """

    await UserSubscriptionsService(UserSubscriptionsRepository(db)).delete(
        user_subscription_id=user_subscription_id
    )
    return {"message": "User subscription deleted successfully"}
