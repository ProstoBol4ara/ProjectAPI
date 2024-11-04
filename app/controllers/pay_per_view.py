from repositories import PayPerViewRepository
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from services import PayPerViewService
from fastapi import APIRouter, Depends
from responses.pay_per_view import *

router = APIRouter(prefix="/pay_per_views", tags=["pay_per_views"])


@router.get("/", summary="Fetch all pay per views", responses=get_pay_per_views)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/pay_per_views
    """

    pay_per_views = await PayPerViewService(PayPerViewRepository(db)).get_all()
    return pay_per_views


@router.get(
    "/{pay_per_view_id}", summary="Fetch pay per view by id", responses=get_pay_per_view
)
@handle_exceptions(status_code=400)
async def get_one(pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/pay_per_views/1
    """

    pay_per_view = await PayPerViewService(PayPerViewRepository(db)).get_one(
        pay_per_view_id=pay_per_view_id
    )
    return pay_per_view


@router.post("/", summary="Create pay per view", responses=create_pay_per_view)
@handle_exceptions(status_code=400)
async def create(amount: float, content_id: float, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/pay_per_views/
        {
            "pay_per_view_id": 1,
            "amount": 100,
            "content_id": 1
        }
    """

    new_pay_per_view = await PayPerViewService(PayPerViewRepository(db)).create(
        amount=amount, content_id=content_id
    )
    return new_pay_per_view


@router.put(
    "/{pay_per_view_id}",
    summary="Update pay per view by id",
    responses=update_pay_per_view,
)
@handle_exceptions(status_code=400)
async def update(
    pay_per_view_id: int,
    amount: float = None,
    content_id: float = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/pay_per_views/1
        {
            "pay_per_view_id": 1,
            "amount": 200
        }
    """

    pay_per_view = await PayPerViewService(PayPerViewRepository(db)).update(
        pay_per_view_id=pay_per_view_id, amount=amount, content_id=content_id
    )

    return pay_per_view


@router.delete(
    "/{pay_per_view_id}",
    summary="Delete pay per view by id",
    responses=delete_pay_per_view,
)
@handle_exceptions(status_code=400)
async def delete(pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/pay_per_views/1
    """

    await PayPerViewService(PayPerViewRepository(db)).delete(
        pay_per_view_id=pay_per_view_id
    )
    return {"message": "Pay per view deleted successfully"}
