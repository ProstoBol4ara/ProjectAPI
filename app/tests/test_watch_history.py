from repositories import WatchHistoryRepository
from services import WatchHistoryService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=WatchHistoryRepository)


@pytest.fixture
def service(mock_repository):
    return WatchHistoryService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(watch_history_id=1, user_id=1, content_id=1),
        AsyncMock(watch_history_id=2, user_id=1, content_id=2),
    ]

    watch_historys = await service.get_all()

    assert watch_historys == [
        {"watch_history_id": 1, "user_id": 1, "content_id": 1},
        {"watch_history_id": 2, "user_id": 1, "content_id": 2},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    watch_history_id = 1
    content_id = 1
    user_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        watch_history_id=watch_history_id, user_id=user_id, content_id=content_id
    )

    watch_history = await service.get_one(watch_history_id=watch_history_id)

    assert watch_history == {
        "watch_history_id": watch_history_id,
        "user_id": user_id,
        "content_id": content_id,
    }
    mock_repository.get_one.assert_called_once_with(watch_history_id=watch_history_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    watch_history_id = None

    with pytest.raises(ValueError):
        await service.get_one(watch_history_id=watch_history_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    watch_history_id = 1
    content_id = 1
    user_id = 1

    mock_repository.create.return_value = AsyncMock(
        watch_history_id=watch_history_id, user_id=user_id, content_id=content_id
    )

    watch_history = await service.create(user_id=user_id, content_id=content_id)

    assert watch_history == {
        "watch_history_id": watch_history_id,
        "user_id": user_id,
        "content_id": content_id,
    }
    mock_repository.create.assert_called_once_with(
        user_id=user_id, content_id=content_id
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    content_id = None
    user_id = None

    with pytest.raises(ValueError):
        await service.create(user_id=user_id, content_id=content_id)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    watch_history_id = 1
    content_id = 1
    user_id = 2

    mock_repository.update.return_value = AsyncMock(
        watch_history_id=watch_history_id, user_id=user_id, content_id=content_id
    )

    watch_history = await service.update(
        watch_history_id=watch_history_id, user_id=user_id, content_id=content_id
    )

    assert watch_history == {
        "watch_history_id": watch_history_id,
        "user_id": user_id,
        "content_id": content_id,
    }

    mock_repository.update.assert_called_once_with(
        watch_history_id=watch_history_id, user_id=user_id, content_id=content_id
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    invalid_watch_history_id = None
    invalid_content_id = 1
    invalid_user_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            watch_history_id=invalid_watch_history_id,
            content_id=invalid_content_id,
            user_id=invalid_user_id,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    watch_history_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(watch_history_id=watch_history_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(watch_history_id=watch_history_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    watch_history_id = None

    with pytest.raises(ValueError):
        await service.delete(watch_history_id=watch_history_id)

    mock_repository.delete.assert_not_called()
