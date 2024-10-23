from fastapi import APIRouter, HTTPException, Depends
from repositories import PayPerViewRepository
from database import AsyncSession, get_db
from services import PayPerViewService

router = APIRouter(
    prefix="/pay_per_views",
    tags=["pay_per_views"]
)

@router.get('/')
async def get_pay_per_views(db: AsyncSession = Depends(get_db)):
    pay_per_views = await PayPerViewService(PayPerViewRepository(db)).get_pay_per_views()
    if pay_per_views is None:
        raise HTTPException(status_code=400, detail="Pay Per Views not found")
    return pay_per_views

@router.get('/{pay_per_view_id}')
async def get_pay_per_view(pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    pay_per_view = await PayPerViewService(PayPerViewRepository(db)).get_pay_per_view(pay_per_view_id=pay_per_view_id)
    if pay_per_view is None:
        raise HTTPException(status_code=400, detail="Pay per view not found")
    return pay_per_view

@router.post('/')
async def create_pay_per_view(amount: float, content_id: float, db: AsyncSession = Depends(get_db)):
    try:
        new_pay_per_view = await PayPerViewPayPerViewService(PayPerViewRepository(db)).create_pay_per_view(amount=amount, content_id=content_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_pay_per_view

@router.put('/{pay_per_view_id}')
async def update_pay_per_view(pay_per_view_id: int, amount: float = None, content_id: float = None, db: AsyncSession = Depends(get_db)):
    try:
        pay_per_view = await PayPerViewService(PayPerViewRepository(db)).update_pay_per_view(pay_per_view_id=pay_per_view_id)
        if pay_per_view is None:
            raise HTTPException(status_code=400, detail="Pay per view not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return pay_per_view

@router.delete('/{pay_per_view_id}')
async def delete_pay_per_view(pay_per_view_id: int, db: AsyncSession = Depends(get_db)):
    if not await PayPerViewService(PayPerViewRepository(db)).delete_pay_per_view(pay_per_view_id=pay_per_view_id):
        raise HTTPException(status_code=400, detail="Pay per view not found")
    return {"message": "Pay per view deleted successfully"}