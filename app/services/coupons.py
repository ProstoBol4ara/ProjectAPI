from repositories import CouponsRepository
from constants import date_pattern
from re import match


class CouponsService:

    def __init__(self, repository: CouponsRepository):
        self.repository = repository

    async def get_all(self):
        coupons = await self.repository.get_all()

        return (
            None
            if coupons is None
            else [
                {
                    "coupon_id": coupon.coupon_id,
                    "discount_percentage": coupon.discount_percentage,
                    "valid_from": coupon.valid_from,
                    "valid_until": coupon.valid_until,
                }
                for coupon in coupons
            ]
        )

    async def get_one(self, coupon_id: int):
        if not coupon_id:
            raise ValueError("coupon_id cannot be empty")

        coupon = await self.repository.get_one(coupon_id=coupon_id)

        if not coupon:
            raise ValueError("Coupon not found")

        return {
            "coupon_id": coupon.coupon_id,
            "discount_percentage": coupon.discount_percentage,
            "valid_from": coupon.valid_from,
            "valid_until": coupon.valid_until,
        }

    async def create(
        self,
        code: str,
        discount_percentage: float,
        valid_from: str = None,
        valid_until: str = None,
    ):
        if not code or not discount_percentage:
            raise ValueError("Code and discount_percentage cannot be empty")

        if valid_from and not match(date_pattern, valid_from):
            raise ValueError("Invalid valid_from! Date format: day.month.year")

        if valid_until and not match(date_pattern, valid_until):
            raise ValueError("Invalid valid_until! Date format: day.month.year")

        if not 0 < discount_percentage < 1:
            raise ValueError("rating can be greater than 0 and less than 1.")

        new_coupon = await self.repository.create(
            code=code,
            discount_percentage=discount_percentage,
            valid_from=valid_from,
            valid_until=valid_until,
        )

        return {
            "coupon_id": new_coupon.coupon_id,
            "discount_percentage": new_coupon.discount_percentage,
            "valid_from": new_coupon.valid_from,
            "valid_until": new_coupon.valid_until,
        }

    async def update(
        self,
        coupon_id: int,
        code: str = None,
        discount_percentage: float = None,
        valid_from: str = None,
        valid_until: str = None,
    ):

        if not coupon_id:
            raise ValueError("coupon_id cannot be empty")

        if not valid_from or not match(date_pattern, valid_from):
            raise ValueError("Invalid valid_from! Date format: day.month.year")

        if not valid_until or not match(date_pattern, valid_until):
            raise ValueError("Invalid valid_until! Date format: day.month.year")

        if not discount_percentage or not 0 < discount_percentage < 1:
            raise ValueError("rating can be greater than 0 and less than 1.")

        coupon = await self.repository.update(
            coupon_id=coupon_id,
            code=code,
            discount_percentage=discount_percentage,
            valid_from=valid_from,
            valid_until=valid_until,
        )

        if not coupon:
            raise ValueError("Coupon not found")

        return {
            "coupon_id": coupon.coupon_id,
            "discount_percentage": coupon.discount_percentage,
            "valid_from": coupon.valid_from,
            "valid_until": coupon.valid_until,
        }

    async def delete(self, coupon_id: int):
        if not coupon_id:
            raise ValueError("coupon_id cannot be empty")

        if not (delete_coupon := await self.repository.delete(coupon_id=coupon_id)):
            raise ValueError("Coupon not found")
        return delete_coupon
