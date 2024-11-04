from repositories import PaymentMethodsRepository
from services import PaymentMethodsService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=PaymentMethodsRepository)


@pytest.fixture
def service(mock_repository):
    return PaymentMethodsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(payment_method_id=1, user_id=1, method_type="test_type1"),
        AsyncMock(payment_method_id=2, user_id=1, method_type="test_type2"),
    ]

    payment_methods = await service.get_all()

    assert payment_methods == [
        {"payment_method_id": 1, "user_id": 1, "method_type": "test_type1"},
        {"payment_method_id": 2, "user_id": 1, "method_type": "test_type2"},
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    method_type = "test_type1"
    payment_method_id = 1
    user_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        payment_method_id=payment_method_id, user_id=user_id, method_type=method_type
    )

    payment_method = await service.get_one(payment_method_id=payment_method_id)

    assert payment_method == {
        "payment_method_id": payment_method_id,
        "user_id": user_id,
        "method_type": method_type,
    }

    mock_repository.get_one.assert_called_once_with(payment_method_id=payment_method_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    payment_method_id = None

    with pytest.raises(ValueError):
        await service.get_one(payment_method_id=payment_method_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    account_number = "test_account_number"
    provider = ("test_provider",)
    payment_method_id = 1
    method_type = "SBP"
    user_id = 1

    mock_repository.create.return_value = AsyncMock(
        payment_method_id=payment_method_id,
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )

    payment_method = await service.create(
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )

    assert payment_method == {
        "payment_method_id": payment_method_id,
        "user_id": user_id,
        "method_type": method_type,
        "provider": provider,
        "account_number": account_number,
    }

    mock_repository.create.assert_called_once_with(
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    method_type = "test_type1"
    user_id = None
    provider = ""
    account_number = ""

    with pytest.raises(ValueError):
        await service.create(
            user_id=user_id,
            method_type=method_type,
            provider=provider,
            account_number=account_number,
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    account_number = "test_account_number"
    provider = ("test_provider",)
    payment_method_id = 1
    method_type = "SBP"
    user_id = 1

    mock_repository.update.return_value = AsyncMock(
        payment_method_id=payment_method_id,
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )

    payment_method = await service.update(
        payment_method_id=payment_method_id,
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )

    assert payment_method == {
        "payment_method_id": payment_method_id,
        "user_id": user_id,
        "method_type": method_type,
    }

    mock_repository.update.assert_called_once_with(
        payment_method_id=payment_method_id,
        user_id=user_id,
        method_type=method_type,
        provider=provider,
        account_number=account_number,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    account_number = "test_account_number"
    provider = ("test_provider",)
    payment_method_id = None
    method_type = "SBP"
    user_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            payment_method_id=payment_method_id,
            user_id=user_id,
            method_type=method_type,
            provider=provider,
            account_number=account_number,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    payment_method_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(payment_method_id=payment_method_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(payment_method_id=payment_method_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    payment_method_id = None

    with pytest.raises(ValueError):
        await service.delete(payment_method_id=payment_method_id)

    mock_repository.delete.assert_not_called()
