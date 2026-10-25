class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self, amount):
        self.balance += amount
        return amount
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount
    def check_balance(self):
        print(f"Current Balance: Ksh {self.balance}")
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: Ksh {self.balance}")
        
acc1 = BankAccount("ACC1001", 50000, "2024-01-15", "James Kariuki")
print("--- Customer Details ---")
acc1.customer_details()
print()
print(f"Deposited: Ksh {acc1.deposit(10000)}")
acc1.check_balance()
print()
print(f"Withdraw: Ksh {acc1.withdraw(20000)}")
acc1.check_balance()
print()
print(f"Withdraw 100,000: {acc1.withdraw(100000)}")
    
