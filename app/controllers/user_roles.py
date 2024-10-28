from fastapi import APIRouter, HTTPException, Depends
from repositories import UserRolesRepository
from database import AsyncSession, get_db
from services import UserRolesService
from responses.user_roles import *

router = APIRouter(
    prefix="/user_roles",
    tags=["user_roles"]
)

@router.get('/', summary="Fetch all user roles", responses=get_user_roles)
async def get_user_roles(db: AsyncSession = Depends(get_db)):
    """
    Query example:
        
        GET /api/user_roles
    """

    user_roles = await UserRolesService(UserRolesRepository(db)).get_user_roles()
    if user_roles is None:
        raise HTTPException(status_code=400, detail="User roles not found")
    return user_roles

@router.get('/{user_role_id}', summary="Fetch user role by id", responses=get_user_role)
async def get_user_role(user_role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/user_roles/1
    """

    user_role = await UserRolesService(UserRolesRepository(db)).get_user_role(user_role_id=user_role_id)
    if user_role is None:
        raise HTTPException(status_code=400, detail="User role not found")
    return user_role

@router.post('/', summary="Create user role", responses=create_user_role)
async def create_user_role(user_id: int, role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/user_roles/
        {
            "user_role_id": 1, 
            "user_id": 1, 
            "role_id": 1
        }
    """

    try:
        new_user_role = await UserRolesService(UserRolesRepository(db)).create_user_role(user_id=user_id, role_id=role_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_user_role

@router.put('/{user_role_id}', summary="Update user role by id", responses=update_user_role)
async def update_user_role(user_role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/user_roles/1
        {
            "user_role_id": 1,
            "role_id": 2
        }
    """

    try:
        user_role = await UserRolesService(UserRolesRepository(db)).update_user_role(user_role_id=user_role_id, user_id=user_id, role_id=role_id)
        if user_role is None:
            raise HTTPException(status_code=400, detail="User role not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return user_role

@router.delete('/{user_role_id}', summary="Delete user role by id", responses=delete_user_role)
async def delete_user_role(user_role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/user_roles/1
    """

    if not await UserRolesService(UserRolesRepository(db)).delete_user_role(user_role_id=user_role_id):
        raise HTTPException(status_code=400, detail="User role not found")
    return {"message": "User role deleted successfully"}