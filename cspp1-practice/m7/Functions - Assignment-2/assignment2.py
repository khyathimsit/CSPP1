'''
Author:Khyathi
Created on 06-08-2018

Assignment-2 - Paying Debt off in a Year

This program calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance)+
.                    (Monthly interest rate x Monthly unpaid balance)

'''

def paying_debt_off_in_a_year(initial_balance, annual_interest_rate):
    """
    The monthly payment must be a multiple of $10 and is the same for all
    months

    Notice that it is possible for the balance to become negative using this
    payment scheme, which is okay. A summary of the required math is found
    below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) +
    .                (Monthly interest rate x Monthly unpaid balance)

    """
    monthlyfixedprice = 0
    while True:
        updatedbalancemonth = initial_balance
        for _ in range(12):
            monthlyinterestrate = annual_interest_rate/12.0
            monthlyunpaidbalance = updatedbalancemonth - monthlyfixedprice
            updatedbalancemonth = monthlyunpaidbalance + monthlyinterestrate*monthlyunpaidbalance
        if updatedbalancemonth <= 0:
            break
        monthlyfixedprice += 10
    return "Lowest Payment: "+str(monthlyfixedprice)

def main():
    """
    Program execution starts in the main function...
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_in_a_year(data[0], data[1]))

if __name__ == "__main__":
    main()
 