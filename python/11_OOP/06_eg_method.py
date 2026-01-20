class Bank:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, am):
        self.balance = self.balance - am
        print(f"{am} debited")

    def credit(self, am):
        self.balance = self.balance + am
        print(f"{am} credited")

    def show_balance(self):
        print(f"Balance: {self.balance}")

p1 = Bank(100000, 123)
p1.show_balance()
p1.debit(5000)
p1.show_balance()
p1.credit(20000)
p1.show_balance()
