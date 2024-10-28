from repositories import PaymentsRepository

class PaymentsService:
    def __init__(self, payments_repository: PaymentsRepository):
        self.payments_repository = payments_repository

    async def get_payments(self):
        payments = await self.payments_repository.get_payments()
        return None if payments is None else [{"payment_id": payment.payment_id, "pay_per_view_id": payment.pay_per_view_id, "payment_method_id": payment.payment_method_id} for payment in payments]

    async def get_payment(self, payment_id: int):
        payment = await self.payments_repository.get_payment(payment_id=payment_id)
        return None if payment is None else {"payment_id": payment.payment_id, "pay_per_view_id": payment.pay_per_view_id, "payment_method_id": payment.payment_method_id}

    async def create_payment(self, payment_method_id: int, pay_per_view_id: int):
        new_payment = await self.payments_repository.create_payment(payment_method_id=payment_method_id, pay_per_view_id=pay_per_view_id)
        return {"payment_id": new_payment.payment_id, "payment_method_id": new_payment.payment_method_id, "pay_per_view_id": new_payment.pay_per_view_id}

    async def update_payment(self, payment_id: int, payment_method_id: int, pay_per_view_id: int):
        payment = await self.payments_repository.update_payment(payment_id=payment_id, payment_method_id=payment_method_id, pay_per_view_id=pay_per_view_id)
        return None if payment is None else {"payment_id": payment.payment_id, "pay_per_view_id": payment.pay_per_view_id, "payment_method_id": payment.payment_method_id}

    async def delete_payment(self, payment_id: int):
        return await self.payments_repository.delete_payment(payment_id=payment_id)
    