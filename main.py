from app.payment_app import PaymentApp
from app.transaction import TransactionType, PaymentMode

# Example usage
app = PaymentApp()
user_id = app.register_user("1234567890", "password")
app.update_user(user_id, "John Doe", "john@example.com", "1234567890")
transaction_id = app.create_transaction(TransactionType.USER_TO_USER, user_id, "9876543210", 100)
app.make_payment(transaction_id, PaymentMode.UPI, {})
app.view_transaction_history(user_id)
