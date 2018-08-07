'''
Author : Khyathi
Date : 7-8-2018
'''
# This function takes in one number and returns one number.

def sumofdigits(n_val):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_val == 0:
        return n_val
    return (n_val%10) + sumofdigits(n_val//10)
def main():
    ''' main function'''
    a_1 = input()
    print(sumofdigits(int(a_1)))
if __name__ == "__main__":
    main()
