import math

initial_balance = 0
transactions = []

def deposit(amount):
    global initial_balance
    initial_balance += amount
    transactions.append(("Deposit", amount))

def withdraw(amount):
    global initial_balance
    if amount > initial_balance:
        print("Insufficient funds. Cannot withdraw.")
        return

    tax = 0
    if initial_balance >= 5000000:
        tax = math.ceil(amount * 0.1)
        initial_balance -= tax

    fee = max(30, min(0.015 * amount, 600))
    total_withdrawal = amount + fee

    initial_balance -= total_withdrawal
    transactions.append(("Withdrawal", amount))

def print_balance():
    global initial_balance
    print(f"Current balance: {initial_balance} u.e.")

def print_transactions():
    print("Transaction history:")
    for transaction in transactions:
        action, amount = transaction
        print(f"{action}: {amount} u.e.")

def atm():
    while True:
        print("\nATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Print balance")
        print("4. Print transaction history")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = int(input("Enter the amount to deposit (must be a multiple of 50): "))
            if amount % 50 != 0:
                print("Invalid amount. Amount must be a multiple of 50.")
                continue
            deposit(amount)
            print(f"Amount deposited: {amount}")
            print_balance()
        elif choice == "2":
            amount = int(input("Enter the amount to withdraw (must be a multiple of 50): "))
            if amount % 50 != 0:
                print("Invalid amount. Amount must be a multiple of 50.")
                continue
            withdraw(amount)
            print(f"Amount withdrawn: {amount}")
            print_balance()
        elif choice == "3":
            print_balance()
        elif choice == "4":
            print_transactions()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

atm()