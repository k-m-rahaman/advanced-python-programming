class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Balance:", self.balance)


name = input("Enter your name: ")
acc = BankAccount(name)

while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        acc.deposit(float(input("Amount: ")))
    elif ch == "2":
        acc.withdraw(float(input("Amount: ")))
    elif ch == "3":
        acc.show_balance()
    else:
        break
