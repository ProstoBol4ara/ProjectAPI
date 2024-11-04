from repositories import PaymentsRepository


class PaymentsService:
    def __init__(self, repository: PaymentsRepository):
        self.repository = repository

    async def get_all(self):
        payments = await self.repository.get_all()

        return (
            None
            if payments is None
            else [
                {
                    "payment_id": payment.payment_id,
                    "pay_per_view_id": payment.pay_per_view_id,
                    "payment_method_id": payment.payment_method_id,
                }
                for payment in payments
            ]
        )

    async def get_one(self, payment_id: int):
        if not payment_id:
            raise ValueError("payment_id cannot be empty")

        payment = await self.repository.get_one(payment_id=payment_id)

        if not payment:
            raise ValueError("Payment not found")

        return {
            "payment_id": payment.payment_id,
            "pay_per_view_id": payment.pay_per_view_id,
            "payment_method_id": payment.payment_method_id,
        }

    async def create(self, payment_method_id: int, pay_per_view_id: int):
        if not payment_method_id or not pay_per_view_id:
            raise ValueError("payment_method_id and pay_per_view_id cannot be empty")

        new_payment = await self.repository.create(
            payment_method_id=payment_method_id, pay_per_view_id=pay_per_view_id
        )

        return {
            "payment_id": new_payment.payment_id,
            "payment_method_id": new_payment.payment_method_id,
            "pay_per_view_id": new_payment.pay_per_view_id,
        }

    async def update(
        self, payment_id: int, payment_method_id: int, pay_per_view_id: int
    ):
        if not payment_id:
            raise ValueError("payment_id cannot be empty")

        payment = await self.repository.update(
            payment_id=payment_id,
            payment_method_id=payment_method_id,
            pay_per_view_id=pay_per_view_id,
        )

        if not payment:
            raise ValueError("Payment not found")

        return {
            "payment_id": payment.payment_id,
            "pay_per_view_id": payment.pay_per_view_id,
            "payment_method_id": payment.payment_method_id,
        }

    async def delete(self, payment_id: int):
        if not payment_id:
            raise ValueError("payment_id cannot be empty")

        if not (delete_payment := await self.repository.delete(payment_id=payment_id)):
            raise ValueError("Payment not found")
        return delete_payment
