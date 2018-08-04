'''
Author: Khyathi
Date : 4- 8- 18
'''
def main():
    '''
    This program is to print n numbers with fizz and buzz
    '''
    num = int(input())
    for i in range(1, num+1, 1):
        if i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0 and i%5 == 0:
            print("Fizz")
            print("Buzz")
        else:
            print(i)
if __name__ == "__main__":
    main()
