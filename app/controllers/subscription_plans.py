from fastapi import APIRouter, HTTPException, Depends
from repositories import SubscriptionPlansRepository
from services import SubscriptionPlansService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/subscription_plans",
    tags=["subscription_plans"]
)

@router.get('/')
async def get_subscription_plans(db: AsyncSession = Depends(get_db)):
    subscription_plans = await SubscriptionPlansService(SubscriptionPlansRepository(db)).get_subscription_plans()
    if subscription_plans is None:
        raise HTTPException(status_code=400, detail="SubscriptionPlans not found")
    return subscription_plans

@router.get('/{plan_id}')
async def get_subscription_plan(plan_id: int, db: AsyncSession = Depends(get_db)):
    subscription_plan = await SubscriptionPlansService(SubscriptionPlansRepository(db)).get_subscription_plan(plan_id=plan_id)
    if subscription_plan is None:
        raise HTTPException(status_code=400, detail="Subscription plan not found")
    return subscription_plan

@router.post('/')
async def create_subscription_plan(plan_name: str, plan_price: float, db: AsyncSession = Depends(get_db)):
    try:
        new_subscription_plan = await SubscriptionPlansService(SubscriptionPlansRepository(db)).create_subscription_plan(plan_name=plan_name, plan_price=plan_price)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return {"plan_id": new_subscription_plan.plan_id, "plan_name": new_subscription_plan.plan_name, "plan_price": new_subscription_plan.plan_price}

@router.put('/{plan_id}')
async def update_subscription_plan(subscription_plan_id: int, plan_name: str = None, plan_price: float = None, db: AsyncSession = Depends(get_db)):
    try:
        subscription_plan = await SubscriptionPlansService(SubscriptionPlansRepository(db)).update_subscription_plan(subscription_plan_id=subscription_plan_id, plan_name=plan_name, plan_price=plan_price)
        if subscription_plan is None:
            raise HTTPException(status_code=400, detail="Subscription plan not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return subscription_plan

@router.delete('/{subscription_plan_id}')
async def delete_subscription_plan(subscription_plan_id: int, db: AsyncSession = Depends(get_db)):
    if not await SubscriptionPlansService(SubscriptionPlansRepository(db)).delete_subscription_plan(subscription_plan_id=subscription_plan_id):
        raise HTTPException(status_code=400, detail="Subscription plan not found")
    return {"message": "Subscription plan deleted successfully"}