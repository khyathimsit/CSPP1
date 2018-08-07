'''
Author : Khyathi
Date : 7-8-2018
Write a Python function, factorial(n), 
that takes in one number and returns the factorial of given number.
'''
# This function takes in one number and returns one number.


def factorial(num_value):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if num_value <= 1:
        return 1
    else:
        return num_value*factorial(num_value-1)
    def main():
    a_number = input()
    print(factorial(int(a_number)))    
if __name__ == "__main__":
    main()
