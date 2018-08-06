'''
Author : Khyathi
Date  : 6-8-2018
'''
def square(x):
    '''
    x: int or float.
    This code is used to find the square of the given number..
    '''
    return x**2


def fourthPower(x):
    '''
    x: int or float.
    This function is used to find the fourth power of a nnumber using the above function.
    '''
    return square(square(x))

def main():
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if(temp[1] == '0'):
        print(fourthPower(int(float(str(data)))))
    else:
        print(fourthPower(data))

if __name__ == "__main__":
    main()
