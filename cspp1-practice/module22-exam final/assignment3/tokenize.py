'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

# def tokenize(string):
#     pass
            
def main():
    input_1 = int(input())
    string = input()
    wordlist = []
    wordlist = string.split()
    #print(wordlist)
    wordfreq = [wordlist.count(word) for word in wordlist]
    dict_1 = dict(zip(wordlist, wordfreq))
    print(dict_1)
    
if __name__ == '__main__':
    main()
