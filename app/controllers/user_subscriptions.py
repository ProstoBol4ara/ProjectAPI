from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import UserSubscriptions

router = APIRouter(
    prefix="/user_subscriptions",
    tags=["user_subscriptions"]
)

@router.get('/', response_model=list[dict])
async def get_user_subscriptions(db: Session = Depends(get_db)):
    user_subscriptions = db.query(UserSubscriptions).all()
    if user_subscriptions is None:
        raise HTTPException(status_code=400, detail="User subscription subscriptions not found")
    return [{"user_subscription_id": user_subscription.user_subscription_id, "plan_name": user_subscription.plan_name, "plan_price": user_subscription.plan_price} for user_subscription in user_subscriptions]

@router.get('/{user_subscription_id}', response_model=dict)
async def get_user_subscription(user_subscription_id: int, db: Session = Depends(get_db)):
    user_subscription = db.query(UserSubscriptions).filter(UserSubscriptions.user_subscription_id == user_subscription_id).first()
    if user_subscription is None:
        raise HTTPException(status_code=400, detail="User subscription not found")
    return {"user_subscription_id": user_subscription.user_subscription_id, "plan_name": user_subscription.plan_name, "plan_price": user_subscription.plan_price}

@router.post('/', response_model=dict)
async def create_user_subscription(plan_name: str, plan_price: float, db: Session = Depends(get_db)):
    try:
        new_user_subscription = UserSubscriptions(plan_name=plan_name, plan_price=plan_price)
        db.add(new_user_subscription)
        db.commit()
        db.refresh(new_user_subscription)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"user_subscription_id": new_user_subscription.user_subscription_id, "plan_name": new_user_subscription.plan_name, "plan_price": new_user_subscription.plan_price}

@router.put('/{user_subscription_id}', response_model=dict)
async def update_user_subscription(user_subscription_id: int, plan_name: str = None, plan_price: float = None, db: Session = Depends(get_db)):
    user_subscription = db.query(UserSubscriptions).filter(UserSubscriptions.user_subscription_id == user_subscription_id).first()
    if user_subscription is None:
        raise HTTPException(status_code=400, detail="User subscription not found")

    if plan_name:
        user_subscription.plan_name = plan_name
    if plan_price:
        user_subscription.plan_price = plan_price
    
    db.commit()
    db.refresh(user_subscription)
    return {"user_subscription_id": user_subscription.user_subscription_id, "plan_name": user_subscription.plan_name, "plan_price": user_subscription.plan_price}

@router.delete('/{user_subscription_id}', response_model=dict)
async def delete_user_subscription(user_subscription_id: int, db: Session = Depends(get_db)):
    user_subscription = db.query(UserSubscriptions).filter(UserSubscriptions.user_subscription_id == user_subscription_id).first()
    if user_subscription is None:
        raise HTTPException(status_code=400, detail="User subscription not found")

    db.delete(user_subscription)
    db.commit()
    return {"message": "User subscription deleted successfully"}