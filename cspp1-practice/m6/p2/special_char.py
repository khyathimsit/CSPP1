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
    for char in str_input:
        if char in "!@#$%^*":
            str_input.append(" ")
        else:
            print(str_input)
if __name__ == "__main__":
    main()
    