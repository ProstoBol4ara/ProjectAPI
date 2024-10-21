from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Payments

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

@router.get('/')
async def get_payments(db: Session = Depends(get_db)):
    payments = db.query(Payments).all()
    if payments is None:
        raise HTTPException(status_code=400, detail="Payments not found")
    return [{"payment_id": payment.payment_id, "pay_per_view_id": payment.pay_per_view_id, "payment_method_id": payment.payment_method_id} for payment in payments]

@router.get('/{payment_id}')
async def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payments).filter(Payments.payment_id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=400, detail="User not found")
    return {"payment_id": payment.payment_id, "pay_per_view_id": payment.pay_per_view_id, "payment_method_id": payment.payment_method_id}

@router.post('/')
async def create_payment(payment_method_id: int, pay_per_view_id: int, db: Session = Depends(get_db)):
    try:
        new_payment = Payments(payment_method_id = payment_method_id, pay_per_view_id = pay_per_view_id)
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"payment_id": new_payment.payment_id, "payment_method_id": new_payment.payment_method_id, "pay_per_view_id": new_payment.pay_per_view_id}

@router.put('/{payment_id}')
async def update_payment(payment_id: int, payment_method_id: int, pay_per_view_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payments).filter(Payments.payment_id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=400, detail="User not found")

    if pay_per_view_id:
        payment.pay_per_view_id = pay_per_view_id
    if payment_method_id:
        payment.payment_method_id = payment_method_id

    db.commit()
    db.refresh(payment)
    return {"payment_id": payment.payment_id, "pay_per_view_id": payment.pay_per_view_id, "payment_method_id": payment.payment_method_id}

@router.delete('/{payment_id}')
async def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payments).filter(Payments.payment_id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=400, detail="User not found")

    db.delete(payment)
    db.commit()
    return {"message": "User deleted successfully"}