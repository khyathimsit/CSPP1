'''
Author : Khyathi
Date: 4-8-18
Exam 1
'''
def main():
    '''
    This code is used to replace all the special characters with a space
    '''
    str_input = input()
    str_2 = ''
    for char in str_input:
        if char in "!@#$%^*":
            str_2 += " "
        else:
            str_2 += char
    print(str_2)
if __name__ == "__main__":
    main()
