class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        balance = self.balance
        if amount <= balance:
            self.balance -= amount
            print(f'Withdraw accepted {self.owner} have {self.balance}')
        else:
            print(f'Funds Unavailable! {self.owner} have {self.balance}')

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit Accepted! {self.owner} have {self.balance}')

    def __str__(self):
        return f'''Account Owner: {self.owner}
Account balance: {self.balance}'''


acct1 = Account('Jose', 100)
acct2 = Account('Martin', 200)

print(acct1.owner)
print(acct1.balance)
print(acct2)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
acct2.deposit(600)

