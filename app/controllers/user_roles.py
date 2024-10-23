from fastapi import APIRouter, HTTPException, Depends
from repositories import UserRolesRepository
from database import AsyncSession, get_db
from services import UserRolesService

router = APIRouter(
    prefix="/user_roles",
    tags=["user_roles"]
)

@router.get('/')
async def get_user_roles(db: AsyncSession = Depends(get_db)):
    user_roles = await UserRolesService(UserRolesRepository(db)).get_user_roles()
    if user_roles is None:
        raise HTTPException(status_code=400, detail="User roles not found")
    return user_roles

@router.get('/{user_role_id}')
async def get_user_role(user_role_id: int, db: AsyncSession = Depends(get_db)):
    user_role = await UserRolesService(UserRolesRepository(db)).get_user_role(user_role_id=user_role_id)
    if user_role is None:
        raise HTTPException(status_code=400, detail="User role not found")
    return user_role

@router.post('/')
async def create_user_role(user_id: int, role_id: int, db: AsyncSession = Depends(get_db)):
    try:
        new_user_role = await UserRolesService(UserRolesRepository(db)).create_user_role(user_id=user_id, role_id=role_id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_user_role

@router.put('/{user_role_id}')
async def update_user_role(user_role_id: int, db: AsyncSession = Depends(get_db)):
    try:
        user_role = await UserRolesService(UserRolesRepository(db)).update_user_role(user_role_id=user_role_id, user_id=user_id, role_id=role_id)
        if user_role is None:
            raise HTTPException(status_code=400, detail="User role not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return user_role

@router.delete('/{user_role_id}')
async def delete_user_role(user_role_id: int, db: AsyncSession = Depends(get_db)):
    if not await UserRolesService(UserRolesRepository(db)).delete_user_role(user_role_id=user_role_id):
        raise HTTPException(status_code=400, detail="User role not found")
    return {"message": "User role deleted successfully"}