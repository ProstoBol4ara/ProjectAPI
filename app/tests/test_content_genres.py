from repositories import ContentGenresRepository
from services import ContentGenresService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=ContentGenresRepository)


@pytest.fixture
def service(mock_repository):
    return ContentGenresService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(content_genre_id=1, content_id=1, genre_id=1),
        AsyncMock(content_genre_id=2, content_id=1, genre_id=2),
    ]

    content_genres = await service.get_all()

    assert content_genres == [
        {"content_genre_id": 1, "content_id": 1, "genre_id": 1},
        {"content_genre_id": 2, "content_id": 1, "genre_id": 2},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    content_genre_id = 1
    content_id = 1
    genre_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        content_genre_id=content_genre_id, content_id=content_id, genre_id=genre_id
    )

    content_genre = await service.get_one(content_genre_id=content_genre_id)

    assert content_genre == {
        "content_genre_id": content_genre_id,
        "content_id": content_id,
        "genre_id": genre_id,
    }
    mock_repository.get_one.assert_called_once_with(content_genre_id=content_genre_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    content_genre_id = None

    with pytest.raises(ValueError):
        await service.get_one(content_genre_id=content_genre_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    content_genre_id = 1
    content_id = 1
    genre_id = 1

    mock_repository.create.return_value = AsyncMock(
        content_genre_id=content_genre_id, content_id=content_id, genre_id=genre_id
    )

    content_genre = await service.create(content_id=content_id, genre_id=genre_id)

    assert content_genre == {
        "content_genre_id": content_genre_id,
        "content_id": content_id,
        "genre_id": genre_id,
    }

    mock_repository.create.assert_called_once_with(
        content_id=content_id, genre_id=genre_id
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    invalid_content_id = None
    invalid_genre_id = None

    with pytest.raises(ValueError):
        await service.create(content_id=invalid_content_id, genre_id=invalid_genre_id)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    content_genre_id = 1
    content_id = 1
    genre_id = 1

    mock_repository.update.return_value = AsyncMock(
        content_genre_id=content_genre_id, content_id=content_id, genre_id=genre_id
    )

    content_genre = await service.update(
        content_genre_id=content_genre_id, content_id=content_id, genre_id=genre_id
    )

    assert content_genre == {
        "content_genre_id": content_genre_id,
        "content_id": content_id,
        "genre_id": genre_id,
    }

    mock_repository.update.assert_called_once_with(
        content_genre_id=content_genre_id, content_id=content_id, genre_id=genre_id
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    content_genre_id = None
    content_id = 1
    genre_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            content_genre_id=content_genre_id, content_id=content_id, genre_id=genre_id
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    content_genre_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(content_genre_id=content_genre_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(content_genre_id=content_genre_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    content_genre_id = None

    with pytest.raises(ValueError):
        await service.delete(content_genre_id=content_genre_id)

    mock_repository.delete.assert_not_called()
