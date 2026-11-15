class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited ${amount}. new balance is ${self.balance}.")
        else:
            print("Invalid deposit amount!")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remining balance is ${self.balance}.")
        else:
            print("Insufficient funds or invalid amount!")
    def display_balance(self):
        print(f"Account Holder: {self.account_holder} | Current Balance: ${self.balance}")
my_account = BankAccount("azan", 1000)
my_account.display_balance()
my_account.deposit(500)
my_account.withdraw(300)
my_account.display_balance()