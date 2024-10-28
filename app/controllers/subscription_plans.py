from fastapi import APIRouter, HTTPException, Depends
from repositories import SubscriptionPlansRepository
from services import SubscriptionPlansService
from database import AsyncSession, get_db
from responses.subscription_plans import *

router = APIRouter(
    prefix="/subscription_plans",
    tags=["subscription_plans"]
)

@router.get('/', summary="Fetch all subscription plans", responses=get_subscription_plans)
async def get_subscription_plans(db: AsyncSession = Depends(get_db)):
    """
    Query example:
        
        GET /api/subscription_plans
    """

    subscription_plans = await SubscriptionPlansService(SubscriptionPlansRepository(db)).get_subscription_plans()
    if subscription_plans is None:
        raise HTTPException(status_code=400, detail="Subscription Plans not found")
    return subscription_plans

@router.get('/{plan_id}', summary="Fetch subscription plan by id", responses=get_subscription_plan)
async def get_subscription_plan(plan_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/subscription_plans/1
    """
    
    subscription_plan = await SubscriptionPlansService(SubscriptionPlansRepository(db)).get_subscription_plan(plan_id=plan_id)
    if subscription_plan is None:
        raise HTTPException(status_code=400, detail="Subscription plan not found")
    return subscription_plan

@router.post('/', summary="Create subscription plan", responses=create_subscription_plan)
async def create_subscription_plan(plan_name: str, plan_price: float, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/subscription_plans/
        {
            "plan_id": 1, 
            "plan_name": "aaa", 
            "plan_price": 100
        }
    """

    try:
        new_subscription_plan = await SubscriptionPlansService(SubscriptionPlansRepository(db)).create_subscription_plan(plan_name=plan_name, plan_price=plan_price)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_subscription_plan

@router.put('/{plan_id}', summary="Update subscription plan by id", responses=update_subscription_plan)
async def update_subscription_plan(subscription_plan_id: int, plan_name: str = None, plan_price: float = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/subscription_plans/1
        {
            "plan_id": 1, 
            "plan_name": "bbb"
        }
    """

    try:
        subscription_plan = await SubscriptionPlansService(SubscriptionPlansRepository(db)).update_subscription_plan(subscription_plan_id=subscription_plan_id, plan_name=plan_name, plan_price=plan_price)
        if subscription_plan is None:
            raise HTTPException(status_code=400, detail="Subscription plan not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return subscription_plan

@router.delete('/{subscription_plan_id}', summary="Delete subscription plan by id", responses=delete_subscription_plan)
async def delete_subscription_plan(subscription_plan_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/subscription_plans/1
    """

    if not await SubscriptionPlansService(SubscriptionPlansRepository(db)).delete_subscription_plan(subscription_plan_id=subscription_plan_id):
        raise HTTPException(status_code=400, detail="Subscription plan not found")
    return {"message": "Subscription plan deleted successfully"}