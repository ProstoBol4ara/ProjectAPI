from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Coupons

router = APIRouter(
    prefix="/coupons",
    tags=["coupons"]
)

@router.get('/')
async def get_coupons(db: Session = Depends(get_db)):
    coupons = db.query(Coupons).all()
    if coupons is None:
        raise HTTPException(status_code=400, detail="Coupons not found")
    return [{"coupon_id": coupon.coupon_id, "code": coupon.code, "discount_percentage": coupon.discount_percentage, "valid_from": coupon.valid_from, "valid_until": coupon.valid_until} for coupon in coupons]

@router.get('/{coupon_id}')
async def get_coupon(coupon_id: int, db: Session = Depends(get_db)):
    coupon = db.query(Coupons).filter(Coupons.coupon_id == coupon_id).first()
    if coupon is None:
        raise HTTPException(status_code=400, detail="Coupon not found")
    return {"coupon_id": coupon.coupon_id, "code": coupon.code, "discount_percentage": coupon.discount_percentage, "valid_from": coupon.valid_from, "valid_until": coupon.valid_until}

@router.post('/')
async def create_coupon(code: str, discount_percentage: float, valid_from: str = None, valid_until: str = None, db: Session = Depends(get_db)):
    try:
        if not valid_from is None:
            valid_from = datetime.strptime(valid_from, '%d.%m.%Y').date()
        if not valid_until is None:
            valid_until = datetime.strptime(valid_until, '%d.%m.%Y').date()
        new_coupon = Coupons(code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)
        db.add(new_coupon)
        db.commit()
        db.refresh(new_coupon)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"coupon_id": new_coupon.coupon_id, "code": new_coupon.code, "discount_percentage": new_coupon.discount_percentage, "valid_from": new_coupon.valid_from, "valid_until": new_coupon.valid_until}

@router.put('/{coupon_id}')
async def update_coupon(coupon_id: int, code: str = None, discount_percentage: float = None, valid_from: str = None, valid_until: str = None, db: Session = Depends(get_db)):
    try:
        coupon = db.query(Coupons).filter(Coupons.coupon_id == coupon_id).first()
        if coupon is None:
            raise HTTPException(status_code=400, detail="Coupon not found")

        if code:
            coupon.code = code
        if discount_percentage:
            coupon.discount_percentage = discount_percentage
        if valid_from:
            coupon.valid_from = datetime.strptime(valid_from, '%d.%m.%Y').date()
        if valid_until:
            coupon.valid_until = datetime.strptime(valid_until, '%d.%m.%Y').date()

        db.commit()
        db.refresh(coupon)
    except:
        raise HTTPException(status_code=400, detail="Update failed")
    return {"coupon_id": coupon.coupon_id, "code": coupon.code, "discount_percentage": coupon.discount_percentage, "valid_from": coupon.valid_from, "valid_until": coupon.valid_until}

@router.delete('/{coupon_id}')
async def delete_coupon(coupon_id: int, db: Session = Depends(get_db)):
    coupon = db.query(Coupons).filter(Coupons.coupon_id == coupon_id).first()
    if coupon is None:
        raise HTTPException(status_code=400, detail="Coupon not found")

    db.delete(coupon)
    db.commit()
    return {"message": "Coupon deleted successfully"}