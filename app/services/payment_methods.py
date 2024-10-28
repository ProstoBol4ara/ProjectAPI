from repositories import PaymentMethodsRepository

class PaymentMethodsService:
    def __init__(self, payment_methods_repository: PaymentMethodsRepository):
        self.payment_methods_repository = payment_methods_repository

    async def get_payment_methods(self):
        payment_methods = await self.payment_methods_repository.get_payment_methods()

        return None if payment_methods is None else \
            [{"payment_method_id": payment_method.payment_method_id, "user_id": payment_method.user_id,
              "method_type": payment_method.method_type} for payment_method in payment_methods]

    async def get_payment_method(self, payment_method_id: int):
        payment_method = await self.payment_methods_repository.get_payment_method(payment_method_id=payment_method_id)

        if not payment_method: raise ValueError("Payment method not found")

        return {"payment_method_id": payment_method.payment_method_id, "user_id": payment_method.user_id,
                "method_type": payment_method.method_type}

    async def create_payment_method(self, user_id: int, method_type: str, provider: str, account_number: str):
        new_payment_method = await self.payment_methods_repository\
            .create_payment_method(user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)

        return {"payment_method_id": new_payment_method.payment_method_id, "user_id": new_payment_method.user_id,
                "method_type": new_payment_method.method_type, "provider": new_payment_method.provider,
                "account_number": new_payment_method.account_number}

    async def update_payment_method(self, payment_method_id: int, user_id: int = None, method_type: str = None,
                                    provider: str = None, account_number: str = None):

        payment_method = await self.payment_methods_repository\
            .update_payment_method(payment_method_id=payment_method_id, user_id=user_id, method_type=method_type,
                                   provider=provider, account_number=account_number)

        if not payment_method: raise ValueError("Payment method not found")

        return {"payment_method_id": payment_method.payment_method_id, "user_id": payment_method.user_id,
                "method_type": payment_method.method_type}

    async def delete_payment_method(self, payment_method_id: int):
        if not await self.payment_methods_repository.delete_payment_method(payment_method_id=payment_method_id):
            raise ValueError("Payment method not found")
