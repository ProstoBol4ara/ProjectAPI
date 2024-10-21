from repositories import CouponsRepository

class CouponsService:
    def __init__(self, coupons_repository: CouponsRepository):
        self.coupons_repository = coupons_repository

    async def get_coupons(self):
        return await self.coupons_repository.get_coupons()

    async def get_coupon(self, coupon_id: int):
        return await self.coupons_repository.get_coupon(coupon_id=coupon_id)

    async def create_coupon(self, code: str, discount_percentage: float, valid_from: str = None, valid_until: str = None):
        return await self.coupons_repository.create_coupon(code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)

    async def update_coupon(self, coupon_id: int, code: str = None, discount_percentage: float = None, valid_from: str = None, valid_until: str = None):
        return await self.coupons_repository.update_coupon(coupon_id=coupon_id, code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)

    async def delete_coupon(self, coupon_id: int):
        await self.coupons_repository.delete_coupon(coupon_id=coupon_id)
    