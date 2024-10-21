from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import PaymentMethods

router = APIRouter(
    prefix="/payment_methods",
    tags=["payment_methods"]
)

@router.get('/')
async def get_payment_methods(db: Session = Depends(get_db)):
    payment_methods = db.query(PaymentMethods).all()
    if payment_methods is None:
        raise HTTPException(status_code=400, detail="PaymentMethods not found")
    return [{"payment_method_id": payment_method.payment_method_id, "name": payment_method.name, "email": payment_method.email} for payment_method in payment_methods]

@router.get('/{payment_method_id}')
async def get_payment_method(payment_method_id: int, db: Session = Depends(get_db)):
    payment_method = db.query(PaymentMethods).filter(PaymentMethods.payment_method_id == payment_method_id).first()
    if payment_method is None:
        raise HTTPException(status_code=400, detail="Payment method not found")
    return {"payment_method_id": payment_method.payment_method_id, "name": payment_method.name, "email": payment_method.email}

@router.post('/')
async def create_payment_method(user_id: int, method_type: str, provider: str, account_number: str, db: Session = Depends(get_db)):
    try:
        new_payment_method = PaymentMethods(user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
        db.add(new_payment_method)
        db.commit()
        db.refresh(new_payment_method)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"payment_method_id": new_payment_method.payment_method_id, "name": new_payment_method.name, "email": new_payment_method.email}

@router.put('/{payment_method_id}')
async def update_payment_method(payment_method_id: int, user_id: int = None, method_type: str = None, provider: str = None, account_number: str = None, db: Session = Depends(get_db)):
    payment_method = db.query(PaymentMethods).filter(PaymentMethods.payment_method_id == payment_method_id).first()
    if payment_method is None:
        raise HTTPException(status_code=400, detail="Payment method not found")

    if user_id:
        payment_method.user_id = user_id
    if provider:
        payment_method.provider = provider
    if method_type:
        payment_method.method_type = method_type
    if account_number:
        payment_method.account_number = account_number

    db.commit()
    db.refresh(payment_method)
    return {"payment_method_id": payment_method.payment_method_id, "name": payment_method.name, "email": payment_method.email}

@router.delete('/{payment_method_id}')
async def delete_payment_method(payment_method_id: int, db: Session = Depends(get_db)):
    payment_method = db.query(PaymentMethods).filter(PaymentMethods.payment_method_id == payment_method_id).first()
    if payment_method is None:
        raise HTTPException(status_code=400, detail="Payment method not found")

    db.delete(payment_method)
    db.commit()
    return {"message": "Payment method deleted successfully"}