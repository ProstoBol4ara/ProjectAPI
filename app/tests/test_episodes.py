from repositories import EpisodesRepository
from services import EpisodesService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=EpisodesRepository)


@pytest.fixture
def service(mock_repository):
    return EpisodesService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(
            episode_id=1,
            content_id=1,
            season_number=1,
            episode_number=1,
            title="test_episode1",
            release_date="2000-10-10",
            episode_path="/ep1.mp4",
        ),
        AsyncMock(
            episode_id=2,
            content_id=1,
            season_number=1,
            episode_number=2,
            title="test_episode2",
            release_date="2000-11-11",
            episode_path="/ep2.mp4",
        ),
    ]

    episodes = await service.get_all()

    assert episodes == [
        {
            "episode_id": 1,
            "content_id": 1,
            "season_number": 1,
            "episode_number": 1,
            "title": "test_episode1",
            "release_date": "2000-10-10",
            "episode_path": "/ep1.mp4",
        },
        {
            "episode_id": 2,
            "content_id": 1,
            "season_number": 1,
            "episode_number": 2,
            "title": "test_episode2",
            "release_date": "2000-11-11",
            "episode_path": "/ep2.mp4",
        },
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    release_date = "2000-10-10"
    episode_path = "/ep1.mp4"
    title = "test_episode1"
    episode_number = 1
    season_number = 1
    content_id = 1
    episode_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        episode_id=episode_id,
        content_id=content_id,
        season_number=season_number,
        episode_number=episode_number,
        title=title,
        release_date=release_date,
        episode_path=episode_path,
    )

    episode = await service.get_one(episode_id=episode_id)

    assert episode == {
        "episode_id": episode_id,
        "content_id": content_id,
        "season_number": season_number,
        "episode_number": episode_number,
        "title": title,
        "release_date": release_date,
        "episode_path": episode_path,
    }

    mock_repository.get_one.assert_called_once_with(episode_id=episode_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    episode_id = None

    with pytest.raises(ValueError):
        await service.get_one(episode_id=episode_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    release_date = "10.10.2000"
    episode_path = "/ep1.mp4"
    title = "test_episode1"
    episode_number = 1
    season_number = 1
    content_id = 1
    episode_id = 1

    mock_repository.create.return_value = AsyncMock(
        episode_id=episode_id,
        content_id=content_id,
        season_number=season_number,
        episode_number=episode_number,
        title=title,
        release_date=release_date,
        episode_path=episode_path,
    )

    episode = await service.create(
        content_id=content_id,
        season_number=season_number,
        episode_number=episode_number,
        title=title,
        release_date=release_date,
        episode_path=episode_path,
    )

    assert episode == {
        "episode_id": episode_id,
        "content_id": content_id,
        "season_number": season_number,
        "episode_number": episode_number,
        "title": title,
        "release_date": release_date,
        "episode_path": episode_path,
    }

    mock_repository.create.assert_called_once_with(
        content_id=content_id,
        season_number=season_number,
        episode_number=episode_number,
        title=title,
        release_date=release_date,
        episode_path=episode_path,
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    release_date = "2000-10-10"
    episode_path = "/ep1.mp4"
    title = "test_episode1"
    episode_number = 1
    season_number = 1
    content_id = 1

    with pytest.raises(ValueError):
        await service.create(
            content_id=content_id,
            season_number=season_number,
            episode_number=episode_number,
            title=title,
            release_date=release_date,
            episode_path=episode_path,
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    release_date = "10.10.2000"
    episode_path = "/ep1.mp4"
    title = "test_episode1"
    episode_number = 1
    season_number = 1
    content_id = 1
    episode_id = 1

    mock_repository.update.return_value = AsyncMock(
        episode_id=episode_id,
        content_id=content_id,
        season_number=season_number,
        episode_number=episode_number,
        title=title,
        release_date=release_date,
        episode_path=episode_path,
    )

    episode = await service.update(
        episode_id=episode_id,
        content_id=content_id,
        season_number=season_number,
        episode_number=episode_number,
        title=title,
        release_date=release_date,
        episode_path=episode_path,
    )

    assert episode == {
        "episode_id": episode_id,
        "content_id": content_id,
        "season_number": season_number,
        "episode_number": episode_number,
        "title": title,
        "release_date": release_date,
        "episode_path": episode_path,
    }

    mock_repository.update.assert_called_once_with(
        episode_id=episode_id,
        content_id=content_id,
        season_number=season_number,
        episode_number=episode_number,
        title=title,
        release_date=release_date,
        episode_path=episode_path,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    release_date = "2000-10-10"
    episode_path = "/ep1.mp4"
    title = "test_episode1"
    episode_number = 1
    season_number = 1
    episode_id = 1
    content_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            episode_id=episode_id,
            content_id=content_id,
            season_number=season_number,
            episode_number=episode_number,
            title=title,
            release_date=release_date,
            episode_path=episode_path,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    episode_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(episode_id=episode_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(episode_id=episode_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    episode_id = None

    with pytest.raises(ValueError):
        await service.delete(episode_id=episode_id)

    mock_repository.delete.assert_not_called()
