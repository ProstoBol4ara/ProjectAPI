from repositories import PaymentMethodsRepository
from api_decorators import handle_exceptions
from services import PaymentMethodsService
from database import AsyncSession, get_db
from responses.payment_methods import *
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/payment_methods", tags=["payment_methods"])


@router.get("/", summary="Fetch all payment methods", responses=get_payment_methods)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/payment_methods
    """

    payment_methods = await PaymentMethodsService(
        PaymentMethodsRepository(db)
    ).get_all()
    return payment_methods


@router.get(
    "/{payment_method_id}",
    summary="Fetch payment method by id",
    responses=get_payment_method,
)
@handle_exceptions(status_code=400)
async def get_one(payment_method_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/payment_methods/1
    """

    payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).get_one(
        payment_method_id=payment_method_id
    )
    return payment_method


@router.post("/", summary="Create payment method", responses=create_payment_method)
@handle_exceptions(status_code=400)
async def create(
    user_id: int,
    method_type: str,
    provider: str,
    account_number: str,
    db: AsyncSession = Depends(get_db),
):
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

    new_payment_method = await PaymentMethodsService(
        PaymentMethodsRepository(db)
    ).create(
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )

    return new_payment_method


@router.put(
    "/{payment_method_id}",
    summary="Update payment method by id",
    responses=update_payment_method,
)
@handle_exceptions(status_code=400)
async def update(
    payment_method_id: int,
    user_id: int = None,
    method_type: str = None,
    provider: str = None,
    account_number: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/payment_methods/1
        {
            "payment_method_id": 1,
            "provider": "bbb"
        }
    """

    payment_method = await PaymentMethodsService(PaymentMethodsRepository(db)).update(
        payment_method_id=payment_method_id,
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )
    return payment_method


@router.delete(
    "/{payment_method_id}",
    summary="Delete payment method by id",
    responses=delete_payment_method,
)
@handle_exceptions(status_code=400)
async def delete(payment_method_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/payment_methods/1
    """

    await PaymentMethodsService(PaymentMethodsRepository(db)).delete(
        payment_method_id=payment_method_id
    )
    return {"message": "Payment method deleted successfully"}
