from email_validator import validate_email, EmailNotValidError
from repositories import UsersRepository
import re

password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,20}$'

class UsersService:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    async def get_users(self):
        users = await self.user_repository.get_users()
        return None if users is None else [{"user_id": user.user_id, "username": user.username} for user in users]

    async def get_user(self, user_id: int):
        user = await self.user_repository.get_user(user_id=user_id)

        if not user: raise ValueError("User not found")

        return {"user_id": user.user_id, "username": user.username}

    async def create_user(self, username: str, email: str, password: str):
        try:
            email = validate_email(email).normalized
        except EmailNotValidError as ex:
            raise ValueError(f"Invalid email address: {ex}")

        if not username or not password:
            raise ValueError("Username and password cannot be empty")

        if not re.match(password_pattern, password):
            raise ValueError("Password must be 8-20 characters long, contain at least one uppercase letter, \
                             one lowercase letter, one digit, and one special character.")

        new_user = await self.user_repository.create_user(username=username, email=email, password=password)
        return {"user_id": new_user.user_id, "username": new_user.username, "email": new_user.email}

    async def update_user(self, user_id: int, username: str = None, email: str = None, password: str = None):
        try:
            if email is not None:
                email = validate_email(email).normalized
        except EmailNotValidError as ex:
            raise ValueError(f"Invalid email address: {ex}")

        if password is not None and not re.match(password_pattern, password):
            raise ValueError("Password must be 8-20 characters long, contain at least one uppercase letter, \
                             one lowercase letter, one digit, and one special character.")

        user = await self.user_repository.update_user(user_id=user_id, username=username, email=email, password=password)

        if user is None: raise ValueError("User not found")

        return {"user_id": user.user_id, "username": user.username, "email": user.email}

    async def delete_user(self, user_id: int):
        return await self.user_repository.delete_user(user_id=user_id)
