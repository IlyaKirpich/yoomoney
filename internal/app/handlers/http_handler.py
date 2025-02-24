from fastapi import APIRouter

from internal.domain.api.requests import CreatePaymentRequest
from internal.domain.api.responses import CreatePaymentResponse, CheckPaymentResponse

from internal.app.usecases.payments import PaymentUseCase

class HTTPHandler:
    def __init__(self, use_case: PaymentUseCase):
        self.__use_case = use_case
        self.router = APIRouter()
        self.router.add_api_route('/api/create', self.create_payment, methods=['POST'])
        self.router.add_api_route('/api/check', self.check_payment, methods=['GET'])
        self.router.add_api_route('/api/refund', self.refund_payment, methods=['POST'])

    async def create_payment(self, req: CreatePaymentRequest):
        return CreatePaymentResponse(link=await self.__use_case.create_payment(req.amount, req.description))
    
    async def check_payment(self, order_id: str):
        is_paid, payment_link = await self.__use_case.check_payment(order_id)
        return CheckPaymentResponse(is_paid=is_paid, payment_link=payment_link)
    
    async def refund_payment(self, order_id: str):
        return {'status': await self.__use_case.refund_payment(order_id)}