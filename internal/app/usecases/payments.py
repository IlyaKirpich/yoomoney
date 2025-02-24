import uuid
from internal.domain.repositories.orders import OrdersRepository
from internal.domain.clients.yookassa import YookassaClient
from internal.domain.entities.order import Order

class PaymentUseCase:
    def __init__(self, orders_repository: OrdersRepository, yookassa_client: YookassaClient):
        self.__orders: OrdersRepository = orders_repository
        self.__yookassa: YookassaClient = yookassa_client
    
    async def create_payment(self, amount: int, description: str):
        order = Order(
            uid=1,
            order_id=str(uuid.uuid4()),
            amount=amount,
            description=description,
            yookassa_id='',
            is_paid=False,
            payment_method_id='',
        )

        info = await self.__yookassa.create_payment(amount, order.order_id, description)
        order.yookassa_id = info.json()["id"]
        await self.__orders.create(order)

        return info.json()["confirmation"]["confirmation_url"]
    
    async def check_payment(self, order_id: str):
        order = await self.__orders.get(order_id)

        if order is None:
            return False, None
        
        payment_link = "https://yoomoney.ru/checkout/payments/v2/contract?orderId=" + order.yookassa_id

        if order.is_paid:
            return True, payment_link
        
        info = await self.__yookassa.check_payment(order.yookassa_id, order.amount)
        is_paid = info.json()["status"] == "succeeded"

        if is_paid:
            await self.__orders.mark_as_paid(order_id, info.json()["payment_method"]["id"])
        
        return is_paid, payment_link

    async def refund_payment(self, order_id: str):
        order = await self.__orders.get(order_id)

        if order is None:
            return False

        succeeded = await self.__yookassa.refund_payment(order.yookassa_id, order.amount)

        if succeeded:
            await self.__orders.mark_as_paid(order_id, 'refunded')

        return succeeded

