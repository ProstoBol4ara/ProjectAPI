from database import AsyncSession, select, delete
from models import UserRoles

class UserRolesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_roles(self):
        user_roles = await self.db.execute(select(UserRoles))
        return user_roles.scalars().all()

    async def get_user_role(self, user_role_id: int):
        user_role = await self.db.execute(
            select(UserRoles).where(UserRoles.user_role_id == user_role_id)
        )
        return user_role.scalar_one_or_none()

    async def create_user_role(self, user_id: int, role_id: int):
        new_user_role = UserRoles(user_id=user_id, role_id=role_id)
        self.db.add(new_user_role)
        await self.db.commit()
        await self.db.refresh(new_user_role)
        return new_user_role

    async def update_user_role(self, user_role_id: int, user_id: int = None, role_id: int = None):
        user_role = await self.db.execute(
            select(UserRoles).where(UserRoles.user_id == user_id)
        )
        user_role = user_role.scalar_one_or_none()

        if user_id:
            user_role.user_id = user_id
        if role_id:
            user_role.role_id = role_id

        await self.db.commit()
        await self.db.refresh(user_role)
        return user_role

    async def delete_user_role(self, user_role_id: int):
        result = await self.db.execute(
            delete(UserRoles).where(UserRoles.user_role_id == user_role_id)
        )
        await self.db.commit()
        return result.rowcount > 0
