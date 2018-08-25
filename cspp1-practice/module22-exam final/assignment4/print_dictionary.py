'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    #list_1 = []
    x = sorted(dictionary)
    #print(x)
    #print(dictionary)
    for i in x:
    #for i in dictionary:
    	print(i, '-', dictionary[i])


def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
