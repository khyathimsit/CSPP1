'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
   #string_1 = ""
   string_1 = re.sub('[A-Za-z0-9]+','',string)
   return string_1

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
