from repositories import NotificationsRepository
from services import NotificationsService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=NotificationsRepository)


@pytest.fixture
def service(mock_repository):
    return NotificationsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(notification_id=1, message="test_message1", user_id=1),
        AsyncMock(notification_id=2, message="test_message2", user_id=1),
    ]

    notifications = await service.get_all()

    assert notifications == [
        {"notification_id": 1, "message": "test_message1", "user_id": 1},
        {"notification_id": 2, "message": "test_message2", "user_id": 1},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    message = "test_message1"
    notification_id = 1
    user_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        notification_id=notification_id, message=message, user_id=user_id
    )

    notification = await service.get_one(notification_id=notification_id)

    assert notification == {
        "notification_id": notification_id,
        "message": message,
        "user_id": user_id,
    }

    mock_repository.get_one.assert_called_once_with(notification_id=notification_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    notification_id = None

    with pytest.raises(ValueError):
        await service.get_one(notification_id=notification_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    message = "test_message1"
    notification_id = 1
    user_id = 1

    mock_repository.create.return_value = AsyncMock(
        notification_id=notification_id, message=message, user_id=user_id
    )

    notification = await service.create(message=message, user_id=user_id)

    assert notification == {
        "notification_id": notification_id,
        "message": message,
        "user_id": user_id,
    }

    mock_repository.create.assert_called_once_with(message=message, user_id=user_id)


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    message = None
    user_id = None

    with pytest.raises(ValueError):
        await service.create(message=message, user_id=user_id)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    message = "test_message1"
    notification_id = 1
    user_id = 1

    mock_repository.update.return_value = AsyncMock(
        notification_id=notification_id, message=message, user_id=user_id
    )

    notification = await service.update(
        notification_id=notification_id, message=message, user_id=user_id
    )

    assert notification == {
        "notification_id": notification_id,
        "message": message,
        "user_id": user_id,
    }

    mock_repository.update.assert_called_once_with(
        notification_id=notification_id, message=message, user_id=user_id
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    message = "test_message1"
    notification_id = None
    user_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            notification_id=notification_id, message=message, user_id=user_id
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    notification_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(notification_id=notification_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(notification_id=notification_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    notification_id = None

    with pytest.raises(ValueError):
        await service.delete(notification_id=notification_id)

    mock_repository.delete.assert_not_called()
