from repositories import UsersRepository

class UsersService:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository
    
    async def get_actors(self):
        return await self.user_repository.get_actors()

    async def get_user(self, user_id: int):
        return await self.user_repository.get_user(user_id=user_id)
        
    async def create_user(self, username: str, email: str, password: str):
        return await self.user_repository.create_user(username=username, email=email, password=password)

    async def update_user(self, user_id: int, username: str = None, email: str = None, password: str = None):
        return await self.user_repository.update_user(user_id=user_id, username=username, email=email, password=password)

    async def delete_user(self, user_id: int):
        await self.user_repository.delete_user(user_id=user_id)