from typing import Optional
import asyncpg

from internal.domain.repositories.orders import OrdersRepository
from internal.domain.entities.order import Order

class PostgresOrdersRepository(OrdersRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    async def _get_connection(self):
        return await asyncpg.connect(self.connection_string)

    async def create(self, order: Order) -> None:
        query = """
        INSERT INTO orders (order_id, yookassa_id, amount, description, is_paid, payment_method_id)
        VALUES ($1, $2, $3, $4, $5, $6)
        """
        conn = await self._get_connection()
        try:
            await conn.execute(query, order.order_id, order.yookassa_id, order.amount, order.description, order.is_paid, order.payment_method_id)
        finally:
            await conn.close()

    async def get(self, order_id: str) -> Optional[Order]:
        query = """
        SELECT id, order_id, yookassa_id, amount, description, is_paid, payment_method_id
        FROM orders
        WHERE order_id = $1
        """
        conn = await self._get_connection()
        try:
            row = await conn.fetchrow(query, order_id)
            if row:
                return Order(
                    uid=row['id'],
                    order_id=row['order_id'],
                    yookassa_id=row['yookassa_id'],
                    amount=row['amount'],
                    description=row['description'],
                    is_paid=row['is_paid'],
                    payment_method_id=row['payment_method_id']
                )
            return None
        finally:
            await conn.close()

    async def mark_as_paid(self, order_id: str, payment_method_id: str) -> None:
        query = """
        UPDATE orders
        SET is_paid = TRUE, payment_method_id = $1
        WHERE order_id = $2
        """
        conn = await self._get_connection()
        try:
            await conn.execute(query, payment_method_id, order_id)
        finally:
            await conn.close()