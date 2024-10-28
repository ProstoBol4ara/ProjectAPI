from fastapi import APIRouter, HTTPException, Depends
from database import AsyncSession, get_db
from repositories import UsersRepository
from services import UsersService
from responses.users import *

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get('/', summary="Fetch all users", responses=get_users)
async def get_users(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/users
    """

    users = await UsersService(UsersRepository(db)).get_users()
    if users is None:
        raise HTTPException(stlatus_code=400, detail="Users not found")
    return users

@router.get('/{user_id}', summary="Fetch user by id", responses=get_user)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/users/1
    """

    user = await UsersService(UsersRepository(db)).get_user(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return user

@router.post('/', summary="Create user", responses=create_user)
async def create_user(username: str, email: str, password: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/users/
        {
            "username": "aaa",
            "email": "aaa@aaa.com",
            "password": "aaa"
        }
    """

    try:
        new_user = await UsersService(UsersRepository(db)).create_user(username=username, email=email, password=password)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_user

@router.put('/{user_id}', summary="Update user by id", responses=update_user)
async def update_user(user_id: int, username: str = None, email: str = None, password: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/users/1
        {
            "user_id": 1,
            "username": "bbb"
        }
    """

    try:
        user = await UsersService(UsersRepository(db)).update_user(user_id=user_id, username=username, email=email, password=password)
        if user is None:
            raise HTTPException(status_code=400, detail="User not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return user

@router.delete('/{user_id}', summary="Delete user by id", responses=delete_user)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/users/1
    """

    if not await UsersService(UsersRepository(db)).delete_user(user_id=user_id):
        raise HTTPException(status_code=400, detail="User not found")
    return {"message": "User deleted successfully"}
