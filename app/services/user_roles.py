from repositories import UserRolesRepository

class UserRolesService:
    def __init__(self, user_roles_repository: UserRolesRepository):
        self.user_roles_repository = user_roles_repository

    async def get_user_roles(self):
        user_roles = await self.user_roles_repository.get_user_roles()

        return None if user_roles is None else \
            [{"user_role_id": user_role.user_role_id, "user_id": user_role.user_id,
              "role_id": user_role.role_id} for user_role in user_roles]

    async def get_user_role(self, user_role_id: int):
        user_role = await self.user_roles_repository.get_user_role(user_role_id=user_role_id)

        if not user_role: raise ValueError("User role not found")

        return {"user_role_id": user_role.user_role_id, "user_id": user_role.user_id, "role_id": user_role.role_id}

    async def create_user_role(self, user_id: int, role_id: int):
        new_user_role = await self.user_roles_repository.create_user_role(user_id=user_id, role_id=role_id)

        return {"user_role_id": new_user_role.user_role_id, "user_id": new_user_role.user_id, "role_id": new_user_role.role_id}

    async def update_user_role(self, user_role_id: int, user_id: int = None, role_id: int = None):
        user_role = await self.user_roles_repository\
            .update_user_role(user_role_id=user_role_id, user_id=user_id, role_id=role_id)

        if not user_role: raise ValueError("User role not found")

        return {"user_role_id": user_role.user_role_id, "user_id": user_role.user_id, "role_id": user_role.role_id}

    async def delete_user_role(self, user_role_id: int):
        return await self.user_roles_repository.delete_user_role(user_role_id=user_role_id)
