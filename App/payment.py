from enum import Enum
from datetime import datetime

class PaymentMode(Enum):
    UPI = 1
    CREDIT_CARD = 2
    DEBIT_CARD = 3
    NET_BANKING = 4

class PaymentStatus(Enum):
    SUCCESS = 1
    FAILURE = 2
    PENDING = 3

class Payment:
    def __init__(self, payment_id, amount, mode):
        self.payment_id = payment_id
        self.amount = amount
        self.mode = mode
        self.status = PaymentStatus.PENDING
        self.timestamp = datetime.now()

    def complete_payment(self):
        self.status = PaymentStatus.SUCCESS
