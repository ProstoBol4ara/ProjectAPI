from database import AsyncSession
from models import Users

class UsersRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_users(self):
        users = await self.db.execute(select(Users))
        return users.scalar().all()

    async def get_user(self, user_id: int):
        user = await self.db.execute(
            select(Users).where(Users.user_id == user_id)
        )
        return user.scalar_one_or_none()

    async def create_user(self, username: str, email: str, password: str):
        password = hash_password(password)
        new_user = Users(username=username, email=email, password_hash=password)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def update_user(self, user_id: int, username: str = None, email: str = None, password: str = None):
        user = await self.db.execute(
            select(Users).where(Users.user_id == user_id)
        )
        user = user.scalar_one_or_none()

        if password:
            user.password = hash_password(password)
        if username:
            user.username = username
        if email:
            user.email = email

        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete_user(self, user_id: int):
        await self.db.execute(
            delete(Users).where(Users.user_id == user_id)
        )
        await self.db.commit()