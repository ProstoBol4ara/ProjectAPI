from fastapi import APIRouter, HTTPException, Depends
from database import AsyncSession, get_db
from repositories import RolesRepository
from services import RolesService

router = APIRouter(
    prefix="/roles",
    tags=["roles"]
)

@router.get('/')
async def get_roles(db: AsyncSession = Depends(get_db)):
    roles = await RolesService(RolesRepository(db)).get_roles()
    if roles is None:
        raise HTTPException(status_code=400, detail="Roles not found")
    return roles

@router.get('/{role_id}')
async def get_role(role_id: int, db: AsyncSession = Depends(get_db)):
    role = await RolesService(RolesRepository(db)).get_role(role_id=role_id)
    if role is None:
        raise HTTPException(status_code=400, detail="Role not found")
    return role

@router.post('/')
async def create_role(role_name: str, db: AsyncSession = Depends(get_db)):
    try:
        new_role = await RolesService(RolesRepository(db)).create_role(role_name=role_name)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return new_role

@router.put('/{role_id}')
async def update_role(role_id: int, role_name: str = None, db: AsyncSession = Depends(get_db)):
    try:
        role = await RolesService(RolesRepository(db)).update_role(role_id=role_id, role_name=role_name)
        if role is None:
            raise HTTPException(status_code=400, detail="Role not found")
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"{ex}")
    return role

@router.delete('/{role_id}')
async def delete_role(role_id: int, db: AsyncSession = Depends(get_db)):
    if not await RolesService(RolesRepository(db)).delete_role(role_id=role_id):
        raise HTTPException(status_code=400, detail="Role not found")
    return {"message": "Role deleted successfully"}