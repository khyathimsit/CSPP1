'''
Author : Khyathi
Date : 3-8-18
'''

def main():
	''' This is code is used to find the square root of a number using bisection method'''
	x_1 = input()
	epsilon = 0.01
	#step = 0.1
	numGuesses = 0
    low = 0.0
    high = int(x_1)
    ans = (high + low)/2.0
    while abs(ans**2 - int(x_1)) >= epsilon:
        numGuesses += 1
        if ans**2 < int(x_1):
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
print(str(ans))
if __name__== "__main__":
	main()
