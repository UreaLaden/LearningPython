from investment_analyzer import Investment, add_investment
from loan_analyzer import Liability,add_debt
from delete_line import delete_last_line
import keyboard,sys

def financial_advisor():
    res = input('Do you need help with an [A]Asset or a [B]Liability (Enter [Q] to exit)?  ')
    delete_last_line()
    # assets = {}
    # liabilities = {}
    if res.title() == 'A':
        title = input('Give your investment a title (No Spaces): ')
        delete_last_line()
        asset = add_investment(title)

        def choose_service():
            query = input('Please Choose an Option: (Add Funds, Check Balance, Project Earnings, or Quit): ')
       
            if query.title() == 'Check Balance':
                print(asset.current_balance())
                choose_service()
                delete_last_line()
            elif query.title() == 'Project Earnings':
                deposit_frequency = int(input('How many times per month will you make deposits? '))
                delete_last_line()
                deposit_amount = int(input('How much will you deposit? '))
                delete_last_line()
                print(asset.project_earnings(deposit_frequency,deposit_amount))
                delete_last_line()
                choose_service()
                delete_last_line()
            elif query.title() == 'Quit':
                print('Let me know if I can be of further assistance')
                delete_last_line()
                financial_advisor()
            elif query.title() == 'Add Funds':
                amount = int(input('How much would you like to deposit? '))
                asset.deposit(amount)
                choose_service()
            else:
                print('That is not a valid response. Please try again')
                delete_last_line()
                choose_service()
        
        choose_service()

    elif res.title() == 'B':
        title = input('Give your debt a title: ')
        delete_last_line()

        debt = add_debt(title)

        def choose_option():
            res = input('Please choose an option ([A]Payment Assessment , [B]Recommend Payment, [Q]Exit) :')
            if res.title() == 'A':
                print(debt.payment_status())
                choose_option()
            elif res.title() == 'B':
                print(debt.recommend_payment())
                choose_option()
            elif res.title() == 'Q' :
                print('Please let us know if we can assist you in the future.')
                financial_advisor()
            else:
                print('That is not a valid response. please try again.')
                delete_last_line()
                choose_option()
        choose_option()

    elif res.title() == 'Q':
        print('Goodbye')
        sys.exit()
    else:
        print('Not a valid response')
        financial_advisor()
        delete_last_line()

financial_advisor()