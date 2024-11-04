from repositories import UserRolesRepository
from services import UserRolesService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=UserRolesRepository)


@pytest.fixture
def service(mock_repository):
    return UserRolesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(user_role_id=1, user_id=1, role_id=1),
        AsyncMock(user_role_id=2, user_id=2, role_id=2),
    ]

    user_roles = await service.get_all()

    assert user_roles == [
        {"user_role_id": 1, "user_id": 1, "role_id": 1},
        {"user_role_id": 2, "user_id": 2, "role_id": 2},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    user_role_id = 1
    user_id = 1
    role_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        user_role_id=user_role_id, user_id=user_id, role_id=role_id
    )

    user_role = await service.get_one(user_role_id=user_role_id)

    assert user_role == {
        "user_role_id": user_role_id,
        "user_id": user_id,
        "role_id": role_id,
    }
    mock_repository.get_one.assert_called_once_with(user_role_id=user_role_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    user_role_id = None

    with pytest.raises(ValueError):
        await service.get_one(user_role_id=user_role_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    user_role_id = 1
    user_id = 1
    role_id = 1

    mock_repository.create.return_value = AsyncMock(
        user_role_id=user_role_id, user_id=user_id, role_id=role_id
    )

    user_role = await service.create(user_id=user_id, role_id=role_id)

    assert user_role == {
        "user_role_id": user_role_id,
        "user_id": user_id,
        "role_id": role_id,
    }
    mock_repository.create.assert_called_once_with(user_id=user_id, role_id=role_id)


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    user_id = None
    role_id = "awdawd"

    with pytest.raises(ValueError):
        await service.create(user_id=user_id, role_id=role_id)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    user_role_id = 1
    user_id = 1
    role_id = 1

    mock_repository.update.return_value = AsyncMock(
        user_role_id=user_role_id, user_id=user_id, role_id=role_id
    )

    user_role = await service.update(
        user_role_id=user_role_id, user_id=user_id, role_id=role_id
    )

    assert user_role == {
        "user_role_id": user_role_id,
        "user_id": user_id,
        "role_id": role_id,
    }

    mock_repository.update.assert_called_once_with(
        user_role_id=user_role_id, user_id=user_id, role_id=role_id
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    user_role_id = None
    user_id = 1
    role_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            user_role_id=user_role_id, user_id=user_id, role_id=role_id
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    user_role_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(user_role_id=user_role_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(user_role_id=user_role_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    user_role_id = None

    with pytest.raises(ValueError):
        await service.delete(user_role_id=user_role_id)

    mock_repository.delete.assert_not_called()
