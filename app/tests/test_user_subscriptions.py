from repositories import UserSubscriptionsRepository
from services import UserSubscriptionsService
from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=UserSubscriptionsRepository)


@pytest.fixture
def service(mock_repository):
    return UserSubscriptionsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(
            user_subscription_id=1,
            start_date="2000-10-10",
            end_date="2000-11-11",
            user_id=1,
            plan_id=1,
        ),
        AsyncMock(
            user_subscription_id=2,
            start_date="2022-10-10",
            end_date="2022-11-11",
            user_id=2,
            plan_id=2,
        ),
    ]

    users = await service.get_all()

    assert users == [
        {
            "user_subscription_id": 1,
            "start_date": "2000-10-10",
            "end_date": "2000-11-11",
            "user_id": 1,
            "plan_id": 1,
        },
        {
            "user_subscription_id": 2,
            "start_date": "2022-10-10",
            "end_date": "2022-11-11",
            "user_id": 2,
            "plan_id": 2,
        },
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    start_date = "2000-10-10"
    user_subscription_id = 1
    end_date = "2000-11-11"
    user_id = 1
    plan_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        user_subscription_id=user_subscription_id,
        start_date=start_date,
        end_date=end_date,
        user_id=user_id,
        plan_id=plan_id,
    )

    user_subscription = await service.get_one(user_subscription_id=user_subscription_id)

    assert user_subscription == {
        "user_subscription_id": user_subscription_id,
        "start_date": start_date,
        "end_date": end_date,
        "user_id": user_id,
        "plan_id": plan_id,
    }

    mock_repository.get_one.assert_called_once_with(
        user_subscription_id=user_subscription_id
    )


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    user_subscription_id = None

    with pytest.raises(ValueError):
        await service.get_one(user_subscription_id=user_subscription_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    start_date = "10.10.2000"
    user_subscription_id = 1
    end_date = "11.11.2000"
    user_id = 1
    plan_id = 1

    mock_repository.create.return_value = AsyncMock(
        user_subscription_id=user_subscription_id,
        start_date=start_date,
        end_date=end_date,
        user_id=user_id,
        plan_id=plan_id,
    )

    user_subscription = await service.create(
        start_date=start_date, end_date=end_date, user_id=user_id, plan_id=plan_id
    )

    assert user_subscription == {
        "user_subscription_id": user_subscription_id,
        "start_date": start_date,
        "end_date": end_date,
        "user_id": user_id,
        "plan_id": plan_id,
    }

    mock_repository.create.assert_called_once_with(
        start_date=start_date, end_date=end_date, user_id=user_id, plan_id=plan_id
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    start_date = "2000-10-10"
    end_date = "2000-11-11"
    user_id = 1
    plan_id = 1

    with pytest.raises(ValueError):
        await service.create(
            start_date=start_date, end_date=end_date, user_id=user_id, plan_id=plan_id
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    start_date = "10.10.2000"
    user_subscription_id = 1
    end_date = "11.11.2000"
    user_id = 1
    plan_id = 1

    mock_repository.update.return_value = AsyncMock(
        user_subscription_id=user_subscription_id,
        start_date=start_date,
        end_date=end_date,
        user_id=user_id,
        plan_id=plan_id,
    )

    user_subscription = await service.update(
        user_subscription_id=user_subscription_id,
        start_date=start_date,
        end_date=end_date,
        user_id=user_id,
        plan_id=plan_id,
    )

    assert user_subscription == {
        "user_subscription_id": user_subscription_id,
        "start_date": start_date,
        "end_date": end_date,
        "user_id": user_id,
        "plan_id": plan_id,
    }

    mock_repository.update.assert_called_once_with(
        user_subscription_id=user_subscription_id,
        start_date=start_date,
        end_date=end_date,
        user_id=user_id,
        plan_id=plan_id,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    start_date = "10.10.2000"
    user_subscription_id = None
    end_date = "11.11.2000"
    user_id = 1
    plan_id = 1

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            user_subscription_id=user_subscription_id,
            start_date=start_date,
            end_date=end_date,
            user_id=user_id,
            plan_id=plan_id,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    user_subscription_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(user_subscription_id=user_subscription_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(
        user_subscription_id=user_subscription_id
    )


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    user_subscription_id = None

    with pytest.raises(ValueError):
        await service.delete(user_subscription_id=user_subscription_id)

    mock_repository.delete.assert_not_called()
