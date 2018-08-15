'''
Program for poker game
'''
def is_straight(hand):
    '''
    Straight Function
    '''
    stng_values = "--23456789TJQKA"
    hand_values = []
    for i in hand:
        hand_values.append(stng_values.index(i[0]))
    hand_values.sort()
    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] != -1:
            return False
    return True

def is_flush(hand):
    '''
    Flush Function
    '''
    values_set = set({})
    for i in hand:
        values_set.add(i[1])
    return len(values_set) == 1

def is_four(hand):
    '''
    Function for 4 of a kind
    '''
    # count = 1
    # stng_values = "--23456789TJQKA"
    # hand_values = []
    # for i in hand:
    #     hand_values.append(stng_values.index(i[0]))
    # hand_values.sort()
    # for i in range(len(hand_values) - 1):
    #     if hand_values[i] - hand_values[i+1] == 0:
    #         count += 1
    # if count==4:
    #     return True
    # return False
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) != 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 4:
            return True
    return False

def is_three(hand):
    '''
    Function for 3 of a kind
    '''
    # count = 1
    # stng_values = "--23456789TJQKA"
    # hand_values = []
    # for i in hand:
    #     hand_values.append(stng_values.index(i[0]))
    # hand_values.sort()
    # for i in range(len(hand_values) - 1):
    #     if hand_values[i] - hand_values[i+1] == 0:
    #         count += 1
    # if count==3:
    #     return True
    # return False
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) <= 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 3:
            return True
    return False

def is_onepair(hand):
    '''
    Function for one pair
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    twopairs = [f_1 for f_1 in set_val if hand_values.count(f_1) == 2]
    if len(twopairs) != 1:
        return False
    return True

def is_full(hand):
    '''
    Full hand function
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) != 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 3:
            return True
    return False

def is_twopair(hand):
    '''
    Function for two pair
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    twopairs = [f_1 for f_1 in set_val if hand_values.count(f_1) == 2]
    if len(twopairs) != 2:
        return False
    return True

def hand_rank(hand):
    '''
    Function for hand rank
    '''
    rank = 0
    if is_straight(hand) and is_flush(hand):
        rank =8
    elif is_flush(hand):
        rank = 7
    elif is_straight(hand):
        rank = 6
    elif is_four(hand):
        rank = 5
    elif is_three(hand):
        rank = 4
    elif is_onepair(hand):
        rank = 3
    elif is_full(hand):
        rank = 2
    elif is_twopair(hand):
        rank = 1
    else:
        rank = 0

def poker(hands):
    '''Poker function
    '''
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    COUNT = int(input())
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    print(' '.join(poker(HANDS)))
    