from fastapi import APIRouter, HTTPException, Depends
from repositories import PaymentsRepository
from database import AsyncSession, get_db
from services import PaymentsService

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

@router.get('/')
async def get_payments(db: AsyncSession = Depends(get_db)):
    payments = await PaymentsService(PaymentsRepository(db)).get_payments()
    if payments is None:
        raise HTTPException(status_code=400, detail="Payments not found")
    return payments

@router.get('/{payment_id}')
async def get_payment(payment_id: int, db: AsyncSession = Depends(get_db)):
    payment = await PaymentsService(PaymentsRepository(db)).get_payment(payment_id=payment_id)
    if payment is None:
        raise HTTPException(status_code=400, detail="User not found")
    return payment

@router.post('/')
async def create_payment(payment_method_id: int, pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_payment = await PaymentsService(PaymentsRepository(db)).create_payment(payment_method_id = payment_method_id, pay_per_view_id = pay_per_view_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_payment

@router.put('/{payment_id}')
async def update_payment(payment_id: int, payment_method_id: int, pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    try:
        payment = await PaymentsService(PaymentsRepository(db)).update_payment(payment_id=payment_id, payment_method_id = payment_method_id, pay_per_view_id = pay_per_view_id)
        if payment is None:
            raise HTTPException(status_code=400, detail="User not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return payment

@router.delete('/{payment_id}')
async def delete_payment(payment_id: int, db: AsyncSession = Depends(get_db)):
    if not await PaymentsService(PaymentsRepository(db)).delete_payment(payment_id=payment_id):
        raise HTTPException(status_code=400, detail="User not found")
    return {"message": "User deleted successfully"}