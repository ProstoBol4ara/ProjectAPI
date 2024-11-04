from repositories import UserRolesRepository


class UserRolesService:
    def __init__(self, repository: UserRolesRepository):
        self.repository = repository

    async def get_all(self):
        user_roles = await self.repository.get_all()

        return (
            None
            if user_roles is None
            else [
                {
                    "user_role_id": user_role.user_role_id,
                    "user_id": user_role.user_id,
                    "role_id": user_role.role_id,
                }
                for user_role in user_roles
            ]
        )

    async def get_one(self, user_role_id: int):
        if not user_role_id:
            raise ValueError("user_role_id cannot be empty")

        user_role = await self.repository.get_one(user_role_id=user_role_id)

        if not user_role:
            raise ValueError("User role not found")

        return {
            "user_role_id": user_role.user_role_id,
            "user_id": user_role.user_id,
            "role_id": user_role.role_id,
        }

    async def create(self, user_id: int, role_id: int):
        if not user_id or not role_id:
            raise ValueError("user_id and role_id cannot be empty")

        new_user_role = await self.repository.create(user_id=user_id, role_id=role_id)
        return {
            "user_role_id": new_user_role.user_role_id,
            "user_id": new_user_role.user_id,
            "role_id": new_user_role.role_id,
        }

    async def update(self, user_role_id: int, user_id: int = None, role_id: int = None):
        if not user_role_id:
            raise ValueError("user_role_id cannot be empty")

        user_role = await self.repository.update(
            user_role_id=user_role_id, user_id=user_id, role_id=role_id
        )

        if not user_role:
            raise ValueError("User role not found")

        return {
            "user_role_id": user_role.user_role_id,
            "user_id": user_role.user_id,
            "role_id": user_role.role_id,
        }

    async def delete(self, user_role_id: int):
        if not user_role_id:
            raise ValueError("user_role_id cannot be empty")

        if not (
            delete_user_role := await self.repository.delete(user_role_id=user_role_id)
        ):
            raise ValueError("User role not found")
        return delete_user_role
