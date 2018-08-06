'''
Author : Khyathi
Date : 6-8-18
'''
def square(x):
    '''
    x: int or float.
    This program is used to find the square of a number.
    '''
    return x**2

def main():
	data = input()
	data = float(data)
	temp = str(data).split('.')
	if(temp[1] == '0'):
		print(square(int(float(str(data)))))
	else:
		print(square(data))

if __name__== "__main__":
	main()

