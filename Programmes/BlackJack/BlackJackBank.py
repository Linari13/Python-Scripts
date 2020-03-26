class BlackJackBank:
    ''' fonction relatives à la banque du jeu'''

    def __init__(self, balance):
            """Assigments"""
            self.balance=balance
    
    def payoff(self,amount):
        ''' fonction affichage balance enfonction des pertes/gains'''
        self.balance = self.balance + amount
        print (f'Your balance is {self.balance}€')
            
    def ask_amount(self):
        """Ask an amount until user enters an integer"""
        print (f'Your balance is {self.balance}€')
        
        if self.balance == 0:
            """ End of Game if no funds"""
            print ('You\'re broke, end of the game ! ')
        else:
            """Error Managment"""
            while True:                
                try:
                    amount = int(input('How much would you like to bet? '))
                    
                    """Check if funds available in loop"""
                    while amount > self.balance:
                        amount = int(input('Funds Unavailable, enter an more reasonable amount : '))
                except:
                    """Error Message -> Send back to loop"""
                    print ('Please Enter an integer !')
                    continue
                else:
                    """Bet accepted set acount balance accordingly + return bet amount"""
                    self.balance = self.balance-amount
                    print(f'Bet Accepted.\nYour balance is: €{self.balance}')
                    return amount
                    break