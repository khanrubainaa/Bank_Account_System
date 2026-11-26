class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Please enter a valid amount.")

        self.show_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount > self.balance:
            print("Insufficient balance! Withdrawal refused.")

        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")

        self.show_balance()

    def show_balance(self):
        print(f"{self.account_holder}'s balance: ₹{self.balance}")

account1 = BankAccount("Rahul")
account2 = BankAccount("Priya")

print("\n===== RAHUL'S ACCOUNT =====")

account1.deposit(5000)
account1.withdraw(1500)
account1.deposit(2000)

print("\n===== PRIYA'S ACCOUNT =====")

account2.deposit(3000)
account2.withdraw(1000)
account2.withdraw(5000)