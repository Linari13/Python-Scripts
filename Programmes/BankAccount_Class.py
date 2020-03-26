class Account:
    
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'deposit of {amount} accepted.\nYour balance is: {self.balance}')
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
            print(f'Withdrawal Accepted.\nYour balance is: €{self.balance}')
        else:
            print('Funds Unavailable')