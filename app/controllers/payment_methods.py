from fastapi import APIRouter, HTTPException, Depends
from repositories import PaymentMethodsRepository
from services import PaymentMethodsService
from database import AsyncSession, get_db
from responses.payment_methods import *

router = APIRouter(
    prefix="/payment_methods",
    tags=["payment_methods"]
)

@router.get('/', summary="Fetch all payment methods", responses=get_payment_methods)
async def get_payment_methods(db: AsyncSession = Depends(get_db)):
    """
    Query example:
        
        GET /api/payment_methods
    """

    payment_methods = await PaymentMethodsService(PaymentMethodsRepository(db)).get_payment_methods()
    if payment_methods is None:
        raise HTTPException(status_code=400, detail="PaymentMethods not found")
    return payment_methods

@router.get('/{payment_method_id}', summary="Fetch payment method by id", responses=get_payment_method)
async def get_payment_method(payment_method_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/payment_methods/1
    """

    payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).get_payment_method(payment_method_id=payment_method_id)
    if payment_method is None:
        raise HTTPException(status_code=400, detail="Payment method not found")
    return payment_method

@router.post('/', summary="Create payment method", responses=create_payment_method)
async def create_payment_method(user_id: int, method_type: str, provider: str, account_number: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/payment_methods/
        {
            "payment_method_id": 1, 
            "user_id": 1, 
            "method_type": "aaa", 
            "provider": "aaa", 
            "account_number": "XXXXX-XXXXX-XXXXX-XXXXX"
        }
    """

    try:
        new_payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).create_payment_method(user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_payment_method

@router.put('/{payment_method_id}', summary="Update payment method by id", responses=update_payment_method)
async def update_payment_method(payment_method_id: int, user_id: int = None, method_type: str = None, provider: str = None, account_number: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/payment_methods/1
        {
            "payment_method_id": 1, 
            "provider": "bbb"
        }
    """

    try:
        payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).update_payment_method(payment_method_id=payment_method_id, user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
        if payment_method is None:
            raise HTTPException(status_code=400, detail="Payment method not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return payment_method

@router.delete('/{payment_method_id}', summary="Delete payment method by id", responses=delete_payment_method)
async def delete_payment_method(payment_method_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/payment_methods/1
    """

    if not await PaymentMethodsService(PaymentMethodsRepository(db)).delete_payment_method(payment_method_id=payment_method_id):
        raise HTTPException(status_code=400, detail="Payment method not found")
    return {"message": "Payment method deleted successfully"}