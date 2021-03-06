'''
Author:Khyathi
Created on 06-08-2018
'''
def paying_debt_off_in_a_year(balance, annual_interest_rate, monthly_payment_rate):
    '''
        This code is to calculate the credit card balance after one year if a person only
        pays the minimum monthly payment required by the credit card company each month
    '''
    i = 1
    balance_copy = balance
    while i <= 12:
        mir = (annual_interest_rate) / 12.0
        mmp = (monthly_payment_rate)*(balance_copy)
        mub = (balance_copy) - (mmp)
        balance_copy = (mub) + (mir*mub)
        i += 1
    return "Remaining balance: " + str(round(balance_copy, 2))

def main():
    '''
    Main function starts here
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_in_a_year(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()
