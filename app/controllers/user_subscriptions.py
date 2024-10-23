from fastapi import APIRouter, HTTPException, Depends
from repositories import UserSubscriptionsRepository
from services import UserSubscriptionsService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/user_subscriptions",
    tags=["user_subscriptions"]
)

@router.get('/')
async def get_user_subscriptions(db: AsyncSession = Depends(get_db)):
    user_subscriptions = UserSubscriptionsService(UserSubscriptionsRepository(db)).get_user_subscriptions()
    if user_subscriptions is None:
        raise HTTPException(status_code=400, detail="User subscriptions not found")
    return user_subscriptions

@router.get('/{user_subscription_id}')
async def get_user_subscription(user_subscription_id: int, db: AsyncSession = Depends(get_db)):
    user_subscription = UserSubscriptionsService(UserSubscriptionsRepository(db)).get_user_subscription(user_subscription_id=user_subscription_id)
    if user_subscription is None:
        raise HTTPException(status_code=400, detail="User subscription not found")
    return user_subscription

@router.post('/')
async def create_user_subscription(plan_name: str, plan_price: float, db: AsyncSession = Depends(get_db)):
    try:
        new_user_subscription = UserSubscriptionsService(UserSubscriptionsRepository(db)).create_user_subscription(plan_name=plan_name, plan_price=plan_price)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_user_subscription

@router.put('/{user_subscription_id}')
async def update_user_subscription(user_subscription_id: int, plan_name: str = None, plan_price: float = None, db: AsyncSession = Depends(get_db)):
    try:
        user_subscription = UserSubscriptionsService(UserSubscriptionsRepository(db)).update_user_subscription(user_subscription_id=user_subscription_id, plan_name=plan_name, plan_price=plan_price)
        if user_subscription is None:
            raise HTTPException(status_code=400, detail="User subscription not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return user_subscription

@router.delete('/{user_subscription_id}')
async def delete_user_subscription(user_subscription_id: int, db: AsyncSession = Depends(get_db)):
    if not UserSubscriptionsService(UserSubscriptionsRepository(db)).delete_user_subscription(user_subscription_id=user_subscription_id):
        raise HTTPException(status_code=400, detail="User subscription not found")
    return {"message": "User subscription deleted successfully"}