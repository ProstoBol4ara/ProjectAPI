from repositories import UserRolesRepository
from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from fastapi import APIRouter, Depends
from services import UserRolesService
from responses.user_roles import *

router = APIRouter(prefix="/user_roles", tags=["user_roles"])


@router.get("/", summary="Fetch all user roles", responses=get_user_roles)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/user_roles
    """

    user_roles = await UserRolesService(UserRolesRepository(db)).get_all()
    return user_roles


@router.get("/{user_role_id}", summary="Fetch user role by id", responses=get_user_role)
@handle_exceptions(status_code=400)
async def get_one(user_role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/user_roles/1
    """

    user_role = await UserRolesService(UserRolesRepository(db)).get_one(
        user_role_id=user_role_id
    )
    return user_role


@router.post("/", summary="Create user role", responses=create_user_role)
@handle_exceptions(status_code=400)
async def create(user_id: int, role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/user_roles/
        {
            "user_role_id": 1,
            "user_id": 1,
            "role_id": 1
        }
    """

    new_user_role = await UserRolesService(UserRolesRepository(db)).create(
        user_id=user_id, role_id=role_id
    )
    return new_user_role


@router.put(
    "/{user_role_id}", summary="Update user role by id", responses=update_user_role
)
@handle_exceptions(status_code=400)
async def update(user_role_id: int, role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/user_roles/1
        {
            "user_role_id": 1,
            "role_id": 2
        }
    """

    user_role = await UserRolesService(UserRolesRepository(db)).update(
        user_role_id=user_role_id, role_id=role_id
    )
    return user_role


@router.delete(
    "/{user_role_id}", summary="Delete user role by id", responses=delete_user_role
)
@handle_exceptions(status_code=400)
async def delete(user_role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/user_roles/1
    """

    await UserRolesService(UserRolesRepository(db)).delete(user_role_id=user_role_id)
    return {"message": "User role deleted successfully"}
