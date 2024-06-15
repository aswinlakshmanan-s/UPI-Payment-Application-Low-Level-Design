import uuid
from app.user.py import User
from app.transaction.py import Transaction, TransactionType, TransactionStatus
from app.payment.py import Payment, PaymentMode

class PaymentApp:
    def __init__(self):
        self.users = {}
        self.transactions = {}
        self.payments = {}

    def register_user(self, phone_number, password):
        user_id = str(uuid.uuid4())
        new_user = User(user_id, "", phone_number, "", password)
        self.users[user_id] = new_user
        return user_id

    def update_user(self, user_id, name, email, phone_number):
        if user_id in self.users:
            self.users[user_id].update_profile(name, email, phone_number)
        else:
            print(f"User with id {user_id} not found")

    def create_transaction(self, transaction_type, from_user_id, to_user, amount):
        transaction_id = str(uuid.uuid4())
        new_transaction = Transaction(transaction_id, amount, from_user_id, to_user, transaction_type)
        self.transactions[transaction_id] = new_transaction
        return transaction_id

    def make_payment(self, transaction_id, payment_method, details):
        if transaction_id in self.transactions:
            transaction = self.transactions[transaction_id]
            payment_id = str(uuid.uuid4())
            new_payment = Payment(payment_id, transaction.amount, payment_method)
            self.payments[payment_id] = new_payment
            transaction.add_payment(new_payment)
            new_payment.complete_payment()
        else:
            print(f"Transaction with id {transaction_id} not found")

    def refund_transaction(self, transaction_id):
        if transaction_id in self.transactions:
            transaction = self.transactions[transaction_id]
            if transaction.status == TransactionStatus.SUCCESS:
                transaction.status = TransactionStatus.PENDING
                print(f"Transaction {transaction_id} has been refunded")
            else:
                print(f"Transaction {transaction_id} is not successful, cannot refund")
        else:
            print(f"Transaction with id {transaction_id} not found")

    def view_transaction_history(self, user_id):
        user_transactions = [t for t in self.transactions.values() if t.sender == user_id or t.receiver == user_id]
        for transaction in user_transactions:
            print(f"Transaction ID: {transaction.transaction_id}, Amount: {transaction.amount}, Status: {transaction.status.name}, Timestamp: {transaction.timestamp}")
