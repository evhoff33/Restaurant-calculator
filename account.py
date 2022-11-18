class Account:
    def __init__(self, name):
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        elif amount <= 0:
            return False

    def withdraw(self, amount):
        if amount <= 0:
            return False
        elif amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True


    def get_balance(self):
        return f'{self.account_balance}'



    def get_name(self):
        return f'{self.account_name}'
    

