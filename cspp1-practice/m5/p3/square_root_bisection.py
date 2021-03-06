'''
Author : Khyathi
Date : 3-8-18
'''

def main():
    ''' This is code is used to find the square root of a number using bisection method'''
    x_1 = input()
    epsilon = 0.01
    #step = 0.1
    num_guesses = 0
    low = 0.0
    high = int(x_1)
    an_s = (high + low)/2
    while abs(an_s**2 - int(x_1)) >= epsilon:
        num_guesses += 1
        if an_s**2 < int(x_1):
            low = an_s
        else:
            high = an_s
        an_s = (high + low)/2.0
    print(str(an_s))
if __name__ == "__main__":
    main()
