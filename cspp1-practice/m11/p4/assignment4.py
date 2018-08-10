#Exercise: Assignment-4
'''
Author : Khyathi
'''

#We are now ready to begin writing the code that interacts with the player.
#We'll be implementing the playHand function. This function allows the user
#to play out a single hand. First, though, you'll need to implement the helper
#calculateHandlen function, which can be done in under five lines of code.

def calculate_handlen(ha_nd):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum_val = 0
    for values in ha_nd.values():
        sum_val += values
    return sum_val

def main():
    '''main function'''
    num_n = input()
    a_dict = {}
    for i in range(int(n)):
        da_ta = input()
        l_1 = da_ta.split()
        a_dict[l_1[0]] = int(l_1[1])
    print(calculate_handlen(a_dict))

if __name__ == "__main__":
    main()
