from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import PayPerView

router = APIRouter(
    prefix="/pay_per_views",
    tags=["pay_per_views"]
)

@router.get('/', response_model=list[dict])
async def get_pay_per_views(db: Session = Depends(get_db)):
    pay_per_views = db.query(PayPerView).all()
    if pay_per_views is None:
        raise HTTPException(status_code=400, detail="Pay Per Views not found")
    return [{"pay_per_view_id": pay_per_view.pay_per_view_id, "amount": pay_per_view.amount, "content_id": pay_per_view.content_id} for pay_per_view in pay_per_views]

@router.get('/{pay_per_view_id}', response_model=dict)
async def get_pay_per_view(pay_per_view_id: int, db: Session = Depends(get_db)):
    pay_per_view = db.query(PayPerView).filter(PayPerView.pay_per_view_id == pay_per_view_id).first()
    if pay_per_view is None:
        raise HTTPException(status_code=400, detail="Pay per view not found")
    return {"pay_per_view_id": pay_per_view.pay_per_view_id, "amount": pay_per_view.amount, "content_id": pay_per_view.content_id}

@router.post('/', response_model=dict)
async def create_pay_per_view(amount: float, content_id: float, db: Session = Depends(get_db)):
    try:
        new_pay_per_view = PayPerView(amount=amount, content_id=content_id)
        db.add(new_pay_per_view)
        db.commit()
        db.refresh(new_pay_per_view)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"pay_per_view_id": new_pay_per_view.pay_per_view_id, "amount": new_pay_per_view.amount, "content_id": new_pay_per_view.content_id}

@router.put('/{pay_per_view_id}', response_model=dict)
async def update_pay_per_view(pay_per_view_id: int, amount: float = None, content_id: float = None, db: Session = Depends(get_db)):
    pay_per_view = db.query(PayPerView).filter(PayPerView.pay_per_view_id == pay_per_view_id).first()
    if pay_per_view is None:
        raise HTTPException(status_code=400, detail="Pay per view not found")

    if amount:
        pay_per_view.amount = amount
    if content_id:
        pay_per_view.content_id = content_id

    db.commit()
    db.refresh(pay_per_view)
    return {"pay_per_view_id": pay_per_view.pay_per_view_id, "amount": pay_per_view.amount, "content_id": pay_per_view.content_id}

@router.delete('/{pay_per_view_id}', response_model=dict)
async def delete_pay_per_view(pay_per_view_id: int, db: Session = Depends(get_db)):
    pay_per_view = db.query(PayPerView).filter(PayPerView.pay_per_view_id == pay_per_view_id).first()
    if pay_per_view is None:
        raise HTTPException(status_code=400, detail="Pay per view not found")

    db.delete(pay_per_view)
    db.commit()
    return {"message": "Pay per view deleted successfully"}