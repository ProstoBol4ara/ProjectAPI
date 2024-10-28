from repositories import UsersRepository
from unittest.mock import AsyncMock
from services import UsersService
import pytest

@pytest.fixture
def mock_user_repository():
    return AsyncMock(spec=UsersRepository)

@pytest.fixture
def users_service(mock_user_repository):
    return UsersService(user_repository=mock_user_repository)

@pytest.mark.asyncio
async def test_get_all_users(users_service, mock_user_repository):
    mock_user_repository.get_users.return_value = [
        AsyncMock(user_id=1, username="test_user1"),
        AsyncMock(user_id=2, username="test_user2")
    ]

    users = await users_service.get_users()

    assert users == [
        {"user_id": 1, "username": "test_user1"},
        {"user_id": 2, "username": "test_user2"}
    ]
    mock_user_repository.get_users.assert_called_once()

@pytest.mark.asyncio
async def test_get_user_not_found(users_service, mock_user_repository):
    mock_user_repository.get_user.return_value = None
    with pytest.raises(ValueError):
        await users_service.get_user(user_id=1)

    mock_user_repository.get_user.assert_called_once_with(user_id=1)

@pytest.mark.asyncio
async def test_create_user(users_service, mock_user_repository):
    password = "Valid1Password!"
    email = "valid@gmail.com"
    username="new_user"

    mock_user_repository.create_user.return_value = AsyncMock(user_id=1, username=username, email=email)

    user = await users_service.create_user(username=username, email=email, password=password)

    assert user == {"user_id": 1, "username": username, "email": email}
    mock_user_repository.create_user.assert_called_once_with(username=username, email=email, password=password)

@pytest.mark.asyncio
async def test_update_user(users_service, mock_user_repository):
    mock_user_repository.update_user.return_value = AsyncMock(user_id=1, username="updated_user", email="valid@gmail.com")

    user = await users_service.update_user(user_id=1, username="updated_user", email="valid@gmail.com")

    assert user == {"user_id": 1, "username": "updated_user", "email": "valid@gmail.com"}

    mock_user_repository.update_user.assert_called_once_with(user_id=1, username="updated_user", email="valid@gmail.com", password=None)

@pytest.mark.asyncio
async def test_delete_user(users_service, mock_user_repository):
    mock_user_repository.delete_user.return_value = True

    result = await users_service.delete_user(user_id=1)

    assert result is True
    mock_user_repository.delete_user.assert_called_once_with(user_id=1)

@pytest.mark.asyncio
async def test_create_user_invalid_data(users_service, mock_user_repository):
    invalid_username = None
    invalid_email = "not-an-email"
    invalid_password = ""

    with pytest.raises(ValueError):
        await users_service.create_user(username=invalid_username, email=invalid_email, password=invalid_password)

    mock_user_repository.create_user.assert_not_called()
