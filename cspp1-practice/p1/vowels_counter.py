'''
Author : Khyathi Cheedalla
Date: 2-8-16
'''

def main():
    '''
        This function is used to find the vowels in the given string
    '''
    st_r = input()
    co_unt = 0
    for cha_r in st_r:
        if cha_r in ('a', 'e', 'i', 'o', 'u'):
            co_unt += 1
    print(co_unt)

if __name__ == "__main__":
    main()
  