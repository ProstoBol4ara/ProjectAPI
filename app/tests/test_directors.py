from repositories import DirectorsRepository
from services import DirectorsService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=DirectorsRepository)


@pytest.fixture
def service(mock_repository):
    return DirectorsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(
            director_id=1,
            director_name="test_director1",
            biography="test_biography1",
            birth_date="2000-10-10",
        ),
        AsyncMock(
            director_id=2,
            director_name="test_director2",
            biography="test_biography2",
            birth_date="2022-10-10",
        ),
    ]

    directors = await service.get_all()

    assert directors == [
        {
            "director_id": 1,
            "director_name": "test_director1",
            "biography": "test_biography1",
            "birth_date": "2000-10-10",
        },
        {
            "director_id": 2,
            "director_name": "test_director2",
            "biography": "test_biography2",
            "birth_date": "2022-10-10",
        },
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    director_name = "test_director1"
    biography = "test_biography1"
    birth_date = "2000-10-10"
    director_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        director_id=director_id,
        director_name=director_name,
        biography=biography,
        birth_date=birth_date,
    )

    director = await service.get_one(director_id=director_id)

    assert director == {
        "director_id": director_id,
        "director_name": director_name,
        "biography": biography,
        "birth_date": birth_date,
    }

    mock_repository.get_one.assert_called_once_with(director_id=director_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    director_id = None

    with pytest.raises(ValueError):
        await service.get_one(director_id=director_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    director_name = "test_director1"
    biography = "test_biography1"
    birth_date = "10.10.2000"
    director_id = 1

    mock_repository.create.return_value = AsyncMock(
        director_id=director_id,
        director_name=director_name,
        biography=biography,
        birth_date=birth_date,
    )

    director = await service.create(
        director_name=director_name, biography=biography, birth_date=birth_date
    )

    assert director == {
        "director_id": director_id,
        "director_name": director_name,
        "biography": biography,
        "birth_date": birth_date,
    }

    mock_repository.create.assert_called_once_with(
        director_name=director_name, biography=biography, birth_date=birth_date
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    director_name = "test_director1"
    biography = "test_biography1"
    birth_date = "2000-10-10"

    with pytest.raises(ValueError):
        await service.create(
            director_name=director_name, biography=biography, birth_date=birth_date
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    director_name = "test_director1"
    biography = "test_biography1"
    birth_date = "10.10.2000"
    director_id = 1

    mock_repository.update.return_value = AsyncMock(
        director_id=director_id,
        director_name=director_name,
        biography=biography,
        birth_date=birth_date,
    )

    director = await service.update(
        director_id=director_id,
        director_name=director_name,
        biography=biography,
        birth_date=birth_date,
    )

    assert director == {
        "director_id": director_id,
        "director_name": director_name,
        "biography": biography,
        "birth_date": birth_date,
    }

    mock_repository.update.assert_called_once_with(
        director_id=director_id,
        director_name=director_name,
        biography=biography,
        birth_date=birth_date,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    director_name = "test_director1"
    biography = "test_biography1"
    birth_date = "2000-10-10"
    director_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            director_id=director_id,
            director_name=director_name,
            biography=biography,
            birth_date=birth_date,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    director_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(director_id=director_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(director_id=director_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    director_id = None

    with pytest.raises(ValueError):
        await service.delete(director_id=director_id)

    mock_repository.delete.assert_not_called()
