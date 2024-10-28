from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from repositories import RolesRepository
from fastapi import APIRouter, Depends
from services import RolesService
from responses.roles import *

router = APIRouter(
    prefix="/roles",
    tags=["roles"]
)

@handle_exceptions(status_code=400)
@router.get('/', summary="Fetch all roles", responses=get_roles)
async def get_roles(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/roles
    """

    roles = await RolesService(RolesRepository(db)).get_roles()
    return roles

@handle_exceptions(status_code=400)
@router.get('/{role_id}', summary="Fetch role by id", responses=get_role)
async def get_role(role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/roles/1
    """

    role = await RolesService(RolesRepository(db)).get_role(role_id=role_id)
    return role

@handle_exceptions(status_code=400)
@router.post('/', summary="Create role", responses=create_role)
async def create_role(role_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/roles/
        {
            "role_id": 1,
            "role_name": "aaa"
        }
    """

    new_role = await RolesService(RolesRepository(db)).create_role(role_name=role_name)
    return new_role

@handle_exceptions(status_code=400)
@router.put('/{role_id}', summary="Update role by id", responses=update_role)
async def update_role(role_id: int, role_name: str = None, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        PUT /api/roles/1
        {
            "role_id": 1,
            "role_name": "bbb"
        }
    """

    role = await RolesService(RolesRepository(db)).update_role(role_id=role_id, role_name=role_name)
    return role

@handle_exceptions(status_code=400)
@router.delete('/{role_id}', summary="Delete role by id", responses=delete_role)
async def delete_role(role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/roles/1
    """

    await RolesService(RolesRepository(db)).delete_role(role_id=role_id)
    return {"message": "Role deleted successfully"}
