from repositories import ReviewsRepository
from unittest.mock import AsyncMock
from services import ReviewsService
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=ReviewsRepository)


@pytest.fixture
def service(mock_repository):
    return ReviewsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(review_id=1, content_id=1, user_id=1, rating=1, comment="aaa"),
        AsyncMock(review_id=2, content_id=1, user_id=2, rating=4, comment="bbb"),
    ]

    reviews = await service.get_all()

    assert reviews == [
        {"review_id": 1, "content_id": 1, "user_id": 1, "rating": 1, "comment": "aaa"},
        {"review_id": 2, "content_id": 1, "user_id": 2, "rating": 4, "comment": "bbb"},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    comment = "aaa"
    content_id = 1
    review_id = 1
    user_id = 1
    rating = 1

    mock_repository.get_one.return_value = AsyncMock(
        review_id=review_id,
        content_id=content_id,
        user_id=user_id,
        rating=rating,
        comment=comment,
    )

    review = await service.get_one(review_id=review_id)

    assert review == {
        "review_id": review_id,
        "content_id": content_id,
        "user_id": user_id,
        "rating": rating,
        "comment": comment,
    }

    mock_repository.get_one.assert_called_once_with(review_id=review_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    review_id = None

    with pytest.raises(ValueError):
        await service.get_one(review_id=review_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    comment = "aaa"
    content_id = 1
    review_id = 1
    user_id = 1
    rating = 1

    mock_repository.create.return_value = AsyncMock(
        review_id=review_id,
        content_id=content_id,
        user_id=user_id,
        rating=rating,
        comment=comment,
    )

    review = await service.create(
        content_id=content_id, user_id=user_id, rating=rating, comment=comment
    )

    assert review == {
        "review_id": review_id,
        "content_id": content_id,
        "user_id": user_id,
        "rating": rating,
        "comment": comment,
    }

    mock_repository.create.assert_called_once_with(
        content_id=content_id, user_id=user_id, rating=rating, comment=comment
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    comment = "aaa"
    content_id = 1
    user_id = "123"
    rating = None

    with pytest.raises(ValueError):
        await service.create(
            content_id=content_id, user_id=user_id, rating=rating, comment=comment
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    comment = "aaa"
    content_id = 1
    review_id = 1
    user_id = 1
    rating = 2

    mock_repository.update.return_value = AsyncMock(
        review_id=review_id,
        content_id=content_id,
        user_id=user_id,
        rating=rating,
        comment=comment,
    )

    review = await service.update(
        review_id=review_id,
        content_id=content_id,
        user_id=user_id,
        rating=rating,
        comment=comment,
    )

    assert review == {
        "review_id": review_id,
        "content_id": content_id,
        "user_id": user_id,
        "rating": rating,
        "comment": comment,
    }

    mock_repository.update.assert_called_once_with(
        review_id=review_id,
        content_id=content_id,
        user_id=user_id,
        rating=rating,
        comment=comment,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    comment = "aaa"
    content_id = 1
    review_id = None
    user_id = 1
    rating = 2

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            review_id=review_id,
            content_id=content_id,
            user_id=user_id,
            rating=rating,
            comment=comment,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    review_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(review_id=review_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(review_id=review_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    review_id = None

    with pytest.raises(ValueError):
        await service.delete(review_id=review_id)

    mock_repository.delete.assert_not_called()
