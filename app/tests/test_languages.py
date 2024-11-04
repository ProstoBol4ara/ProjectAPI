from repositories import LanguagesRepository
from services import LanguagesService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=LanguagesRepository)


@pytest.fixture
def service(mock_repository):
    return LanguagesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(language_id=1, language_name="test_language1"),
        AsyncMock(language_id=2, language_name="test_language2"),
    ]

    languages = await service.get_all()

    assert languages == [
        {"language_id": 1, "language_name": "test_language1"},
        {"language_id": 2, "language_name": "test_language2"},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    language_name = "test_language"
    language_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        language_id=language_id, language_name=language_name
    )

    language = await service.get_one(language_id=language_id)

    assert language == {"language_id": language_id, "language_name": language_name}
    mock_repository.get_one.assert_called_once_with(language_id=language_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    language_id = None

    with pytest.raises(ValueError):
        await service.get_one(language_id=language_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    language_name = "test_language"
    language_id = 1

    mock_repository.create.return_value = AsyncMock(
        language_id=language_id, language_name=language_name
    )

    language = await service.create(language_name=language_name)

    assert language == {"language_id": language_id, "language_name": language_name}
    mock_repository.create.assert_called_once_with(language_name=language_name)


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    language_name = None

    with pytest.raises(ValueError):
        await service.create(language_name=language_name)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    language_name = "test_language"
    language_id = 1

    mock_repository.update.return_value = AsyncMock(
        language_id=language_id, language_name=language_name
    )

    language = await service.update(
        language_id=language_id, language_name=language_name
    )

    assert language == {"language_id": language_id, "language_name": language_name}

    mock_repository.update.assert_called_once_with(
        language_id=language_id, language_name=language_name
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    language_name = "test_language"
    language_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(language_id=language_id, language_name=language_name)

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    language_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(language_id=language_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(language_id=language_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    language_id = None

    with pytest.raises(ValueError):
        await service.delete(language_id=language_id)

    mock_repository.delete.assert_not_called()
