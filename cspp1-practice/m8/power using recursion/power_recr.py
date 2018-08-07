'''
Author : Khyathi
Date : 7-8-18
'''
# Write a Python function, recurPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    if exp == 1:
    	return base
    else:
    	while exp>1:
    		result *= base
    		exp -= 1
    	return result

def main():
    data = input()
    data = data.split()
    print(recurPower(float(data[0]),int(data[1])))   

if __name__ == "__main__":
    main()