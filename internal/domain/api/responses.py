from pydantic import BaseModel

class CreatePaymentResponse(BaseModel):  
    link: str

class CheckPaymentResponse(BaseModel):  
    is_paid: bool
    payment_link: str