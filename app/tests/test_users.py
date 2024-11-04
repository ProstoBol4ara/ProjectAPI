from repositories import UsersRepository
from unittest.mock import AsyncMock
from services import UsersService
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=UsersRepository)


@pytest.fixture
def service(mock_repository):
    return UsersService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(user_id=1, username="test_user1"),
        AsyncMock(user_id=2, username="test_user2"),
    ]

    users = await service.get_all()

    assert users == [
        {"user_id": 1, "username": "test_user1"},
        {"user_id": 2, "username": "test_user2"},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    username = "test_user"
    user_id = 1

    mock_repository.get_one.return_value = AsyncMock(user_id=user_id, username=username)

    user = await service.get_one(user_id=user_id)

    assert user == {"user_id": user_id, "username": username}
    mock_repository.get_one.assert_called_once_with(user_id=user_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    user_id = None

    with pytest.raises(ValueError):
        await service.get_one(user_id=user_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    password = "Valid1Password!"
    email = "valid@gmail.com"
    username = "new_user"
    user_id = 1

    mock_repository.create.return_value = AsyncMock(
        user_id=user_id, username=username, email=email
    )

    user = await service.create(username=username, email=email, password=password)

    assert user == {"user_id": user_id, "username": username, "email": email}
    mock_repository.create.assert_called_once_with(
        username=username, email=email, password=password
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    username = None
    email = "not-an-email"
    password = ""

    with pytest.raises(ValueError):
        await service.create(username=username, email=email, password=password)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    password = "Valid1Password!"
    email = "valid@gmail.com"
    username = "new_user"
    user_id = 1

    mock_repository.update.return_value = AsyncMock(
        user_id=user_id, username=username, email=email, password=password
    )

    user = await service.update(
        user_id=user_id, username=username, email=email, password=password
    )

    assert user == {"user_id": user_id, "username": username, "email": email}

    mock_repository.update.assert_called_once_with(
        user_id=user_id, username=username, email=email, password=password
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    username = "updated_user"
    email = "valid@gmail.com"
    password = "aa"
    user_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            user_id=user_id, username=username, email=email, password=password
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    user_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(user_id=user_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(user_id=user_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    user_id = None

    with pytest.raises(ValueError):
        await service.delete(user_id=user_id)

    mock_repository.delete.assert_not_called()
