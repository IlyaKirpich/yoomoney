from abc import ABC, abstractmethod

class YookassaClient(ABC):
    @abstractmethod
    async def create_payment(self, amount: int, order_id: str, description: str):
        pass

    @abstractmethod
    async def check_payment(self, yookassa_id: str, amount: int):
        pass
    
    @abstractmethod
    async def refund_payment(self, yookassa_id: str, amount: int):
        pass
    