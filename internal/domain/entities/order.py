class Order:
    def __init__(self, uid: int, order_id: str, yookassa_id: str, amount: int, description: str, is_paid: bool, payment_method_id: str):
        self.id = uid
        self.order_id = order_id
        self.yookassa_id = yookassa_id
        self.amount = amount
        self.description = description
        self.is_paid = is_paid
        self.payment_method_id = payment_method_id