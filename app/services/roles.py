from repositories import RolesRepository

class RolesService:
    def __init__(self, roles_repository: RolesRepository):
        self.roles_repository = roles_repository

    async def get_roles(self):
        return await self.roles_repository.get_roles()

    async def get_role(self, role_id: int):
        return await self.roles_repository.get_role(role_id=role_id)

    async def create_role(self, role_name: str):
        return await self.roles_repository.create_role(role_name=role_name)

    async def update_role(self, role_id: int, role_name: str = None):
        return await self.roles_repository.update_role(role_id=role_id, role_name=role_name)

    async def delete_role(self, role_id: int):
        await self.roles_repository.delete_role(role_id=role_id)
    