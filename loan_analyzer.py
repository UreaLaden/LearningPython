from itertools import accumulate,cycle

class Liability:

    def __init__(self,balance,interest_rate,min_payment):
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_payment = min_payment

    def payment_status(self):
        monthly_interest = ((self.interest_rate / 100) / 12) * self.balance
        result = self.min_payment - monthly_interest
        months_until_paid = self.balance * (((self.interest_rate /100)/12) + 1) / self.min_payment
        total_interest_paid = monthly_interest * months_until_paid
        
        if result < 0:
            return f"""================================
            \nThe current payment is $ {self.min_payment} with a monthly interest of $ {monthly_interest}. 
            \nTotal Interest Paid: $ {round(total_interest_paid)}
            \nBy maintaining the current payment plan, the balance will increase from $ {self.balance} to {self.balance - result}
            \n=========================================="""
        else:
            return f"""================================
            \nThe current payment is $ {self.min_payment} with a monthly interest of $ {monthly_interest}. 
            \nTotal Interest Paid: $ {round(total_interest_paid)}
            \nBy maintaining the current payment plan, the debt will be fullfilled in {round(months_until_paid)} months
            \n================================"""
    
    def recommend_payment(self):
        time = int(input('Tell me in years when you intend to fulfill this debt: '))
        min_required_payment = ((self.balance / (time * 12)) * ((self.interest_rate / 100) + 1)) 
        needed_payment = min_required_payment * 1.31
        payment_counter = [((i / -i) * needed_payment) for i in range(1,time * 12 )]
        payment_counter.insert(0,self.balance)
        running_balance = list(accumulate(payment_counter,lambda bal,payment:round(bal * ((self.interest_rate / 100) / 12 + 1) + payment)))
        accumulated_interest = sum([round(i * (((self.interest_rate) / 100) / 12),2) for i in running_balance])
        return f'''\n========================\n========================\nMonthly Payment Recommended: ${round(needed_payment)}
        \nTotal Interest paid: $ {round(accumulated_interest)}
        \nPayment breakdown with {self.interest_rate}% interest included over {len(running_balance)} monthly payments: 
        \n*********************\n{running_balance}\n*********************\n========================\n========================\n'''

def add_debt(name):
    debts = {}

    debts['balance'] = int(input('What is your account balance? '))
    debts['interest'] = int(input('What is your interest rate? '))
    debts['min_payment'] = int(input('What is your minimum payment? '))

    balance = debts['balance']
    interest = debts['interest']
    min_payment = debts['min_payment']

    debt = Liability(balance,interest,min_payment)
    return debt
