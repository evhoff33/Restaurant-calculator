from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('Checking')
        self.a2 = Account('Savings')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_balance() == 0
        assert self.a1.get_name() == 'Checking'
        assert self.a2.get_balance() == 0
        assert self.a2.get_name() == 'Savings'

    def test_deposit(self):
        assert self.a1.deposit(30) is True
        assert self.a1.get_balance() == 30

        assert self.a1.deposit(-30) is False
        assert self.a1.get_balance() == 30

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 30


    def test_withdraw(self):
        self.a2.deposit(30)
        assert self.a2.withdraw(25) is True
        assert self.a2.get_balance() == 5

        assert self.a2.withdraw(-20) is False
        assert self.a2.get_balance() == 5

        assert self.a2.withdraw(0) is False
        assert self.a2.get_balance() == 5

        assert self.a2.withdraw(7.2) is False
        assert self.a2.get_balance() == 5



