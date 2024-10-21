from database import AsyncSession
from models import Payments

class PaymentsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_payments(self):
        payments = await self.db.execute(select(Payments))
        return payments.scalar().all()

    async def get_payment(self, payment_id: int):
        payment = await self.db.execute(
            select(Payments).where(Payments.payment_id == payment_id)
        )
        return payment.scalar_one_or_none()

    async def create_payment(self, payment_method_id: int, pay_per_view_id: int):
        new_payment = Payments(payment_method_id = payment_method_id, pay_per_view_id = pay_per_view_id)
        self.db.add(new_payment)
        await self.db.commit()
        await self.db.refresh(new_payment)
        return new_payment

    async def update_payment(self, payment_id: int, payment_method_id: int, pay_per_view_id: int):
        payment = await self.db.execute(
            select(Payments).where(Payments.payment_id == payment_id)
        )
        payment = payment.scalar_one_or_none()

        if pay_per_view_id:
            payment.pay_per_view_id = pay_per_view_id
        if payment_method_id:
            payment.payment_method_id = payment_method_id

        await self.db.commit()
        await self.db.refresh(payment)
        return payment

    async def delete_payment(self, payment_id: int):
        await self.db.execute(
            delete(Payments).where(Payments.payment_id == payment_id)
        )
        await self.db.commit()