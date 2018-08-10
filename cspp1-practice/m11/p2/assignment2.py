'''
#Exercise: Assignment-2
Author : Khyathi
'''
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for val_ue in word:
        if val_ue in hand:
            hand[val_ue] -= 1
    return hand

def main():
    '''
        Main function
    '''
    n_1 = input()
    adict = {}
    for i_val in range(int(n_1)):
        data = input()
        l_val = data.split()
        adict[l_val[0]] = int(l_val[1])
        i_val += 1
    data1 = input()
    print(update_hand(adict, data1))
        
if __name__ == "__main__":
    main()