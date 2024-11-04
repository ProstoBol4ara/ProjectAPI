from api_decorators import handle_exceptions
from repositories import PaymentsRepository
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import PaymentsService
from responses.payments import *

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("/", summary="Fetch all payments", responses=get_payments)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/payments
    """

    payments = await PaymentsService(PaymentsRepository(db)).get_all()
    return payments


@router.get("/{payment_id}", summary="Fetch payment by id", responses=get_payment)
@handle_exceptions(status_code=400)
async def get_one(payment_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/payments/1
    """

    payment = await PaymentsService(PaymentsRepository(db)).get_one(
        payment_id=payment_id
    )
    return payment


@router.post("/", summary="Create payment", responses=create_payment)
@handle_exceptions(status_code=400)
async def create(
    payment_method_id: int, pay_per_view_id: int, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        POST /api/payments/
        {
            "payment_id": 1,
            "pay_per_view_id": 1,
            "payment_method_id": 1
        }
    """

    new_payment = await PaymentsService(PaymentsRepository(db)).create(
        payment_method_id=payment_method_id, pay_per_view_id=pay_per_view_id
    )

    return new_payment


@router.put("/{payment_id}", summary="Update payment by id", responses=update_payment)
@handle_exceptions(status_code=400)
async def update(
    payment_id: int,
    payment_method_id: int,
    pay_per_view_id: int,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/payments/1
        {
            "payment_id": 1,
            "payment_method_id": 2
        }
    """

    payment = await PaymentsService(PaymentsRepository(db)).update(
        payment_id=payment_id,
        payment_method_id=payment_method_id,
        pay_per_view_id=pay_per_view_id,
    )

    return payment


@router.delete(
    "/{payment_id}", summary="Delete payment by id", responses=delete_payment
)
@handle_exceptions(status_code=400)
async def delete(payment_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/payments/1
    """

    await PaymentsService(PaymentsRepository(db)).delete(payment_id=payment_id)
    return {"message": "Payment deleted successfully"}
