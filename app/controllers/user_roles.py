from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import UserRoles

router = APIRouter(
    prefix="/user_roles",
    tags=["user_roles"]
)

@router.get('/')
async def get_user_roles(db: Session = Depends(get_db)):
    user_roles = db.query(UserRoles).all()
    if user_roles is None:
        raise HTTPException(status_code=400, detail="User roles not found")
    return [{"user_role_id": user_role.user_role_id, "user_id": user_role.user_id, "role_id": user_role.role_id} for user_role in user_roles]

@router.get('/{user_role_id}')
async def get_user_role(user_role_id: int, db: Session = Depends(get_db)):
    user_role = db.query(UserRoles).filter(UserRoles.user_role_id == user_role_id).first()
    if user_role is None:
        raise HTTPException(status_code=400, detail="User role not found")
    return {"user_role_id": user_role.user_role_id, "user_id": user_role.user_id, "role_id": user_role.role_id}

@router.post('/')
async def create_user_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    try:
        new_user_role = UserRoles(user_id=user_id, role_id=role_id)
        db.add(new_user_role)
        db.commit()
        db.refresh(new_user_role)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"user_role_id": new_user_role.user_role_id, "user_id": new_user_role.user_id, "role_id": new_user_role.role_id}

@router.put('/{user_role_id}')
async def update_user_role(user_role_id: int, db: Session = Depends(get_db)):
    user_role = db.query(UserRoles).filter(UserRoles.user_role_id == user_role_id).first()
    if user_role is None:
        raise HTTPException(status_code=400, detail="User role not found")

    db.commit()
    db.refresh(user)
    return {"user_role_id": user_role.user_role_id, "user_id": user_role.user_id, "role_id": user_role.role_id}

@router.delete('/{user_role_id}')
async def delete_user_role(user_role_id: int, db: Session = Depends(get_db)):
    user = db.query(UserRoles).filter(UserRoles.user_role_id == user_role_id).first()
    if user is None:
        raise HTTPException(status_code=400, detail="User role not found")

    db.delete(user)
    db.commit()
    return {"message": "User role deleted successfully"}