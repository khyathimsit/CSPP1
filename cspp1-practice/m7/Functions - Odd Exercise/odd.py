# Author : Khyathi
# Date : 6-8-2018

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

    return x%2 != 0
    

def main():
    data = input()
    print(odd(int(data)))

if __name__== "__main__":
    main()
