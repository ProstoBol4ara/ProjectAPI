from fastapi import APIRouter, HTTPException, Depends
from repositories import PayPerViewRepository
from database import AsyncSession, get_db
from services import PayPerViewService
from responses.pay_per_view import *

router = APIRouter(
    prefix="/pay_per_views",
    tags=["pay_per_views"]
)

@router.get('/', summary="Fetch all pay per views", responses=get_pay_per_views)
async def get_pay_per_views(db: AsyncSession = Depends(get_db)):
    """
    Query example:
        
        GET /api/pay_per_views
    """

    pay_per_views = await PayPerViewService(PayPerViewRepository(db)).get_pay_per_views()
    if pay_per_views is None:
        raise HTTPException(status_code=400, detail="Pay per views not found")
    return pay_per_views

@router.get('/{pay_per_view_id}', summary="Fetch pay per view by id", responses=get_pay_per_view)
async def get_pay_per_view(pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/pay_per_views/1
    """

    pay_per_view = await PayPerViewService(PayPerViewRepository(db)).get_pay_per_view(pay_per_view_id=pay_per_view_id)
    if pay_per_view is None:
        raise HTTPException(status_code=400, detail="Pay per view not found")
    return pay_per_view

@router.post('/', summary="Create pay per view", responses=create_pay_per_view)
async def create_pay_per_view(amount: float, content_id: float, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/pay_per_views/
        {
            "pay_per_view_id": 1, 
            "amount": 100, 
            "content_id": 1
        }
    """

    try:
        new_pay_per_view = await PayPerViewPayPerViewService(PayPerViewRepository(db)).create_pay_per_view(amount=amount, content_id=content_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_pay_per_view

@router.put('/{pay_per_view_id}', summary="Update pay per view by id", responses=update_pay_per_view)
async def update_pay_per_view(pay_per_view_id: int, amount: float = None, content_id: float = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/pay_per_views/1
        {
            "pay_per_view_id": 1, 
            "amount": 200
        }
    """

    try:
        pay_per_view = await PayPerViewService(PayPerViewRepository(db)).update_pay_per_view(pay_per_view_id=pay_per_view_id)
        if pay_per_view is None:
            raise HTTPException(status_code=400, detail="Pay per view not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return pay_per_view

@router.delete('/{pay_per_view_id}', summary="Delete pay per view by id", responses=delete_pay_per_view)
async def delete_pay_per_view(pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/pay_per_views/1
    """

    if not await PayPerViewService(PayPerViewRepository(db)).delete_pay_per_view(pay_per_view_id=pay_per_view_id):
        raise HTTPException(status_code=400, detail="Pay per view not found")
    return {"message": "Pay per view deleted successfully"}