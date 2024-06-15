class User:
    def __init__(self, user_id, name, phone_number, email, password):
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.bank_accounts = []

    def update_profile(self, name=None, email=None, phone_number=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone_number:
            self.phone_number = phone_number

    def add_bank_account(self, bank_account):
        self.bank_accounts.append(bank_account)
