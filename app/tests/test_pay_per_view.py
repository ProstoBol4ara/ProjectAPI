from repositories import PayPerViewRepository
from services import PayPerViewService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=PayPerViewRepository)


@pytest.fixture
def service(mock_repository):
    return PayPerViewService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(pay_per_view_id=1, amount=100, content_id=1),
        AsyncMock(pay_per_view_id=2, amount=200, content_id=2),
    ]

    pay_per_views = await service.get_all()

    assert pay_per_views == [
        {"pay_per_view_id": 1, "amount": 100, "content_id": 1},
        {"pay_per_view_id": 2, "amount": 200, "content_id": 2},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    pay_per_view_id = 1
    content_id = 1
    amount = 100

    mock_repository.get_one.return_value = AsyncMock(
        pay_per_view_id=pay_per_view_id, content_id=content_id, amount=amount
    )

    pay_per_view = await service.get_one(pay_per_view_id=pay_per_view_id)

    assert pay_per_view == {
        "pay_per_view_id": pay_per_view_id,
        "amount": amount,
        "content_id": content_id,
    }
    mock_repository.get_one.assert_called_once_with(pay_per_view_id=pay_per_view_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    pay_per_view_id = None

    with pytest.raises(ValueError):
        await service.get_one(pay_per_view_id=pay_per_view_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    pay_per_view_id = 1
    content_id = 1
    amount = 100

    mock_repository.create.return_value = AsyncMock(
        pay_per_view_id=pay_per_view_id, content_id=content_id, amount=amount
    )

    pay_per_view = await service.create(content_id=content_id, amount=amount)

    assert pay_per_view == {
        "pay_per_view_id": pay_per_view_id,
        "amount": amount,
        "content_id": content_id,
    }
    mock_repository.create.assert_called_once_with(content_id=content_id, amount=amount)


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    content_id = None
    amount = None

    with pytest.raises(ValueError):
        await service.create(content_id=content_id, amount=amount)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    pay_per_view_id = 1
    content_id = 1
    amount = 100

    mock_repository.update.return_value = AsyncMock(
        pay_per_view_id=pay_per_view_id, content_id=content_id, amount=amount
    )

    pay_per_view = await service.update(
        pay_per_view_id=pay_per_view_id, content_id=content_id, amount=amount
    )

    assert pay_per_view == {
        "pay_per_view_id": pay_per_view_id,
        "amount": amount,
        "content_id": content_id,
    }

    mock_repository.update.assert_called_once_with(
        pay_per_view_id=pay_per_view_id, content_id=content_id, amount=amount
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    invalid_pay_per_view_id = None
    invalid_content_id = 1
    invalid_amount = 100

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            pay_per_view_id=invalid_pay_per_view_id,
            content_id=invalid_content_id,
            amount=invalid_amount,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    pay_per_view_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(pay_per_view_id=pay_per_view_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(pay_per_view_id=pay_per_view_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    pay_per_view_id = None

    with pytest.raises(ValueError):
        await service.delete(pay_per_view_id=pay_per_view_id)

    mock_repository.delete.assert_not_called()
