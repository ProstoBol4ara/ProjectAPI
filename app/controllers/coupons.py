from fastapi import APIRouter, HTTPException, Depends
from repositories import CouponsRepository
from database import AsyncSession, get_db
from services import CouponsService

router = APIRouter(
    prefix="/coupons",
    tags=["coupons"]
)

@router.get('/')
async def get_coupons(db: AsyncSession = Depends(get_db)):
    coupons = await CouponsService(CouponsRepository(db)).get_coupons()
    if coupons is None:
        raise HTTPException(status_code=400, detail="Coupons not found")
    return coupons

@router.get('/{coupon_id}')
async def get_coupon(coupon_id: int, db: AsyncSession = Depends(get_db)):
    coupon = await CouponsService(CouponsRepository(db)).get_coupon(coupon_id=coupon_id)
    if coupon is None:
        raise HTTPException(status_code=400, detail="Coupon not found")
    return coupon

@router.post('/')
async def create_coupon(code: str, discount_percentage: float, valid_from: str = None, valid_until: str = None, db: AsyncSession = Depends(get_db)):
    try:
        new_coupon = await CouponsService(CouponsRepository(db)).create_coupon(code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return new_coupon

@router.put('/{coupon_id}')
async def update_coupon(coupon_id: int, code: str = None, discount_percentage: float = None, valid_from: str = None, valid_until: str = None, db: AsyncSession = Depends(get_db)):
    try:
        coupon = await CouponsService(CouponsRepository(db)).update_coupon(coupon_id=coupon_id, code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)
        if coupon is None:
            raise HTTPException(status_code=400, detail="Coupon not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return coupon

@router.delete('/{coupon_id}')
async def delete_coupon(coupon_id: int, db: AsyncSession = Depends(get_db)):
    if not await CouponsService(CouponsRepository(db)).delete_coupon(coupon_id=coupon_id):
        raise HTTPException(status_code=400, detail="Coupon not found")
    return {"message": "Coupon deleted successfully"}