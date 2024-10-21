from database import AsyncSession
from models import Roles

class RolesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_roles(self):
        roles = await self.db.execute(select(Roles))
        return roles.scalar().all()

    async def get_role(self, role_id: int):
        role = await self.db.execute(
            select(Roles).where(Roles.role_id == role_id)
        )
        return role.scalar_one_or_none()

    async def create_role(self, role_name: str):
        new_role = Roles(role_name=role_name)
        self.db.add(new_role)
        await self.db.commit()
        await self.db.refresh(new_role)
        return new_role

    async def update_role(self, role_id: int, role_name: str = None):
        role = await self.db.execute(
            select(Roles).where(Roles.role_id == role_id)
        )
        role = role.scalar_one_or_none()

        if role_name:
            role.role_name = role_name

        await self.db.commit()
        await self.db.refresh(role)
        return role

    async def delete_role(self, role_id: int):
        await self.db.execute(
            delete(Roles).where(Roles.role_id == role_id)
        )
        await self.db.commit()