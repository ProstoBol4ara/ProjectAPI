from database import AsyncSession
from models import PayPerView

class PayPerViewRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_pay_per_views(self):
        pay_per_views = await self.db.execute(select(PayPerView))
        return pay_per_views.scalar().all()
    
    async def get_pay_per_view(self, pay_per_view_id: int):
        pay_per_view = await self.db.execute(
            select(PayPerView).where(PayPerView.pay_per_view_id == pay_per_view_id)
        )
        return pay_per_view.scalar_one_or_none()

    async def create_pay_per_view(self, amount: float, content_id: float):
        new_pay_per_view = PayPerView(amount=amount, content_id=content_id)
        self.db.add(new_pay_per_view)
        await self.db.commit()
        await self.db.refresh(new_pay_per_view)
        return new_pay_per_view

    async def update_pay_per_view(self, pay_per_view_id: int, amount: float = None, content_id: float = None):
        pay_per_view = await self.db.execute(
            select(PayPerView).where(PayPerView.pay_per_view_id == pay_per_view_id)
        )
        pay_per_view = pay_per_view.scalar_one_or_none()

        if amount:
            pay_per_view.amount = amount
        if content_id:
            pay_per_view.content_id = content_id

        await self.db.commit()
        await self.db.refresh(pay_per_view)
        return pay_per_view

    async def delete_pay_per_view(self, pay_per_view_id: int):
        await self.db.execute(
            delete(PayPerView).where(PayPerView.pay_per_view_id == pay_per_view_id)
        )
        await self.db.commit()
