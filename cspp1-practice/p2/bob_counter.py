'''
 Author: Khyathi
 Date : 2-8-18
'''

def main():
    # This code prints the number of times that bob occured in the given string
    s_1 = input()
    co_unt = 0
    for i in range(0,len(s_1)-2):
        if s_1[i] == 'b' and s_1[i+1] == 'o' and s_1[i+2] == 'b':
            co_unt += 1
    print(co_unt)

if __name__== "__main__":
    main()
    