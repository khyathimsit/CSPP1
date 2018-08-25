'''
Author: Khyathi
'''
import re
def clean_string(string):
   #string_1 = ""
   string_1 = re.sub('[^A-Za-z0-9]+', '', string)
   return string_1

def main():
    '''
    Main Function
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
