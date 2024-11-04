from repositories import ActorsRepository
from unittest.mock import AsyncMock
from services import ActorsService
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=ActorsRepository)


@pytest.fixture
def service(mock_repository):
    return ActorsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(
            actor_id=1,
            actor_name="test_actor1",
            biography="test_biography1",
            birth_date="2002-10-10",
        ),
        AsyncMock(
            actor_id=2,
            actor_name="test_actor2",
            biography="test_biography2",
            birth_date="2022-10-10",
        ),
    ]

    actors = await service.get_all()

    assert actors == [
        {
            "actor_id": 1,
            "actor_name": "test_actor1",
            "biography": "test_biography1",
            "birth_date": "2002-10-10",
        },
        {
            "actor_id": 2,
            "actor_name": "test_actor2",
            "biography": "test_biography2",
            "birth_date": "2022-10-10",
        },
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    biography = "test_biography1"
    actor_name = "test_actor1"
    birth_date = "2002-10-10"
    actor_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        actor_id=actor_id,
        actor_name=actor_name,
        biography=biography,
        birth_date=birth_date,
    )

    actor = await service.get_one(actor_id=actor_id)

    assert actor == {
        "actor_id": 1,
        "actor_name": "test_actor1",
        "biography": "test_biography1",
        "birth_date": "2002-10-10",
    }
    mock_repository.get_one.assert_called_once_with(actor_id=actor_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    actor_id = None

    with pytest.raises(ValueError):
        await service.get_one(actor_id=actor_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    biography = "test_biography1"
    actor_name = "test_actor1"
    birth_date = "10.10.2002"
    actor_id = 1

    mock_repository.create.return_value = AsyncMock(
        actor_id=actor_id,
        actor_name=actor_name,
        biography=biography,
        birth_date=birth_date,
    )

    actor = await service.create(
        actor_name=actor_name, biography=biography, birth_date=birth_date
    )

    assert actor == {
        "actor_id": actor_id,
        "actor_name": actor_name,
        "biography": biography,
        "birth_date": birth_date,
    }

    mock_repository.create.assert_called_once_with(
        actor_name=actor_name, biography=biography, birth_date=birth_date
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    biography = "test_biography1"
    actor_name = "test_actor1"
    birth_date = "2002-10-10"

    with pytest.raises(ValueError):
        await service.create(
            actor_name=actor_name, biography=biography, birth_date=birth_date
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    biography = "test_biography1"
    actor_name = "test_actor1"
    birth_date = "10.10.2002"
    actor_id = 1

    mock_repository.update.return_value = AsyncMock(
        actor_id=actor_id,
        actor_name=actor_name,
        biography=biography,
        birth_date=birth_date,
    )

    actor = await service.update(
        actor_id=actor_id,
        actor_name=actor_name,
        biography=biography,
        birth_date=birth_date,
    )

    assert actor == {
        "actor_id": actor_id,
        "actor_name": actor_name,
        "biography": biography,
        "birth_date": birth_date,
    }

    mock_repository.update.assert_called_once_with(
        actor_id=actor_id,
        actor_name=actor_name,
        biography=biography,
        birth_date=birth_date,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    biography = "test_biography1"
    actor_name = "test_actor1"
    birth_date = "2002-10-10"
    actor_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            actor_id=actor_id,
            actor_name=actor_name,
            biography=biography,
            birth_date=birth_date,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    actor_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(actor_id=actor_id)

    assert result is True

    mock_repository.delete.assert_called_once_with(actor_id=actor_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    actor_id = None

    with pytest.raises(ValueError):
        await service.delete(actor_id=actor_id)

    mock_repository.delete.assert_not_called()
