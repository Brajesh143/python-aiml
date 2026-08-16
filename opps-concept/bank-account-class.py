class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.owner} has ₹{self.balance}")

account1 = BankAccount("Alice", 10000)
account2 = BankAccount("Bob", 20000)

account1.deposit(5000)
account2.deposit(3000)