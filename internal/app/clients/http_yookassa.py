import uuid
from pydantic import SecretStr
from httpx import AsyncClient

from internal.domain.clients.yookassa import YookassaClient


class HTTPYookassaClient(YookassaClient):
    def __init__(self, base_url: str, shop_id: str, secret_key: SecretStr):
        self.__yookassa = AsyncClient(base_url=base_url, auth=(shop_id, secret_key.get_secret_value()))

    async def create_payment(self, amount: int, order_id: str, description: str):
        return await self.__yookassa.post(
        "/payments",
        json={
            "amount": {
                "value": amount,
                "currency": "RUB",
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "http://localhost:8000/api/check?order_id=" + order_id,
            },
            "save_payment_method": True,
            "capture": True,
            "description": description,
        },
        headers={"Idempotence-Key": order_id},
    )

    async def check_payment(self, yookassa_id: str, amount: int):
        return await self.__yookassa.get(
            f"/payments/{yookassa_id}"
        )
    
    async def refund_payment(self, yookassa_id: str, amount: int):
        refund_info = await self.__yookassa.post(
                "/refunds",
                json={
                    "payment_id": yookassa_id,
                    "amount": {
                        "value": amount,
                        "currency": "RUB",
                    },
                },
                headers={"Idempotence-Key": str(uuid.uuid4())},
            )
        return refund_info.json()["status"] == "succeeded"