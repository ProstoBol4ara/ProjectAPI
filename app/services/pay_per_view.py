from repositories import PayPerViewRepository

class PayPerViewService:
    def __init__(self, pay_per_view_repository: PayPerViewRepository):
        self.pay_per_view_repository = pay_per_view_repository

    async def get_pay_per_views(self):
        pay_per_views = await self.pay_per_view_repository.get_pay_per_views()
        return None if pay_per_views is None else [{"pay_per_view_id": pay_per_view.pay_per_view_id, "amount": pay_per_view.amount, "content_id": pay_per_view.content_id} for pay_per_view in pay_per_views]
    
    async def get_pay_per_view(self, pay_per_view_id: int):
        pay_per_view = await self.pay_per_view_repository.get_pay_per_view(pay_per_view_id=pay_per_view_id)
        return None if pay_per_view is None else {"pay_per_view_id": pay_per_view.pay_per_view_id, "amount": pay_per_view.amount, "content_id": pay_per_view.content_id}

    async def create_pay_per_view(self, amount: float, content_id: float):
        new_pay_per_view = await self.pay_per_view_repository.create_pay_per_view(amount=amount, content_id=content_id)
        return {"pay_per_view_id": new_pay_per_view.pay_per_view_id, "amount": new_pay_per_view.amount, "content_id": new_pay_per_view.content_id}
        
    async def update_pay_per_view(self, pay_per_view_id: int, amount: float = None, content_id: float = None):
        pay_per_view = await self.pay_per_view_repository.update_pay_per_view(pay_per_view_id=pay_per_view_id, amount=amount, content_id=content_id)
        return None if pay_per_view is None else {"pay_per_view_id": pay_per_view.pay_per_view_id, "amount": pay_per_view.amount, "content_id": pay_per_view.content_id}

    async def delete_pay_per_view(self, pay_per_view_id: int):
        return await self.pay_per_view_repository.delete_pay_per_view(pay_per_view_id=pay_per_view_id)
    