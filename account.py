class Account:
    """
    A class representing a bank account with a user
    picked name and a default balance of 0. Includes
    methods to deposit and withdraw money, incrementing the
    account balance accordingly. Also has methods to retrieve
    and check the balance along with getting the account name.
    """

    def __init__(self, name: str):
        """
        Constructor to create initial state of an account object.
        :param name: Name of the account.
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float):
        """
        Method to deposit money into the account incrementing the account balance variable.
        :param amount: Amount to deposit.
        :return: Whether the deposit was successful.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        elif amount <= 0:
            return False

    def withdraw(self, amount: float):
        """
        Method to withdraw money from the account incrementing the account balance variable.
        :param amount: Amount to withdraw.
        :return: Whether the withdrawal was successful.
        """
        if amount <= 0:
            return False
        elif amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True


    def get_balance(self):
        """
        Method to retrieve the account balance value.
        :return: The variable account_balance.
        """
        return self.account_balance


    def get_name(self):
        """
        Method to retrieve the name of the account.
        :return: The variable account_name.
        """
        return self.account_name
    

