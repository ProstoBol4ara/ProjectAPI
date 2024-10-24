from repositories import PaymentMethodsRepository

class PaymentMethodsService:
    def __init__(self, payment_methods_repository: PaymentMethodsRepository):
        self.payment_methods_repository = payment_methods_repository

    async def get_payment_methods(self):
        payment_methods = await self.payment_methods_repository.get_payment_methods()
        return None if payment_methods is None else [{"payment_method_id": payment_method.payment_method_id, "name": payment_method.name, "email": payment_method.email} for payment_method in payment_methods]

    async def get_payment_method(self, payment_method_id: int):
        payment_method = await self.payment_methods_repository.get_payment_method(payment_method_id=payment_method_id)
        return None if payment_method is None else {"payment_method_id": payment_method.payment_method_id, "name": payment_method.name, "email": payment_method.email}

    async def create_payment_method(self, user_id: int, method_type: str, provider: str, account_number: str):
        new_payment_method = await self.payment_methods_repository.create_payment_method(user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
        return {"payment_method_id": new_payment_method.payment_method_id, "name": new_payment_method.name, "email": new_payment_method.email}

    async def update_payment_method(self, payment_method_id: int, user_id: int = None, method_type: str = None, provider: str = None, account_number: str = None):
        payment_method = await self.payment_methods_repository.update_payment_method(payment_method_id=payment_method_id, user_id=user_id, method_type=method_type, provider=provider, account_number=account_number)
        return None if payment_method is None else {"payment_method_id": payment_method.payment_method_id, "name": payment_method.name, "email": payment_method.email}

    async def delete_payment_method(self, payment_method_id: int):
        return await self.payment_methods_repository.delete_payment_method(payment_method_id=payment_method_id)