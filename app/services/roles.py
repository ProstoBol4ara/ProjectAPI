from repositories import RolesRepository

class RolesService:
    def __init__(self, roles_repository: RolesRepository):
        self.roles_repository = roles_repository

    async def get_roles(self):
        roles = await self.roles_repository.get_roles()
        return None if roles is None else [{"role_id": role.role_id, "role_name": role.role_name} for role in roles]

    async def get_role(self, role_id: int):
        role = await self.roles_repository.get_role(role_id=role_id)
        return None if role is None else {"role_id": role.role_id, "role_name": role.role_name}

    async def create_role(self, role_name: str):
        new_role = await self.roles_repository.create_role(role_name=role_name)
        return {"role_id": new_role.role_id, "role_name": new_role.role_name}

    async def update_role(self, role_id: int, role_name: str = None):
        role = await self.roles_repository.update_role(role_id=role_id, role_name=role_name)
        return None if role is None else {"role_id": role.role_id, "role_name": role.role_name}

    async def delete_role(self, role_id: int):
        return await self.roles_repository.delete_role(role_id=role_id)
