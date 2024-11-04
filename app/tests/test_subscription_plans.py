from repositories import SubscriptionPlansRepository
from services import SubscriptionPlansService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=SubscriptionPlansRepository)


@pytest.fixture
def service(mock_repository):
    return SubscriptionPlansService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(plan_id=1, plan_name="test_name1", plan_price=100),
        AsyncMock(plan_id=2, plan_name="test_name2", plan_price=200),
    ]

    subscription_plans = await service.get_all()

    assert subscription_plans == [
        {"plan_id": 1, "plan_name": "test_name1", "plan_price": 100},
        {"plan_id": 2, "plan_name": "test_name2", "plan_price": 200},
    ]

    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    plan_name = "test_name1"
    plan_price = 100
    plan_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        plan_id=plan_id, plan_name=plan_name, plan_price=plan_price
    )

    subscription_plan = await service.get_one(plan_id=plan_id)

    assert subscription_plan == {
        "plan_id": plan_id,
        "plan_name": plan_name,
        "plan_price": plan_price,
    }
    mock_repository.get_one.assert_called_once_with(plan_id=plan_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    plan_id = None

    with pytest.raises(ValueError):
        await service.get_one(plan_id=plan_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    plan_name = "test_name1"
    plan_price = 100
    plan_id = 1

    mock_repository.create.return_value = AsyncMock(
        plan_id=plan_id, plan_name=plan_name, plan_price=plan_price
    )

    subscription_plan = await service.create(plan_name=plan_name, plan_price=plan_price)

    assert subscription_plan == {
        "plan_id": plan_id,
        "plan_name": plan_name,
        "plan_price": plan_price,
    }

    mock_repository.create.assert_called_once_with(
        plan_name=plan_name, plan_price=plan_price
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    plan_name = None
    plan_price = -100

    with pytest.raises(ValueError):
        await service.create(plan_name=plan_name, plan_price=plan_price)

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    plan_name = "test_name1"
    plan_price = 100
    plan_id = 1

    mock_repository.update.return_value = AsyncMock(
        plan_id=plan_id, plan_name=plan_name, plan_price=plan_price
    )

    subscription_plan = await service.update(
        plan_id=plan_id, plan_name=plan_name, plan_price=plan_price
    )

    assert subscription_plan == {
        "plan_id": plan_id,
        "plan_name": plan_name,
        "plan_price": plan_price,
    }

    mock_repository.update.assert_called_once_with(
        plan_id=plan_id, plan_name=plan_name, plan_price=plan_price
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    plan_name = "test_name1"
    plan_price = -100
    plan_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            plan_id=plan_id, plan_name=plan_name, plan_price=plan_price
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    plan_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(plan_id=plan_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(plan_id=plan_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    plan_id = None

    with pytest.raises(ValueError):
        await service.delete(plan_id=plan_id)

    mock_repository.delete.assert_not_called()
