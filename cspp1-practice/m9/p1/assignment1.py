'''
Author : Khyathi
First, implement the function isWordGuessed that takes in two parameters -
a string, secret_word, and a list of letters, letters_guessed. This function
returns a boolean - True if secret_word has been guessed (ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    secretword_list = list(secret_word)
    temp = letters_guessed[:]
    if secretword_list == []:
        return True
    i = 0
    while i < len(letters_guessed):
        if i in temp[0:i]:
            temp = letters_guessed[:]
        else:
            if letters_guessed[i] in secretword_list:
                count = count + secretword_list.count(letters_guessed[i])
                if count == len(secretword_list):
                    return True
        i = i+1
    if count < len(secretword_list):
        return False
    return "0"

def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
