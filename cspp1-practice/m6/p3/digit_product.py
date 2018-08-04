'''
Author : Khyathi
'''
def main():
    '''
    This code is to print the digit product
    '''
    n_input = int(input())
    p_out = 1
    if n_input == 0:
        print("0")
        break
    while n_input > 0:
        a_1 = n_input % 10
        n_input = n_input // 10
        p_out = p_out * a_1
    print(p_out)
if __name__ == "__main__":
    main()
