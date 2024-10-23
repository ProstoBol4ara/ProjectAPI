from database import AsyncSession, select, delete
from models import PaymentMethods

class PaymentMethodsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_payment_methods(self):
        payment_methods = await self.db.execute(select(PaymentMethods))
        return payment_methods.scalars().all()

    async def get_payment_method(self, payment_method_id: int):
        payment_method = await self.db.execute(
            select(PaymentMethods).where(PaymentMethods.payment_method_id == payment_method_id)
        )
        return payment_method.scalar_one_or_none()

    async def create_payment_method(self, user_id: int, method_type: str, provider: str, account_number: str):
        new_payment_method = PaymentMethods(user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
        self.db.add(new_payment_method)
        await self.db.commit()
        await self.db.refresh(new_payment_method)
        return new_payment_method

    async def update_payment_method(self, payment_method_id: int, user_id: int = None, method_type: str = None, provider: str = None, account_number: str = None):
        payment_method = await self.db.execute(
            select(PaymentMethods).where(PaymentMethods.payment_method_id == payment_method_id)
        )
        payment_method = payment_method.scalar_one_or_none()

        if user_id:
            payment_method.user_id = user_id
        if provider:
            payment_method.provider = provider
        if method_type:
            payment_method.method_type = method_type
        if account_number:
            payment_method.account_number = account_number

        await self.db.commit()
        await self.db.refresh(payment_method)
        return payment_method

    async def delete_payment_method(self, payment_method_id: int):
        result = await self.db.execute(
            delete(PaymentMethods).where(PaymentMethods.payment_method_id == payment_method_id)
        )
        await self.db.commit()
        return result.rowcount > 0