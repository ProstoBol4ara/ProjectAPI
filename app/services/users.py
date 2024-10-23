from repositories import UsersRepository

class UsersService:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository
    
    async def get_users(self):
        users = await self.user_repository.get_users()
        return None if users is None else [{"user_id": user.user_id, "username": user.username} for user in users]

    async def get_user(self, user_id: int):
        user = await self.user_repository.get_user(user_id=user_id)
        return None if user is None else {"user_id": user.user_id, "username": user.username}
        
    async def create_user(self, username: str, email: str, password: str):
        new_user = await self.user_repository.create_user(username=username, email=email, password=password)
        return {"user_id": new_user.user_id, "username": new_user.username, "email": new_user.email}

    async def update_user(self, user_id: int, username: str = None, email: str = None, password: str = None):
        user = await self.user_repository.update_user(user_id=user_id, username=username, email=email, password=password)
        return None if user is None else {"user_id": user.user_id, "username": user.username, "email": user.email}

    async def delete_user(self, user_id: int):
        return await self.user_repository.delete_user(user_id=user_id)