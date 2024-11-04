from email_validator import validate_email, EmailNotValidError
from repositories import UsersRepository
from constants import password_pattern
from re import match


class UsersService:
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    async def get_all(self):
        users = await self.repository.get_all()
        return (
            None
            if users is None
            else [
                {"user_id": user.user_id, "username": user.username} for user in users
            ]
        )

    async def get_one(self, user_id: int):
        if not user_id:
            raise ValueError("user_id cannot be empty")

        user = await self.repository.get_one(user_id=user_id)

        if not user:
            raise ValueError("User not found")

        return {"user_id": user.user_id, "username": user.username}

    async def create(self, username: str, email: str, password: str):
        try:
            email = validate_email(email).normalized
        except EmailNotValidError as ex:
            raise ValueError(f"Invalid email address: {ex}")

        if not username or not password:
            raise ValueError("Username and password cannot be empty")

        if not match(password_pattern, password):
            raise ValueError(
                "Password must be 8-20 characters long, contain at least one uppercase letter, \
                             one lowercase letter, one digit, and one special character."
            )

        new_user = await self.repository.create(
            username=username, email=email, password=password
        )
        return {
            "user_id": new_user.user_id,
            "username": new_user.username,
            "email": new_user.email,
        }

    async def update(
        self,
        user_id: int,
        username: str = None,
        email: str = None,
        password: str = None,
    ):
        if not user_id:
            raise ValueError("user_id cannot be empty")

        try:
            if email is not None:
                email = validate_email(email).normalized
        except EmailNotValidError as ex:
            raise ValueError(f"Invalid email address: {ex}")

        if password and not match(password_pattern, password):
            raise ValueError(
                "Password must be 8-20 characters long, contain at least one uppercase letter, \
                             one lowercase letter, one digit, and one special character."
            )

        user = await self.repository.update(
            user_id=user_id, username=username, email=email, password=password
        )

        if user is None:
            raise ValueError("User not found")

        return {"user_id": user.user_id, "username": user.username, "email": user.email}

    async def delete(self, user_id: int):
        if not user_id:
            raise ValueError("user_id cannot be empty")

        if not (delete_user := await self.repository.delete(user_id=user_id)):
            raise ValueError("User not found")
        return delete_user
