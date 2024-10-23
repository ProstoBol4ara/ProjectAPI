from fastapi import APIRouter, HTTPException, Depends
from database import AsyncSession, get_db
from repositories import UsersRepository
from services import UsersService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get('/')
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await UsersService(UsersRepository(db)).get_users()
    if users is None:
        raise HTTPException(stlatus_code=400, detail="Users not found")
    return users

@router.get('/{user_id}')
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await UsersService(UsersRepository(db)).get_user(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return user

@router.post('/')
async def create_user(username: str, email: str, password: str, db: AsyncSession = Depends(get_db)):
    try:
        new_user = await UsersService(UsersRepository(db)).create_user(username=username, email=email, password=password)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_user

@router.put('/{user_id}')
async def update_user(user_id: int, username: str = None, email: str = None, password: str = None, db: AsyncSession = Depends(get_db)):
    try:
        user = await UsersService(UsersRepository(db)).update_user(user_id=user_id, username=username, email=email, password=password)
        if user is None:
            raise HTTPException(status_code=400, detail="User not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return user

@router.delete('/{user_id}')
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    if not await UsersService(UsersRepository(db)).delete_user(user_id=user_id):
        raise HTTPException(status_code=400, detail="User not found")
    return {"message": "User deleted successfully"}