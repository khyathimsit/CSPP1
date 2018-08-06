'''
Author:Khyathi
Created on 06-08-2018
'''
'''This code is to calculate the credit card balance after one year if a person only
pays the minimum monthly payment required by the credit card company each month'''

def payingDebt_OffInAYear(balance, annual_InterestRate, monthly_PaymentRate):
    i = 1
    '''
        The following variables contain values as described below:
        # balance - the outstanding balance on the credit card
        # annualInterestRate - annual interest rate as a decimal
        # monthlyPaymentRate - minimum monthly payment rate as a decimal
    '''
    balance_copy = balance
    while i <= 12:
        mir = (annual_InterestRate) / 12.0
        mmp = (monthly_PaymentRate)*(balance_copy)
        mub = (balance_copy) - (mmp)
        balance_copy = (mub) + (mir*mub)
        i += 1
    return "Remaining balance: " + str(round(balance_copy, 2))

def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebt_OffInAYear(data[0],data[1],data[2]))

if __name__ == "__main__":
    main()
