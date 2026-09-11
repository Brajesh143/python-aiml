class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                raise InsufficientBalanceError("Insufficient funds for withdrawal.")
        else:
            raise ValueError("Withdrawal amount must be greater than zero.")

    def get_balance(self):
        return self.balance

account = BankAccount("ACC101", "John", 50000)

account.deposit(10000)


print(account.get_balance())

class InsufficientBalanceError(Exception):
    pass

try:
    account.withdraw(170000)
except InsufficientBalanceError as e:
    print(f"Error: {e}")