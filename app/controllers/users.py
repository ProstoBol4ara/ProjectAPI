from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from crypt import hash_password
from models.users import Users

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get('/', response_model=list[dict])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    if users is None:
        raise HTTPException(status_code=400, detail="Users not found")
    return [{"user_id": user.user_id, "username": user.username} for user in users]

@router.get('/{user_id}', response_model=None)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return {"user_id": user.user_id, "username": user.username}

@router.post('/', response_model=dict)
async def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    try:
        password = hash_password(password)
        new_user = Users(username=username, email=email, password_hash=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"user_id": new_user.user_id, "username": new_user.username, "email": new_user.email}

@router.put('/{user_id}', response_model=dict)
async def update_user(user_id: int, username: str = None, email: str = None, password: str = None, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    if password:
        user.password = hash_password(password)
    if username:
        user.username = username
    if email:
        user.email = email

    db.commit()
    db.refresh(user)
    return {"user_id": user.user_id, "username": user.username, "email": user.email}

@router.delete('/{user_id}', response_model=dict)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}