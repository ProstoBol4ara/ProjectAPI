from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import SubscriptionPlans

router = APIRouter(
    prefix="/subscription_plans",
    tags=["subscription_plans"]
)

@router.get('/', response_model=list[dict])
async def get_subscription_plans(db: Session = Depends(get_db)):
    subscription_plans = db.query(SubscriptionPlans).all()
    if subscription_plans is None:
        raise HTTPException(status_code=400, detail="SubscriptionPlans not found")
    return [{"plan_id": subscription_plan.plan_id, "plan_name": subscription_plan.plan_name, "plan_price": subscription_plan.plan_price} for subscription_plan in subscription_plans]

@router.get('/{plan_id}', response_model=dict)
async def get_subscription_plan(plan_id: int, db: Session = Depends(get_db)):
    subscription_plan = db.query(SubscriptionPlans).filter(SubscriptionPlans.plan_id == plan_id).first()
    if subscription_plan is None:
        raise HTTPException(status_code=400, detail="Subscription plan not found")
    return {"plan_id": subscription_plan.plan_id, "plan_name": subscription_plan.plan_name, "plan_price": subscription_plan.plan_price}

@router.post('/', response_model=dict)
async def create_subscription_plan(plan_name: str, plan_price: float, db: Session = Depends(get_db)):
    try:
        new_subscription_plan = SubscriptionPlans(plan_name=plan_name, plan_price=plan_price)
        db.add(new_subscription_plan)
        db.commit()
        db.refresh(new_subscription_plan)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"plan_id": new_subscription_plan.plan_id, "plan_name": new_subscription_plan.plan_name, "plan_price": new_subscription_plan.plan_price}

@router.put('/{plan_id}', response_model=dict)
async def update_subscription_plan(subscription_plan_id: int, plan_name: str = None, plan_price: float = None, db: Session = Depends(get_db)):
    subscription_plan = db.query(SubscriptionPlans).filter(SubscriptionPlans.plan_id == plan_id).first()
    if subscription_plan is None:
        raise HTTPException(status_code=400, detail="Subscription plan not found")

    if plan_name:
        subscription_plan.plan_name = plan_name
    if plan_price:
        subscription_plan.plan_price = plan_price

    db.commit()
    db.refresh(subscription_plan)
    return {"plan_id": subscription_plan.plan_id, "plan_name": subscription_plan.plan_name, "plan_price": subscription_plan.plan_price}

@router.delete('/{subscription_plan_id}', response_model=dict)
async def delete_subscription_plan(subscription_plan_id: int, db: Session = Depends(get_db)):
    subscription_plan = db.query(SubscriptionPlans).filter(SubscriptionPlans.plan_id == subscription_plan_id).first()
    if subscription_plan is None:
        raise HTTPException(status_code=400, detail="Subscription plan not found")

    db.delete(subscription_plan)
    db.commit()
    return {"message": "Subscription plan deleted successfully"}