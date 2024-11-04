from repositories import FavoritesRepository
from services import FavoritesService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=FavoritesRepository)


@pytest.fixture
def service(mock_repository):
    return FavoritesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(favorite_id=1, user_id=1, content_id=1),
        AsyncMock(favorite_id=2, user_id=1, content_id=2),
    ]

    favorites = await service.get_all()

    assert favorites == [
        {"favorite_id": 1, "user_id": 1, "content_id": 1},
        {"favorite_id": 2, "user_id": 1, "content_id": 2},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    favorite_id = 1
    content_id = 1
    user_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        favorite_id=favorite_id, user_id=user_id, content_id=content_id
    )

    favorite = await service.get_one(favorite_id=favorite_id)

    assert favorite == {
        "favorite_id": favorite_id,
        "user_id": user_id,
        "content_id": content_id,
    }
    mock_repository.get_one.assert_called_once_with(favorite_id=favorite_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    favorite_id = None

    with pytest.raises(ValueError):
        await service.get_one(favorite_id=favorite_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    favorite_id = 1
    content_id = 1
    user_id = 1

    mock_repository.create.return_value = AsyncMock(
        favorite_id=favorite_id, user_id=user_id, content_id=content_id
    )

    favorite = await service.create(user_id=user_id, content_id=content_id)

    assert favorite == {
        "favorite_id": favorite_id,
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
    favorite_id = 1
    content_id = 1
    user_id = 1

    mock_repository.update.return_value = AsyncMock(
        favorite_id=favorite_id, user_id=user_id, content_id=content_id
    )

    favorite = await service.update(
        favorite_id=favorite_id, user_id=user_id, content_id=content_id
    )

    assert favorite == {
        "favorite_id": favorite_id,
        "user_id": user_id,
        "content_id": content_id,
    }

    mock_repository.update.assert_called_once_with(
        favorite_id=favorite_id, user_id=user_id, content_id=content_id
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    favorite_id = None
    content_id = 1
    user_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            favorite_id=favorite_id, user_id=user_id, content_id=content_id
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    favorite_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(favorite_id=favorite_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(favorite_id=favorite_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    favorite_id = None

    with pytest.raises(ValueError):
        await service.delete(favorite_id=favorite_id)

    mock_repository.delete.assert_not_called()
