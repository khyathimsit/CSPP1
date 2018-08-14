def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    count_d = 0
    count_s = 0
    count_c = 0
    count_h = 0
    for i in hand:
    	if i[1] == 'D':
    		count_d += 1
    	elif i[1] == 'S':
    		count_s += 1
    	elif i[1] == 'C':
    		count_c += 1
    	elif i[1] == 'H':
    		count_h += 1
    	else:
    		print("Not a suit")
    if count_d == 5 or count_s == 5 or count_c == 5 or count_h == 5:
    	return True
    else:
        return False

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    print(is_flush(HANDS))