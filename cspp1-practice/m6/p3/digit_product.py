'''
Author : Khyathi
'''
def main():
    '''
    This code is to print the digit product
    '''
    n = int(input())
    p = 1
    while n > 0:
        a = n % 10
        n = n // 10
        p = p * a
    print(p)
    #if n == 0:
        #print("0")
if __name__ == "__main__":
    main()
