from abc import ABC, abstractmethod

from internal.domain.entities.order import Order

class OrdersRepository(ABC):
    @abstractmethod
    async def create(self, order: Order):
        pass
    
    @abstractmethod
    async def get(self, order_id: str):
        pass

    @abstractmethod
    async def mark_as_paid(self, order_id: str, payment_method_id: str) -> None:
        pass

