from fastapi import APIRouter, HTTPException
from database import get_depends
from models import Users

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get('/', response_model=Users)
async def get_users(db: Session = get_depends()):
    users = db.query(Users)
    if users is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

@router.get('/{user_id}', response_model=Users)
async def get_user(user_id: int, db: Session = get_depends()):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post('/', response_model=Users)
async def create_user(username: str, email: str = '', password: str = '', db: Session = get_depends()):
    new_user = Users(username=username, email=email, password_hash=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}

@router.put('/{user_id}', response_model=Users)
async def update_user(user_id: int, username: str = None, email: str = None, password: str = None, db: Session = get_depends()):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if username:
        user.name = name
    if email:
        user.email = email
    if password:
        user.password = password

    db.commit()
    db.refresh(user)
    return {"id": user.id, "name": user.name, "email": user.email}

@router.delete('/{user_id}', response_model=Users)
async def delete_user(user_id: int, db: Session = get_depends()):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}