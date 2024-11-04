from repositories import ContentRepository
from services import ContentService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=ContentRepository)


@pytest.fixture
def service(mock_repository):
    return ContentService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(
            content_id=1,
            title="test_title1",
            preview_path="/preview1.jpg",
            description="test_description1",
            release_date="2002-10-11",
            content_type="Movie",
            content_path="/aaa.mp4",
        ),
        AsyncMock(
            content_id=2,
            title="test_title2",
            preview_path="/preview2.jpg",
            description="test_description2",
            release_date="2022-10-10",
            content_type="Serial",
            content_path="/bbb.mp4",
        ),
    ]

    contents = await service.get_all()

    assert contents == [
        {
            "content_id": 1,
            "title": "test_title1",
            "preview_path": "/preview1.jpg",
            "description": "test_description1",
            "release_date": "2002-10-11",
            "content_type": "Movie",
            "content_path": "/aaa.mp4",
        },
        {
            "content_id": 2,
            "title": "test_title2",
            "preview_path": "/preview2.jpg",
            "description": "test_description2",
            "release_date": "2022-10-10",
            "content_type": "Serial",
            "content_path": "/bbb.mp4",
        },
    ]

    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    description = "test_description1"
    preview_path = "/preview1.jpg"
    release_date = "2002-10-11"
    content_path = "/aaa.mp4"
    content_type = "Movie"
    title = "test_title1"
    content_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        content_id=content_id,
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )

    content = await service.get_one(content_id=content_id)

    assert content == {
        "content_id": content_id,
        "title": title,
        "preview_path": preview_path,
        "description": description,
        "release_date": release_date,
        "content_type": content_type,
        "content_path": content_path,
    }

    mock_repository.get_one.assert_called_once_with(content_id=content_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    content_id = None

    with pytest.raises(ValueError):
        await service.get_one(content_id=content_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    description = "test_description1"
    preview_path = "/preview1.jpg"
    release_date = "11.10.2002"
    content_path = "/aaa.mp4"
    content_type = "Movie"
    title = "test_title1"
    content_id = 1

    mock_repository.create.return_value = AsyncMock(
        content_id=content_id,
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )

    content = await service.create(
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )

    assert content == {
        "content_id": content_id,
        "title": title,
        "preview_path": preview_path,
        "description": description,
        "release_date": release_date,
        "content_type": content_type,
        "content_path": content_path,
    }

    mock_repository.create.assert_called_once_with(
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    description = "test_description1"
    preview_path = "/preview1.jpg"
    release_date = "2002-10-11"
    content_path = "/aaa.mp4"
    content_type = "Movie"
    title = "test_title1"

    with pytest.raises(ValueError):
        await service.create(
            title=title,
            preview_path=preview_path,
            description=description,
            release_date=release_date,
            content_type=content_type,
            content_path=content_path,
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    description = "test_description1"
    preview_path = "/preview1.jpg"
    release_date = "10.10.2002"
    content_path = "/aaa.mp4"
    content_type = "Movie"
    title = "test_title1"
    content_id = 1

    mock_repository.update.return_value = AsyncMock(
        content_id=content_id,
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )

    content = await service.update(
        content_id=content_id,
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )

    assert content == {
        "content_id": content_id,
        "title": title,
        "preview_path": preview_path,
        "description": description,
        "release_date": release_date,
        "content_type": content_type,
        "content_path": content_path,
    }

    mock_repository.update.assert_called_once_with(
        content_id=content_id,
        title=title,
        preview_path=preview_path,
        description=description,
        release_date=release_date,
        content_type=content_type,
        content_path=content_path,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    description = "test_description1"
    preview_path = "/preview1.jpg"
    release_date = "2002-10-11"
    content_path = "/aaa.mp4"
    content_type = "Maaasas"
    title = "test_title1"
    content_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            content_id=content_id,
            title=title,
            preview_path=preview_path,
            description=description,
            release_date=release_date,
            content_type=content_type,
            content_path=content_path,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    content_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(content_id=content_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(content_id=content_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    content_id = None

    with pytest.raises(ValueError):
        await service.delete(content_id=content_id)

    mock_repository.delete.assert_not_called()
