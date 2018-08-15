def is_straight(hand):
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
    values_set = set({})
    for i in hand:
        values_set.add(i[1])
    return len(values_set) == 1

def is_four(hand):
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
    hand_values = [f for f, s in hand]
    set_val = set(hand_values)
    if len(set_val) != 2:
        return False
    for f in set_val:
        if hand_values.count(f) == 4:
            return True
    return False 

def is_three(hand):
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
    hand_values = [f for f, s in hand]
    set_val = set(hand_values)
    if len(set_val) <= 2:
        return False
    for f in set_val:
        if hand_values.count(f) == 3:
            return True
    return False 

def is_onepair(hand):
    hand_values = [f for f, s in hand]
    set_val = set(hand_values)
    twopairs = [f for f in set_val if hand_values.count(f) == 2]
    if len(twopairs) != 1:
        return False
    return True

def is_full(hand):
    hand_values = [f for f, s in hand]
    set_val = set(hand_values)
    if len(set_val) != 2:
        return False
    for f in set_val:
        if hand_values.count(set_val) == 3:
            return True
    return False 

def is_twopair(hand):
    hand_values = [f for f, s in hand]
    set_val = set(hand_values)
    twopairs = [f for f in set_val if hand_values.count(f) == 2]
    if len(twopairs) != 2:
        return False
    return True
            
def hand_rank(hand):
    if is_straight(hand) and is_flush(hand):
        return 8
    if is_flush(hand):
        return 7
    if is_straight(hand):
        return 6
    if is_four(hand):
        return 5
    if is_three(hand):
        return 4
    if is_onepair(hand):
        return 3
    if is_full(hand):
        return 2
    if is_twopair(hand):
        return 1
    return 0

def poker(hands):
    
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    COUNT = int(input())
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    print(' '.join(poker(HANDS)))
    