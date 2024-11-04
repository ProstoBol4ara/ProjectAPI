from repositories import CouponsRepository
from unittest.mock import AsyncMock
from services import CouponsService
import pytest


@pytest.fixture
def mock_repository():
    return AsyncMock(spec=CouponsRepository)


@pytest.fixture
def service(mock_repository):
    return CouponsService(repository=mock_repository)


@pytest.mark.asyncio
async def test_get_all(service, mock_repository):
    mock_repository.get_all.return_value = [
        AsyncMock(
            coupon_id=1,
            code="test_code1",
            discount_percentage=0.05,
            valid_from="2000-10-10",
            valid_until="2000-11-11",
        ),
        AsyncMock(
            coupon_id=2,
            code="test_code2",
            discount_percentage=0.01,
            valid_from="2000-11-11",
            valid_until="2000-12-12",
        ),
    ]

    coupons = await service.get_all()

    assert coupons == [
        {
            "coupon_id": 1,
            "discount_percentage": 0.05,
            "valid_from": "2000-10-10",
            "valid_until": "2000-11-11",
        },
        {
            "coupon_id": 2,
            "discount_percentage": 0.01,
            "valid_from": "2000-11-11",
            "valid_until": "2000-12-12",
        },
    ]
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_one(service, mock_repository):
    discount_percentage = 0.05
    valid_until = "2000-11-11"
    valid_from = "2000-10-10"
    code = "test_code1"
    coupon_id = 1

    mock_repository.get_one.return_value = AsyncMock(
        coupon_id=coupon_id,
        code=code,
        discount_percentage=discount_percentage,
        valid_from=valid_from,
        valid_until=valid_until,
    )

    coupon = await service.get_one(coupon_id=coupon_id)

    assert coupon == {
        "coupon_id": coupon_id,
        "discount_percentage": discount_percentage,
        "valid_from": valid_from,
        "valid_until": valid_until,
    }

    mock_repository.get_one.assert_called_once_with(coupon_id=coupon_id)


@pytest.mark.asyncio
async def test_get_null(service, mock_repository):
    coupon_id = None

    with pytest.raises(ValueError):
        await service.get_one(coupon_id=coupon_id)

    mock_repository.get_one.assert_not_called()


@pytest.mark.asyncio
async def test_create(service, mock_repository):
    discount_percentage = 0.05
    valid_until = "11.11.2000"
    valid_from = "10.10.2000"
    code = "test_code1"
    coupon_id = 1

    mock_repository.create.return_value = AsyncMock(
        coupon_id=coupon_id,
        code=code,
        discount_percentage=discount_percentage,
        valid_from=valid_from,
        valid_until=valid_until,
    )

    coupon = await service.create(
        code=code,
        discount_percentage=discount_percentage,
        valid_from=valid_from,
        valid_until=valid_until,
    )

    assert coupon == {
        "coupon_id": coupon_id,
        "discount_percentage": discount_percentage,
        "valid_from": valid_from,
        "valid_until": valid_until,
    }

    mock_repository.create.assert_called_once_with(
        code=code,
        discount_percentage=discount_percentage,
        valid_from=valid_from,
        valid_until=valid_until,
    )


@pytest.mark.asyncio
async def test_invalid_create(service, mock_repository):
    valid_until = "2000-11-11"
    valid_from = "2000-10-10"
    discount_percentage = 0
    code = "test_code1"

    with pytest.raises(ValueError):
        await service.create(
            code=code,
            discount_percentage=discount_percentage,
            valid_from=valid_from,
            valid_until=valid_until,
        )

    mock_repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_update(service, mock_repository):
    discount_percentage = 0.05
    valid_until = "11.11.2000"
    valid_from = "10.10.2000"
    code = "test_code1"
    coupon_id = 1

    mock_repository.update.return_value = AsyncMock(
        coupon_id=coupon_id,
        code=code,
        discount_percentage=discount_percentage,
        valid_from=valid_from,
        valid_until=valid_until,
    )

    coupon = await service.update(
        coupon_id=coupon_id,
        code=code,
        discount_percentage=discount_percentage,
        valid_from=valid_from,
        valid_until=valid_until,
    )

    assert coupon == {
        "coupon_id": coupon_id,
        "discount_percentage": discount_percentage,
        "valid_from": valid_from,
        "valid_until": valid_until,
    }

    mock_repository.update.assert_called_once_with(
        coupon_id=coupon_id,
        code=code,
        discount_percentage=discount_percentage,
        valid_from=valid_from,
        valid_until=valid_until,
    )


@pytest.mark.asyncio
async def test_invalid_update(service, mock_repository):
    valid_until = "2000-11-11"
    valid_from = "2000-10-10"
    discount_percentage = 0
    code = "test_code1"
    coupon_id = None

    mock_repository.update.return_value = None

    with pytest.raises(ValueError):
        await service.update(
            coupon_id=coupon_id,
            code=code,
            discount_percentage=discount_percentage,
            valid_from=valid_from,
            valid_until=valid_until,
        )

    mock_repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_delete(service, mock_repository):
    coupon_id = 1

    mock_repository.delete.return_value = True

    result = await service.delete(coupon_id=coupon_id)

    assert result is True
    mock_repository.delete.assert_called_once_with(coupon_id=coupon_id)


@pytest.mark.asyncio
async def test_delete_null(service, mock_repository):
    coupon_id = None

    with pytest.raises(ValueError):
        await service.delete(coupon_id=coupon_id)

    mock_repository.delete.assert_not_called()
