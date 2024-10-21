from repositories import UserRolesRepository

class UserRolesService:
    def __init__(self, user_roles_repository: UserRolesRepository):
        self.user_roles_repository = user_roles_repository

    async def get_user_roles(self):
        return await self.user_roles_repository.get_user_roles()

    async def get_user_role(self, user_role_id: int):
        return await self.user_roles_repository.get_user_role(user_role_id=user_role_id)

    async def create_user_role(self, user_id: int, role_id: int):
        return await self.user_roles_repository.create_user_role(user_id=user_id, role_id=role_id)

    async def update_user_role(self, user_role_id: int, user_id: int = None, role_id: int = None):
        return await self.user_roles_repository.update_user_role(user_role_id=user_role_id, user_id=user_id, role_id=role_id)

    async def delete_user_role(self, user_role_id: int):
        await self.user_roles_repository.delete_user_role(user_role_id=user_role_id)
    