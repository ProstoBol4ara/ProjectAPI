from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from repositories import UsersRepository
from fastapi import APIRouter, Depends
from services import UsersService
from responses.users import *

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", summary="Fetch all users", responses=get_users)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/users
    """

    users = await UsersService(UsersRepository(db)).get_all()
    return users


@router.get("/{user_id}", summary="Fetch user by id", responses=get_user)
@handle_exceptions(status_code=400)
async def get_one(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/users/1
    """

    user = await UsersService(UsersRepository(db)).get_one(user_id=user_id)
    return user


@router.post("/", summary="Create user", responses=create_user)
@handle_exceptions(status_code=400)
async def create(
    username: str, email: str, password: str, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        POST /api/users/
        {
            "username": "aaa",
            "email": "aaa@aaa.com",
            "password": "aaa"
        }
    """

    new_user = await UsersService(UsersRepository(db)).create(
        username=username, email=email, password=password
    )
    return new_user


@router.put("/{user_id}", summary="Update user by id", responses=update_user)
@handle_exceptions(status_code=400)
async def update(
    user_id: int,
    username: str = None,
    email: str = None,
    password: str = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Query example:

        PUT /api/users/1
        {
            "user_id": 1,
            "username": "bbb"
        }
    """

    user = await UsersService(UsersRepository(db)).update(
        user_id=user_id, username=username, email=email, password=password
    )
    return user


@router.delete("/{user_id}", summary="Delete user by id", responses=delete_user)
@handle_exceptions(status_code=400)
async def delete(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/users/1
    """

    await UsersService(UsersRepository(db)).delete(user_id=user_id)
    return {"message": "User deleted successfully"}
