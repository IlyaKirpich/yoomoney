from pydantic import BaseModel

class CreatePaymentRequest(BaseModel):  
    amount: int
    description: str

class CheckPaymentRequest(BaseModel):  
    order_id: str