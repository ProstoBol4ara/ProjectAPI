from repositories import ContentLanguagesRepository
from services import ContentLanguagesService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=ContentLanguagesRepository)


@pytest.fixture
def service(mock_repository):
    return ContentLanguagesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(content_language_id=1, content_id=1, language_id=1),
        AsyncMock(content_language_id=2, content_id=1, language_id=2),
    ]

    content_languages = await service.get_all()

    assert content_languages == [
        {"content_language_id": 1, "content_id": 1, "language_id": 1},
        {"content_language_id": 2, "content_id": 1, "language_id": 2},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    content_language_id = 1
    language_id = 1
    content_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        content_language_id=content_language_id,
        language_id=language_id,
        content_id=content_id,
    )

    content_language = await service.get_one(content_language_id=content_language_id)

    assert content_language == {
        "content_language_id": content_language_id,
        "content_id": language_id,
        "language_id": content_id,
    }
    mock_repository.get_one.assert_called_once_with(
        content_language_id=content_language_id
    )


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    content_language_id = None

    with pytest.raises(ValueError):
        await service.get_one(content_language_id=content_language_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    content_language_id = 1
    language_id = 1
    content_id = 1

    mock_repository.create.return_value = AsyncMock(
        content_language_id=content_language_id,
        language_id=language_id,
        content_id=content_id,
    )

    content_language = await service.create(
        language_id=language_id, content_id=content_id
    )

    assert content_language == {
        "content_language_id": content_language_id,
        "content_id": language_id,
        "language_id": content_id,
    }

    mock_repository.create.assert_called_once_with(
        language_id=language_id, content_id=content_id
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    language_id = None
    content_id = None

    with pytest.raises(ValueError):
        await service.create(language_id=language_id, content_id=content_id)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    content_language_id = 1
    language_id = 1
    content_id = 1

    mock_repository.update.return_value = AsyncMock(
        content_language_id=content_language_id,
        language_id=language_id,
        content_id=content_id,
    )

    content_language = await service.update(
        content_language_id=content_language_id,
        language_id=language_id,
        content_id=content_id,
    )

    assert content_language == {
        "content_language_id": content_language_id,
        "content_id": language_id,
        "language_id": content_id,
    }

    mock_repository.update.assert_called_once_with(
        content_language_id=content_language_id,
        language_id=language_id,
        content_id=content_id,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    content_language_id = None
    language_id = 1
    content_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            content_language_id=content_language_id,
            language_id=language_id,
            content_id=content_id,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    content_language_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(content_language_id=content_language_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(
        content_language_id=content_language_id
    )


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    content_language_id = None

    with pytest.raises(ValueError):
        await service.delete(content_language_id=content_language_id)

    mock_repository.delete.assert_not_called()
