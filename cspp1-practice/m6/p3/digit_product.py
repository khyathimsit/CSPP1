'''
Autho : Khyathi
'''
def main():
    '''
    This code is to print the digit product
    '''
    n = int(input())
    i = 0
    p = 1
    for i in range(str(n)):
        x = n % 10
        p = p * x
        y = n // 10
        x = y
    print(p)
if __name__ == "__main__":
    main()
