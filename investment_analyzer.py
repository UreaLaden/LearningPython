from itertools import accumulate,cycle
from delete_line import delete_last_line

class Investment:

    account_balance = 0
    active_investments = 0
    
    @classmethod
    def get_account_balance(cls):
        return f'$ {round(Investment.account_balance,2)}'

    def __init__(self,interest_rate,term,balance=0):
        self.interest_rate = interest_rate
        self.term = term 
        self.balance = balance
        Investment.active_investments += 1

    def current_balance(self):
        monthly_interest = self.balance * ((self.interest_rate / 100) / 12)
        return f'''===========================================\nBalance: $ {round(self.balance + monthly_interest,2)} 
        \nInterest Rate: {self.interest_rate}% 
        \nTerm: {self.term} Years / {self.term * 12} Months\n==========================================='''

    def deposit(self,deposit_amount):
            self.deposit_amount = deposit_amount
            self.balance += deposit_amount + self.balance * ((self.interest_rate / 100) / 12)
            Investment.account_balance += deposit_amount + self.balance * ((self.interest_rate / 100) / 12)
            return f'\nDeposit Amount: ${round(deposit_amount, 2)} \n{self.current_balance()}\n'    

    def project_earnings(self,deposit_frequency,deposit_amount):
        balance = self.balance
        term = self.term
        interest_rate = self.interest_rate

        def accumulate_earnings():
            deposits = [balance]
            balanceCycle = cycle(deposits)
            
            for _ in range((term)):
                num = next(balanceCycle)
                deposits.append(num)
            
            running_totals = list(accumulate(deposits,lambda bal,deposit:round(bal*(interest_rate / 100) + (bal + deposit_frequency), 2)))
            return running_totals[len(running_totals) - 1]
        
        def increment_earnings():
            running_total = [self.balance]
            for i in range(1,(self.term * 12) * deposit_frequency):
                running_total.append(i / i)
            new_total = (list(accumulate(running_total,lambda balance,deposit: balance * ((self.interest_rate / 100) / 12 + 1 )+ deposit_amount )))
            return round(new_total[-1],2)
        
        if deposit_frequency == 0:
            earnings = accumulate_earnings()
        else:
            earnings = increment_earnings()
        
        return(f'''===========================================\nStarting Balance: $ {round(self.balance,2)}
        \nInterest Rate: {self.interest_rate}% / {(self.interest_rate / 100)}
        \n({deposit_frequency}) Continued Monthly Deposits over {self.term} Years / {self.term * 12} Months: $ {deposit_amount}
        \nProjected Balance: $ {round(earnings, 2)}
        \nTotal Interest Earned: $ {round(earnings * ((self.interest_rate / 100) )  ,2)}\n===========================================''')

def add_investment(title):
            assets = {}
            assets['interest'] = float(input('Interest Rate: '))
            delete_last_line()
            assets['term'] = int(input('Investment Term: '))
            delete_last_line()
            assets['balance'] = int(input('Starting Deposit (Enter 0 if none): '))
            delete_last_line()
            
            interest =  assets['interest']
            term = assets['term']
            balance = assets['balance']
            title = Investment(interest,term,balance)
            return title

