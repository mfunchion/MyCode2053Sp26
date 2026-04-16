from bank_account import BankAccount

account1 = BankAccount("123454", 10000)
print(account1)

account1.deposit(5000)
print(account1)

account2 = BankAccount("24680", 10000)
account2.deposit(200)
print(account2)
account2.withdraw(1000)
print(account2)
value = account2.get_balance()
print(value)