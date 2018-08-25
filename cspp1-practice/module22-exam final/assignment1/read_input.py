'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    input_1 =int(input())
    string = ""
    for i in range(input_1):
        string += input() + "\n"
    print(string)
   
if __name__ == '__main__':
    main()
