from repositories import ContentActorsRepository
from services import ContentActorsService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=ContentActorsRepository)


@pytest.fixture
def service(mock_repository):
    return ContentActorsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(content_actor_id=1, content_id=1, actor_id=1, role="Loser"),
        AsyncMock(content_actor_id=1, content_id=1, actor_id=2, role="Niko-Niko-Nii"),
    ]

    content_actors = await service.get_all()

    assert content_actors == [
        {"content_actor_id": 1, "content_id": 1, "actor_id": 1, "role": "Loser"},
        {
            "content_actor_id": 1,
            "content_id": 1,
            "actor_id": 2,
            "role": "Niko-Niko-Nii",
        },
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    content_actor_id = 1
    content_id = 1
    role = "Loser"
    actor_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        content_actor_id=content_actor_id,
        content_id=content_id,
        actor_id=actor_id,
        role=role,
    )

    content_actor = await service.get_one(content_actor_id=content_actor_id)

    assert content_actor == {
        "content_actor_id": content_actor_id,
        "content_id": content_id,
        "actor_id": actor_id,
        "role": role,
    }
    mock_repository.get_one.assert_called_once_with(content_actor_id=content_actor_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    content_actor_id = None

    with pytest.raises(ValueError):
        await service.get_one(content_actor_id=content_actor_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    content_actor_id = 1
    content_id = 1
    role = "Loser"
    actor_id = 1

    mock_repository.create.return_value = AsyncMock(
        content_actor_id=content_actor_id,
        content_id=content_id,
        actor_id=actor_id,
        role=role,
    )

    content_actor = await service.create(
        content_id=content_id, actor_id=actor_id, role=role
    )

    assert content_actor == {
        "content_actor_id": content_actor_id,
        "content_id": content_id,
        "actor_id": actor_id,
        "role": role,
    }

    mock_repository.create.assert_called_once_with(
        content_id=content_id, actor_id=actor_id, role=role
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    content_id = None
    role = None
    actor_id = None

    with pytest.raises(ValueError):
        await service.create(content_id=content_id, actor_id=actor_id, role=role)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    content_actor_id = 1
    content_id = 1
    role = "Loser"
    actor_id = 1

    mock_repository.update.return_value = AsyncMock(
        content_actor_id=content_actor_id,
        content_id=content_id,
        actor_id=actor_id,
        role=role,
    )

    content_actor = await service.update(
        content_actor_id=content_actor_id,
        content_id=content_id,
        actor_id=actor_id,
        role=role,
    )

    assert content_actor == {
        "content_actor_id": content_actor_id,
        "content_id": content_id,
        "actor_id": actor_id,
        "role": role,
    }

    mock_repository.update.assert_called_once_with(
        content_actor_id=content_actor_id,
        content_id=content_id,
        actor_id=actor_id,
        role=role,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    role = "Loser"
    content_id = 2
    actor_id = 2
    content_actor_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            content_actor_id=content_actor_id,
            content_id=content_id,
            actor_id=actor_id,
            role=role,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    content_actor_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(content_actor_id=content_actor_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(content_actor_id=content_actor_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    content_actor_id = None

    with pytest.raises(ValueError):
        await service.delete(content_actor_id=content_actor_id)

    mock_repository.delete.assert_not_called()
