from repositories import PayPerViewRepository


class PayPerViewService:
    def __init__(self, repository: PayPerViewRepository):
        self.repository = repository

    async def get_all(self):
        pay_per_views = await self.repository.get_all()

        return (
            None
            if pay_per_views is None
            else [
                {
                    "pay_per_view_id": pay_per_view.pay_per_view_id,
                    "amount": pay_per_view.amount,
                    "content_id": pay_per_view.content_id,
                }
                for pay_per_view in pay_per_views
            ]
        )

    async def get_one(self, pay_per_view_id: int):
        if not pay_per_view_id:
            raise ValueError("pay_per_view_id cannot be empty")

        pay_per_view = await self.repository.get_one(pay_per_view_id=pay_per_view_id)

        if not pay_per_view:
            raise ValueError("Pay per view not found")

        return {
            "pay_per_view_id": pay_per_view.pay_per_view_id,
            "amount": pay_per_view.amount,
            "content_id": pay_per_view.content_id,
        }

    async def create(self, amount: float, content_id: float):
        if not amount or not content_id:
            raise ValueError("amount and content_id cannot be empty")

        if amount < 0:
            raise ValueError("amount can be greater than 0")

        new_pay_per_view = await self.repository.create(
            amount=amount, content_id=content_id
        )

        return {
            "pay_per_view_id": new_pay_per_view.pay_per_view_id,
            "amount": new_pay_per_view.amount,
            "content_id": new_pay_per_view.content_id,
        }

    async def update(
        self, pay_per_view_id: int, amount: float = None, content_id: float = None
    ):
        if not pay_per_view_id:
            raise ValueError("pay_per_view_id cannot be empty")

        if not amount or amount < 0:
            raise ValueError("amount can be greater than 0")

        pay_per_view = await self.repository.update(
            pay_per_view_id=pay_per_view_id, amount=amount, content_id=content_id
        )

        if not pay_per_view:
            raise ValueError("Pay per view not found")

        return {
            "pay_per_view_id": pay_per_view.pay_per_view_id,
            "amount": pay_per_view.amount,
            "content_id": pay_per_view.content_id,
        }

    async def delete(self, pay_per_view_id: int):
        if not pay_per_view_id:
            raise ValueError("pay_per_view_id cannot be empty")

        if not (
            delete_pay_per_view := await self.repository.delete(
                pay_per_view_id=pay_per_view_id
            )
        ):
            raise ValueError("Pay per view not found")
        return delete_pay_per_view
