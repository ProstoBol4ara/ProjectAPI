from repositories import GenresRepository
from unittest.mock import AsyncMock
from services import GenresService
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=GenresRepository)


@pytest.fixture
def service(mock_repository):
    return GenresService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(genre_id=1, genre_name="test_genre1"),
        AsyncMock(genre_id=2, genre_name="test_genre2"),
    ]

    genres = await service.get_all()

    assert genres == [
        {"genre_id": 1, "genre_name": "test_genre1"},
        {"genre_id": 2, "genre_name": "test_genre2"},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    genre_name = "test_genre1"
    genre_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        genre_id=genre_id, genre_name=genre_name
    )

    genre = await service.get_one(genre_id=genre_id)

    assert genre == {"genre_id": genre_id, "genre_name": genre_name}
    mock_repository.get_one.assert_called_once_with(genre_id=genre_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    genre_id = None

    with pytest.raises(ValueError):
        await service.get_one(genre_id=genre_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    genre_name = "test_genre1"
    genre_id = 1

    mock_repository.create.return_value = AsyncMock(
        genre_id=genre_id, genre_name=genre_name
    )

    genre = await service.create(genre_name=genre_name)

    assert genre == {"genre_id": genre_id, "genre_name": genre_name}
    mock_repository.create.assert_called_once_with(genre_name=genre_name)


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    genre_name = None

    with pytest.raises(ValueError):
        await service.create(genre_name=genre_name)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    genre_name = "test_genre1"
    genre_id = 1

    mock_repository.update.return_value = AsyncMock(
        genre_id=genre_id, genre_name=genre_name
    )

    genre = await service.update(genre_id=genre_id, genre_name=genre_name)

    assert genre == {"genre_id": genre_id, "genre_name": genre_name}

    mock_repository.update.assert_called_once_with(
        genre_id=genre_id, genre_name=genre_name
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    genre_name = "test_genre1"
    genre_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(genre_id=genre_id, genre_name=genre_name)

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    genre_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(genre_id=genre_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(genre_id=genre_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    genre_id = None

    with pytest.raises(ValueError):
        await service.delete(genre_id=genre_id)

    mock_repository.delete.assert_not_called()
