from repositories import CountriesRepository
from services import CountriesService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=CountriesRepository)


@pytest.fixture
def service(mock_repository):
    return CountriesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(country_id=1, country_name="test_name1"),
        AsyncMock(country_id=2, country_name="test_name2"),
    ]

    countries = await service.get_all()

    assert countries == [
        {"country_id": 1, "country_name": "test_name1"},
        {"country_id": 2, "country_name": "test_name2"},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    country_name = "test_name1"
    country_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        country_id=country_id, country_name=country_name
    )

    country = await service.get_one(country_id=country_id)

    assert country == {"country_id": country_id, "country_name": country_name}
    mock_repository.get_one.assert_called_once_with(country_id=country_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    country_id = None

    with pytest.raises(ValueError):
        await service.get_one(country_id=country_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    country_name = "test_name1"
    country_id = 1

    mock_repository.create.return_value = AsyncMock(
        country_id=country_id, country_name=country_name
    )

    country = await service.create(country_name=country_name)

    assert country == {"country_id": country_id, "country_name": country_name}
    mock_repository.create.assert_called_once_with(country_name=country_name)


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    country_name = None

    with pytest.raises(ValueError):
        await service.create(country_name=country_name)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    country_name = "test_name1"
    country_id = 1

    mock_repository.update.return_value = AsyncMock(
        country_id=country_id, country_name=country_name
    )

    country = await service.update(country_id=country_id, country_name=country_name)

    assert country == {"country_id": country_id, "country_name": country_name}

    mock_repository.update.assert_called_once_with(
        country_id=country_id, country_name=country_name
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    country_name = "test_name1"
    country_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(country_id=country_id, country_name=country_name)

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    country_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(country_id=country_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(country_id=country_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    country_id = None

    with pytest.raises(ValueError):
        await service.delete(country_id=country_id)

    mock_repository.delete.assert_not_called()
