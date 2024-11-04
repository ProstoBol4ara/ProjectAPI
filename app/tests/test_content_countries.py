from repositories import ContentCountriesRepository
from services import ContentCountriesService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=ContentCountriesRepository)


@pytest.fixture
def service(mock_repository):
    return ContentCountriesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(content_country_id=1, content_id=1, country_id=1),
        AsyncMock(content_country_id=2, content_id=2, country_id=1),
    ]

    content_countries = await service.get_all()

    assert content_countries == [
        {"content_country_id": 1, "content_id": 1, "country_id": 1},
        {"content_country_id": 2, "content_id": 2, "country_id": 1},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    content_country_id = 1
    content_id = 1
    country_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        content_country_id=content_country_id,
        content_id=content_id,
        country_id=country_id,
    )

    content_country = await service.get_one(content_country_id=content_country_id)

    assert content_country == {
        "content_country_id": content_country_id,
        "content_id": content_id,
        "country_id": country_id,
    }
    mock_repository.get_one.assert_called_once_with(
        content_country_id=content_country_id
    )


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    content_country_id = None

    with pytest.raises(ValueError):
        await service.get_one(content_country_id=content_country_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    content_country_id = 1
    content_id = 1
    country_id = 1

    mock_repository.create.return_value = AsyncMock(
        content_country_id=content_country_id,
        content_id=content_id,
        country_id=country_id,
    )

    content_country = await service.create(content_id=content_id, country_id=country_id)

    assert content_country == {
        "content_country_id": content_country_id,
        "content_id": content_id,
        "country_id": country_id,
    }
    mock_repository.create.assert_called_once_with(
        content_id=content_id, country_id=country_id
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    content_id = None
    country_id = None

    with pytest.raises(ValueError):
        await service.create(content_id=content_id, country_id=country_id)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    content_country_id = 1
    content_id = 1
    country_id = 1

    mock_repository.update.return_value = AsyncMock(
        content_country_id=content_country_id,
        content_id=content_id,
        country_id=country_id,
    )

    content_country = await service.update(
        content_country_id=content_country_id,
        content_id=content_id,
        country_id=country_id,
    )

    assert content_country == {
        "content_country_id": content_country_id,
        "content_id": content_id,
        "country_id": country_id,
    }

    mock_repository.update.assert_called_once_with(
        content_country_id=content_country_id,
        content_id=content_id,
        country_id=country_id,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    content_id = 1
    country_id = 1
    content_country_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            content_country_id=content_country_id,
            content_id=content_id,
            country_id=country_id,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    content_country_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(content_country_id=content_country_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(
        content_country_id=content_country_id
    )


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    content_country_id = None

    with pytest.raises(ValueError):
        await service.delete(content_country_id=content_country_id)

    mock_repository.delete.assert_not_called()
