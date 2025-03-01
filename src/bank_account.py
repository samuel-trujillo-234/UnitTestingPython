class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amonut):
        if amonut > 0:
            self.balance += amonut

    def withdraw(self, amonut):
        if amonut > 0:
            self.balance -= amonut
        return self.balance

    def get_balance(self):
        return self.balance