from fastapi import APIRouter, HTTPException, Depends
from repositories import CouponsRepository
from database import AsyncSession, get_db
from services import CouponsService
from responses.coupons import *

router = APIRouter(
    prefix="/coupons",
    tags=["coupons"]
)

@router.get('/', summary="Fetch all coupons", responses=get_coupons)
async def get_coupons(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/coupons
    """

    coupons = await CouponsService(CouponsRepository(db)).get_coupons()
    if coupons is None:
        raise HTTPException(status_code=400, detail="Coupons not found")
    return coupons

@router.get('/{coupon_id}', summary="Fetch coupon by id", responses=get_coupon)
async def get_coupon(coupon_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/coupons/1
    """

    coupon = await CouponsService(CouponsRepository(db)).get_coupon(coupon_id=coupon_id)
    if coupon is None:
        raise HTTPException(status_code=400, detail="Coupon not found")
    return coupon

@router.post('/', summary="Create coupon", responses=create_coupon)
async def create_coupon(code: str, discount_percentage: float, valid_from: str = None, valid_until: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/coupons/
        {
            "coupon_id": 1,
            "code": "aaa",
            "discount_percentage": "0.05",
            "valid_from": "2000-10-10",
            "valid_until": "2000-11-11"
        }
    """

    try:
        new_coupon = await CouponsService(CouponsRepository(db)).create_coupon(code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return new_coupon

@router.put('/{coupon_id}', summary="Update coupon by id", responses=update_coupon)
async def update_coupon(coupon_id: int, code: str = None, discount_percentage: float = None, valid_from: str = None, valid_until: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/coupons/1
        {
            "coupon_id": 1,
            "code": "bbb"
        }
    """

    try:
        coupon = await CouponsService(CouponsRepository(db)).update_coupon(coupon_id=coupon_id, code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)
        if coupon is None:
            raise HTTPException(status_code=400, detail="Coupon not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return coupon

@router.delete('/{coupon_id}', summary="Delete coupon by id", responses=delete_coupon)
async def delete_coupon(coupon_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/coupons/1
    """

    if not await CouponsService(CouponsRepository(db)).delete_coupon(coupon_id=coupon_id):
        raise HTTPException(status_code=400, detail="Coupon not found")
    return {"message": "Coupon deleted successfully"}
