from repositories import RolesRepository


class RolesService:
    def __init__(self, repository: RolesRepository):
        self.repository = repository

    async def get_all(self):
        roles = await self.repository.get_all()
        return (
            None
            if roles is None
            else [
                {"role_id": role.role_id, "role_name": role.role_name} for role in roles
            ]
        )

    async def get_one(self, role_id: int):
        if not role_id:
            raise ValueError("role_id cannot be empty")

        role = await self.repository.get_one(role_id=role_id)

        if not role:
            raise ValueError("Role not found")

        return {"role_id": role.role_id, "role_name": role.role_name}

    async def create(self, role_name: str):
        if not role_name:
            raise ValueError("role_name cannot be empty")

        new_role = await self.repository.create(role_name=role_name)
        return {"role_id": new_role.role_id, "role_name": new_role.role_name}

    async def update(self, role_id: int, role_name: str = None):
        if not role_id:
            raise ValueError("role_id cannot be empty")

        role = await self.repository.update(role_id=role_id, role_name=role_name)

        if not role:
            raise ValueError("Role not found")

        return {"role_id": role.role_id, "role_name": role.role_name}

    async def delete(self, role_id: int):
        if not role_id:
            raise ValueError("role_id cannot be empty")

        if not (delete_role := await self.repository.delete(role_id=role_id)):
            raise ValueError("Role not found")
        return delete_role
