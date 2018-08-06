'''
Author:Khyathi
Created on 06-08-2018

Functions - Assignment-3 - Using Bisection Search to Make the Program Faster

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12)/12.0

Write a program that uses these bounds and bisection search (for more info
check out the Wikipedia page on bisection search) to find the smallest monthly
payment to the cent (no more multiples of $10) such that we can pay off the
debt within a year. Try it out with large inputs, and notice how fast it is
(try the same large inputs in your solution to Problem 2 to compare!).
Produce the same return
value as you did in Assignment 2.
'''

def paying_debt_off_in_a_year(initial_balance, annual_interest_rate):
    '''
    operation
    '''
     epsilon_val = 0.05
     upper_bound = initial_balance*((1+annual_interest_rate/12.0)**12)/12.0
     mfp = 0
    lower_bound = initial_balance/12.0
    # print(lower_bound,upper_bound)
    mir = annual_interest_rate/12.0
    while True:
        # print(mfp)
        ubm = initial_balance
        mfp = (lower_bound+upper_bound)/2.0
        # mfp = int(mfp*100)/100.0
        for _ in range(12):
            mub = ubm - mfp
            ubm = mub + mir*mub
        if ubm > epsilon_val:
            lower_bound = mfp
        elif ubm < -epsilon_val:
            upper_bound = mfp
        else:
            break
    # mfp = int(mfp*100)/100.0
    return "Lowest Payment: "+str(mfp)

def main():
    '''
    main functiion
    '''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_in_a_year(data[0], data[1]))

if __name__ == "__main__":
    main()
