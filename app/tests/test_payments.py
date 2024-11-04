from repositories import PaymentsRepository
from services import PaymentsService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=PaymentsRepository)


@pytest.fixture
def service(mock_repository):
    return PaymentsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(payment_id=1, pay_per_view_id=1, payment_method_id=1),
        AsyncMock(payment_id=2, pay_per_view_id=2, payment_method_id=2),
    ]

    payments = await service.get_all()

    assert payments == [
        {"payment_id": 1, "pay_per_view_id": 1, "payment_method_id": 1},
        {"payment_id": 2, "pay_per_view_id": 2, "payment_method_id": 2},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    payment_method_id = 1
    pay_per_view_id = 1
    payment_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        payment_id=payment_id,
        pay_per_view_id=pay_per_view_id,
        payment_method_id=payment_method_id,
    )

    payment = await service.get_one(payment_id=payment_id)

    assert payment == {
        "payment_id": payment_id,
        "pay_per_view_id": pay_per_view_id,
        "payment_method_id": payment_method_id,
    }
    mock_repository.get_one.assert_called_once_with(payment_id=payment_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    payment_id = None

    with pytest.raises(ValueError):
        await service.get_one(payment_id=payment_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    payment_method_id = 1
    pay_per_view_id = 1
    payment_id = 1

    mock_repository.create.return_value = AsyncMock(
        payment_id=payment_id,
        pay_per_view_id=pay_per_view_id,
        payment_method_id=payment_method_id,
    )

    payment = await service.create(
        pay_per_view_id=pay_per_view_id, payment_method_id=payment_method_id
    )

    assert payment == {
        "payment_id": payment_id,
        "pay_per_view_id": pay_per_view_id,
        "payment_method_id": payment_method_id,
    }

    mock_repository.create.assert_called_once_with(
        pay_per_view_id=pay_per_view_id, payment_method_id=payment_method_id
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    payment_method_id = None
    pay_per_view_id = None

    with pytest.raises(ValueError):
        await service.create(
            pay_per_view_id=pay_per_view_id, payment_method_id=payment_method_id
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    payment_method_id = 1
    pay_per_view_id = 1
    payment_id = 1

    mock_repository.update.return_value = AsyncMock(
        payment_id=payment_id,
        pay_per_view_id=pay_per_view_id,
        payment_method_id=payment_method_id,
    )

    payment = await service.update(
        payment_id=payment_id,
        pay_per_view_id=pay_per_view_id,
        payment_method_id=payment_method_id,
    )

    assert payment == {
        "payment_id": payment_id,
        "pay_per_view_id": pay_per_view_id,
        "payment_method_id": payment_method_id,
    }

    mock_repository.update.assert_called_once_with(
        payment_id=payment_id,
        pay_per_view_id=pay_per_view_id,
        payment_method_id=payment_method_id,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    payment_method_id = 1
    pay_per_view_id = 1
    payment_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            payment_id=payment_id,
            pay_per_view_id=pay_per_view_id,
            payment_method_id=payment_method_id,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    payment_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(payment_id=payment_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(payment_id=payment_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    payment_id = None

    with pytest.raises(ValueError):
        await service.delete(payment_id=payment_id)

    mock_repository.delete.assert_not_called()
