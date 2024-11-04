from database import AsyncSession, select, delete
from datetime import datetime
from models import Coupons


class CouponsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        coupons = await self.db.execute(select(Coupons))
        return coupons.scalars().all()

    async def get_one(self, coupon_id: int):
        coupon = await self.db.execute(
            select(Coupons).where(Coupons.coupon_id == coupon_id)
        )
        return coupon.scalar_one_or_none()

    async def create(
        self,
        code: str,
        discount_percentage: float,
        valid_from: str = None,
        valid_until: str = None,
    ):
        if not valid_from is None:
            valid_from = datetime.strptime(valid_from, "%d.%m.%Y").date()
        if not valid_until is None:
            valid_until = datetime.strptime(valid_until, "%d.%m.%Y").date()
        new_coupon = Coupons(
            code=code,
            discount_percentage=discount_percentage,
            valid_from=valid_from,
            valid_until=valid_until,
        )
        self.db.add(new_coupon)
        await self.db.commit()
        await self.db.refresh(new_coupon)
        return new_coupon

    async def update(
        self,
        coupon_id: int,
        code: str = None,
        discount_percentage: float = None,
        valid_from: str = None,
        valid_until: str = None,
    ):
        coupon = await self.db.execute(
            select(Coupons).where(Coupons.coupon_id == coupon_id)
        )
        coupon = coupon.scalar_one_or_none()

        if code:
            coupon.code = code
        if discount_percentage:
            coupon.discount_percentage = discount_percentage
        if valid_from:
            coupon.valid_from = datetime.strptime(valid_from, "%d.%m.%Y").date()
        if valid_until:
            coupon.valid_until = datetime.strptime(valid_until, "%d.%m.%Y").date()

        await self.db.commit()
        await self.db.refresh(coupon)
        return coupon

    async def delete(self, coupon_id: int):
        result = await self.db.execute(
            delete(Coupons).where(Coupons.coupon_id == coupon_id)
        )
        await self.db.commit()
        return result.rowcount > 0
