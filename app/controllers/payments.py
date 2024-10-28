from api_decorators import handle_exceptions
from repositories import PaymentsRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import PaymentsService
from responses.payments import *

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all payments", responses=get_payments)
async def get_payments(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/payments
    """

    payments = await PaymentsService(PaymentsRepository(db)).get_payments()
    return payments

@handle_exceptions(status_code=400)
@router.get('/{payment_id}', summary="Fetch payment by id", responses=get_payment)
async def get_payment(payment_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/payments/1
    """

    payment = await PaymentsService(PaymentsRepository(db)).get_payment(payment_id=payment_id)
    return payment

@handle_exceptions(status_code=400)
@router.post('/', summary="Create payment", responses=create_payment)
async def create_payment(payment_method_id: int, pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/payments/
        {
            "payment_id": 1,
            "pay_per_view_id": 1,
            "payment_method_id": 1
        }
    """

    new_payment = await PaymentsService(PaymentsRepository(db)).create_payment(payment_method_id = payment_method_id, pay_per_view_id = pay_per_view_id)
    return new_payment

@handle_exceptions(status_code=400)
@router.put('/{payment_id}', summary="Update payment by id", responses=update_payment)
async def update_payment(payment_id: int, payment_method_id: int, pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/payments/1
        {
            "payment_id": 1,
            "payment_method_id": 2
        }
    """

    payment = await PaymentsService(PaymentsRepository(db)).update_payment(payment_id=payment_id, payment_method_id = payment_method_id, pay_per_view_id = pay_per_view_id)
    return payment

@handle_exceptions(status_code=400)
@router.delete('/{payment_id}', summary="Delete payment by id", responses=delete_payment)
async def delete_payment(payment_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/payments/1
    """

    await PaymentsService(PaymentsRepository(db)).delete_payment(payment_id=payment_id)
    return {"message": "Payment deleted successfully"}
