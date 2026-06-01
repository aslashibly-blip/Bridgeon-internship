class InsufficientFundsError:
    pass
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.history=[]
    def deposite(self,amount):
        self.balance+= amount
        self.history.append(f"deposite{amount}")
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientError("Insufficient balance")
        self.balance-=amount
        self.history.append(f"withdrawn{amount}")
    def get_balance(self):
        return self.balance
    def transaction_history(self):
        for transaction in self.history:
            print(transaction)
    def __str__(self):
        return(f"owner:{self.owner},balance:{self.balance}")
class SavingAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super() .__init__(owner,balance)
        self.interest_rate=interest_rate
    def apply_interest(self):
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
        self.history.append(f"interest Added:{interest}")
class CurrentAccount(BankAccount):
    def __init__(self, owner, balance,overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit=overdraft_limit
    def withdraw(self,amount):
        if self.balance-amount<-self.overdraft_limit:
            raise InsufficientFundsError("overdraft limit exceeded")
        self.balance-=amount
        self.history.append(f"withdrawn{amount}")
print("bankaccount")
acc=BankAccount("raju",10000)
acc.deposite(5000)
acc.withdraw(100)
print(100)
print("balance:",acc.get_balance())
print("\n transaction_history")
acc.transaction_history()

print("\n SavingAccount ")
sav=SavingAccount("arjun",50000,4)

print("before interest")
sav.get_balance()
sav.apply_interest()
print("After interest",sav.get_balance())
print("\n transaction_history")
sav.transaction_history()

print("CurrentAccount")
cur=CurrentAccount("sara",500000,5000)
cur.withdraw(4000)
print(cur)
print("balance:",cur.get_balance())

print("\n transaction_history")
cur.transaction_history()

print("\n Error test ")

try:
    acc.withdraw(7000)
except InsufficientFundsError as e:
    print("error:",e)
try:
    acc.withdraw(1000)
except InsufficientFundsError as e:
    print("error:",e)