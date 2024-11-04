from repositories import PaymentMethodsRepository


class PaymentMethodsService:
    def __init__(self, repository: PaymentMethodsRepository):
        self.repository = repository

    async def get_all(self):
        payment_methods = await self.repository.get_all()

        return (
            None
            if payment_methods is None
            else [
                {
                    "payment_method_id": payment_method.payment_method_id,
                    "user_id": payment_method.user_id,
                    "method_type": payment_method.method_type,
                }
                for payment_method in payment_methods
            ]
        )

    async def get_one(self, payment_method_id: int):
        if not payment_method_id:
            raise ValueError("payment_method_id cannot be empty")

        payment_method = await self.repository.get_one(
            payment_method_id=payment_method_id
        )

        if not payment_method:
            raise ValueError("Payment method not found")

        return {
            "payment_method_id": payment_method.payment_method_id,
            "user_id": payment_method.user_id,
            "method_type": payment_method.method_type,
        }

    async def create(
        self, user_id: int, method_type: str, provider: str, account_number: str
    ):
        if not user_id or not method_type or not provider or not account_number:
            raise ValueError(
                "user_id and method_type and provider and account_number cannot be empty"
            )

        if method_type not in ["Credit Card", "Bank Transfer", "SBP"]:
            raise ValueError("method_type can be Credit Card and Bank Transfer and SBP")

        new_payment_method = await self.repository.create(
            user_id=user_id,
            method_type=method_type,
            provider=provider,
            account_number=account_number,
        )

        return {
            "payment_method_id": new_payment_method.payment_method_id,
            "user_id": new_payment_method.user_id,
            "method_type": new_payment_method.method_type,
            "provider": new_payment_method.provider,
            "account_number": new_payment_method.account_number,
        }

    async def update(
        self,
        payment_method_id: int,
        user_id: int = None,
        method_type: str = None,
        provider: str = None,
        account_number: str = None,
    ):

        if not payment_method_id:
            raise ValueError("payment_method_id cannot be empty")

        if method_type not in ["Credit Card", "Bank Transfer", "SBP"]:
            raise ValueError("method_type can be Credit Card or Bank Transfer or SBP")

        payment_method = await self.repository.update(
            payment_method_id=payment_method_id,
            user_id=user_id,
            method_type=method_type,
            provider=provider,
            account_number=account_number,
        )

        if not payment_method:
            raise ValueError("Payment method not found")

        return {
            "payment_method_id": payment_method.payment_method_id,
            "user_id": payment_method.user_id,
            "method_type": payment_method.method_type,
        }

    async def delete(self, payment_method_id: int):
        if not payment_method_id:
            raise ValueError("payment_method_id cannot be empty")

        if not (
            delete_payment_method := await self.repository.delete(
                payment_method_id=payment_method_id
            )
        ):
            raise ValueError("Payment method not found")
        return delete_payment_method
