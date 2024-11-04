from api_decorators import handle_exceptions
from database import AsyncSession, get_db
from repositories import RolesRepository
from fastapi import APIRouter, Depends
from services import RolesService
from responses.roles import *

router = APIRouter(prefix="/roles", tags=["roles"])


@router.get("/", summary="Fetch all roles", responses=get_roles)
@handle_exceptions(status_code=400)
async def get_all(db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/roles
    """

    roles = await RolesService(RolesRepository(db)).get_all()
    return roles


@router.get("/{role_id}", summary="Fetch role by id", responses=get_role)
@handle_exceptions(status_code=400)
async def get_one(role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        GET /api/roles/1
    """

    role = await RolesService(RolesRepository(db)).get_one(role_id=role_id)
    return role


@router.post("/", summary="Create role", responses=create_role)
@handle_exceptions(status_code=400)
async def create(role_name: str, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        POST /api/roles/
        {
            "role_id": 1,
            "role_name": "aaa"
        }
    """

    new_role = await RolesService(RolesRepository(db)).create(role_name=role_name)
    return new_role


@router.put("/{role_id}", summary="Update role by id", responses=update_role)
@handle_exceptions(status_code=400)
async def update(
    role_id: int, role_name: str = None, db: AsyncSession = Depends(get_db)
):
    """
    Query example:

        PUT /api/roles/1
        {
            "role_id": 1,
            "role_name": "bbb"
        }
    """

    role = await RolesService(RolesRepository(db)).update(
        role_id=role_id, role_name=role_name
    )
    return role


@router.delete("/{role_id}", summary="Delete role by id", responses=delete_role)
@handle_exceptions(status_code=400)
async def delete(role_id: int, db: AsyncSession = Depends(get_db)):
    """
    Query example:

        DELETE /api/roles/1
    """

    await RolesService(RolesRepository(db)).delete(role_id=role_id)
    return {"message": "Role deleted successfully"}
