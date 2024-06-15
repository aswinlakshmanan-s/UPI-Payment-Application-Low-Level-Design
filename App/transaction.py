from enum import Enum
from datetime import datetime

class TransactionType(Enum):
    USER_TO_USER = 1
    USER_TO_MERCHANT = 2
    USER_TO_BANK_ACCOUNT = 3

class TransactionStatus(Enum):
    SUCCESS = 1
    FAILURE = 2
    PENDING = 3

class Transaction:
    def __init__(self, transaction_id, amount, sender, receiver, transaction_type):
        self.transaction_id = transaction_id
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.transaction_type = transaction_type
        self.status = TransactionStatus.PENDING
        self.timestamp = datetime.now()
        self.payments = []

    def add_payment(self, payment):
        self.payments.append(payment)
        self.status = TransactionStatus.SUCCESS
