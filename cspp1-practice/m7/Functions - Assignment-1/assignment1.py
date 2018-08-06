'''
Author:Khyathi
Created on 06-08-2018
'''
def payingDebt_offinayear(balance, annual_interestRate, monthly_paymentRate):
    '''
        This code is to calculate the credit card balance after one year if a person only
        pays the minimum monthly payment required by the credit card company each month
    '''
    i = 1
    balance_copy = balance
    
    while i <= 12:
        mir = (annual_interestRate) / 12.0
        mmp = (monthly_paymentRate)*(balance_copy)
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
    print(payingDebt_offinayear(data[0],data[1],data[2]))

if __name__ == "__main__":
    main()
