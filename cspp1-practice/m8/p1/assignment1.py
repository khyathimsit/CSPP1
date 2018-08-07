'''
Author : Khyathi
Date : 7-8-2018
Write a Python function, factorial(n), 
that takes in one number and returns the factorial of given number.
'''
# This function takes in one number and returns one number.


def factorial(num_value):
    '''
    num_value is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if num_value <= 1:
        return 1
    else:
        return num_value * factorial(num_value-1)
def main():
    a = input()
    print(factorial(int(a)))    
if __name__ == "__main__":
    main()
