'''
Author: khyathi
'''

def main():
    '''to find whether the given number is perfect cube or not'''
    x_1 = input()
    ans = 0
    while ans**3 < int(x_1):
        ans = ans + 1
    if ans**3 == int(x_1):
        print(str(x_1) + ' is a perfect cube')
    else:
        print(str(x_1) + ' is not a perfect cube')
if __name__ == "__main__":
    main()
