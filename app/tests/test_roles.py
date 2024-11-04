from repositories import RolesRepository
from unittest.mock import AsyncMock
from services import RolesService
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=RolesRepository)


@pytest.fixture
def service(mock_repository):
    return RolesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(role_id=1, role_name="test_role1"),
        AsyncMock(role_id=2, role_name="test_role2"),
    ]

    roles = await service.get_all()

    assert roles == [
        {"role_id": 1, "role_name": "test_role1"},
        {"role_id": 2, "role_name": "test_role2"},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    role_name = "test_role2"
    role_id = 2

    mock_repository.get_one.return_value = AsyncMock(
        role_id=role_id, role_name=role_name
    )

    role = await service.get_one(role_id=role_id)

    assert role == {"role_id": role_id, "role_name": role_name}
    mock_repository.get_one.assert_called_once_with(role_id=role_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    role_id = None

    with pytest.raises(ValueError):
        await service.get_one(role_id=role_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    role_name = "test_role2"
    role_id = 2

    mock_repository.create.return_value = AsyncMock(
        role_id=role_id, role_name=role_name
    )

    role = await service.create(role_name=role_name)

    assert role == {"role_id": role_id, "role_name": role_name}
    mock_repository.create.assert_called_once_with(role_name=role_name)


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    role_name = None

    with pytest.raises(ValueError):
        await service.create(role_name=role_name)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    role_name = "test_role2"
    role_id = 2

    mock_repository.update.return_value = AsyncMock(
        role_id=role_id, role_name=role_name
    )

    role = await service.update(role_id=role_id, role_name=role_name)

    assert role == {"role_id": role_id, "role_name": role_name}

    mock_repository.update.assert_called_once_with(role_id=role_id, role_name=role_name)


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    role_name = "test_role2"
    role_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(role_id=role_id, role_name=role_name)

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    role_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(role_id=role_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(role_id=role_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    role_id = None

    with pytest.raises(ValueError):
        await service.delete(role_id=role_id)

    mock_repository.delete.assert_not_called()
