from repositories import PaymentsRepository

class PaymentsService:
    def __init__(self, payments_repository: PaymentsRepository):
        self.payments_repository = payments_repository

    async def get_payments(self):
        return await self.payments_repository.get_payments()

    async def get_payment(self, payment_id: int):
        return await self.payments_repository.get_payment(payment_id=payment_id)

    async def create_payment(self, payment_method_id: int, pay_per_view_id: int):
        return await self.payments_repository.create_payment(payment_method_id=payment_method_id, pay_per_view_id=pay_per_view_id)

    async def update_payment(self, payment_id: int, payment_method_id: int, pay_per_view_id: int):
        return await self.payments_repository.update_payment(payment_id=payment_id, payment_method_id=payment_method_id, pay_per_view_id=pay_per_view_id)

    async def delete_payment(self, payment_id: int):
        await self.payments_repository.delete_payment(payment_id=payment_id)
    