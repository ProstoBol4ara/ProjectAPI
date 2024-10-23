from fastapi import APIRouter, HTTPException, Depends
from repositories import PaymentMethodsRepository
from services import PaymentMethodsService
from database import AsyncSession, get_db

router = APIRouter(
    prefix="/payment_methods",
    tags=["payment_methods"]
)

@router.get('/')
async def get_payment_methods(db: AsyncSession = Depends(get_db)):
    payment_methods = await PaymentMethodsService(PaymentMethodsRepository(db)).get_payment_methods()
    if payment_methods is None:
        raise HTTPException(status_code=400, detail="PaymentMethods not found")
    return payment_methods

@router.get('/{payment_method_id}')
async def get_payment_method(payment_method_id: int, db: AsyncSession = Depends(get_db)):
    payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).get_payment_method(payment_method_id=payment_method_id)
    if payment_method is None:
        raise HTTPException(status_code=400, detail="Payment method not found")
    return payment_method

@router.post('/')
async def create_payment_method(user_id: int, method_type: str, provider: str, account_number: str, db: AsyncSession = Depends(get_db)):
    try:
        new_payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).create_payment_method(user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_payment_method

@router.put('/{payment_method_id}')
async def update_payment_method(payment_method_id: int, user_id: int = None, method_type: str = None, provider: str = None, account_number: str = None, db: AsyncSession = Depends(get_db)):
    try:
        payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).update_payment_method(payment_method_id=payment_method_id, user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
        if payment_method is None:
            raise HTTPException(status_code=400, detail="Payment method not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return payment_method

@router.delete('/{payment_method_id}')
async def delete_payment_method(payment_method_id: int, db: AsyncSession = Depends(get_db)):
    if not await PaymentMethodsService(PaymentMethodsRepository(db)).delete_payment_method(payment_method_id=payment_method_id):
        raise HTTPException(status_code=400, detail="Payment method not found")
    return {"message": "Payment method deleted successfully"}