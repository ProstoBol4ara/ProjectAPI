from repositories import CouponsRepository

class CouponsService:
    def __init__(self, coupons_repository: CouponsRepository):
        self.coupons_repository = coupons_repository

    async def get_coupons(self):
        coupons = await self.coupons_repository.get_coupons()
        return None if coupons is None else [{"coupon_id": coupon.coupon_id, "code": coupon.code, "discount_percentage": coupon.discount_percentage, "valid_from": coupon.valid_from, "valid_until": coupon.valid_until} for coupon in coupons]

    async def get_coupon(self, coupon_id: int):
        coupon = await self.coupons_repository.get_coupon(coupon_id=coupon_id)

        if not coupon: raise ValueError("Coupon not found")

        return {"coupon_id": coupon.coupon_id, "code": coupon.code, "discount_percentage": coupon.discount_percentage, "valid_from": coupon.valid_from, "valid_until": coupon.valid_until}

    async def create_coupon(self, code: str, discount_percentage: float, valid_from: str = None, valid_until: str = None):
        new_coupon = await self.coupons_repository.create_coupon(code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)
        return {"coupon_id": new_coupon.coupon_id, "code": new_coupon.code, "discount_percentage": new_coupon.discount_percentage, "valid_from": new_coupon.valid_from, "valid_until": new_coupon.valid_until}

    async def update_coupon(self, coupon_id: int, code: str = None, discount_percentage: float = None, valid_from: str = None, valid_until: str = None):
        coupon = await self.coupons_repository.update_coupon(coupon_id=coupon_id, code=code, discount_percentage=discount_percentage, valid_from=valid_from, valid_until=valid_until)

        if not coupon: raise ValueError("Coupon not found")

        return {"coupon_id": coupon.coupon_id, "code": coupon.code, "discount_percentage": coupon.discount_percentage, "valid_from": coupon.valid_from, "valid_until": coupon.valid_until}

    async def delete_coupon(self, coupon_id: int):
        if not await self.coupons_repository.delete_coupon(coupon_id=coupon_id): raise ValueError("Coupon not found")
