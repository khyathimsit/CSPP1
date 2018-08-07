'''
Author : Khyathi
Date : 7-8-2018
'''
# This function takes in one number and returns one number.


def factorial(num_value):
    '''
    num_value is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if num_value <= 1:
        return 1
    return num_value * factorial(num_value-1)
def main():
    '''main function'''
    a_1 = input()
    print(factorial(int(a_1)))    
if __name__ == "__main__":
    main()
