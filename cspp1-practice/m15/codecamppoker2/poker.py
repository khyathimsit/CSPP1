def is_straight(hand):
    
    stng_values = "--23456789TJQKA"
    hand_values = []

    for i in hand:
        hand_values.append(stng_values.index(i[0]))

    hand_values.sort()

    #print(hand_values)

    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] != -1:
            return False

    return True

def is_flush(hand):
    values_set = set({})

    for i in hand:
        values_set.add(i[1])

    #print(values_set)

    return len(values_set) == 1
def is_four(hand):
    count = 1
    stng_values = "--23456789TJQKA"
    hand_values = []
    for i in hand:
        hand_values.append(stng_values.index(i[0]))
    hand_values.sort()
    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] == 0:
            count += 1
    if count==4:
        return True
    return False

def is_three(hand):
    count = 1
    stng_values = "--23456789TJQKA"
    hand_values = []
    for i in hand:
        hand_values.append(stng_values.index(i[0]))
    hand_values.sort()
    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] == 0:
            count += 1
    if count==3:
        return True
    return False
def is_onepair(hand):
    count = 1
    stng_values = "--23456789TJQKA"
    hand_values = []
    for i in hand:
        hand_values.append(stng_values.index(i[0]))
    hand_values.sort()
    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] == 0:
            count += 1
    if count==2:
        return True
    return False

def hand_rank(hand):
    if is_straight(hand) and is_flush(hand):
        #print("called 3")
        return 3
    if is_flush(hand):
        #print("called 2")
        return 2
    if is_straight(hand):
        #print("called")
        return 1
    if is_four(hand):
        return 4
    if is_three(hand):
        return 5
    if is_onepair(hand):
        return 6
    return 0

def poker(hands):
    
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)

    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    #print(HANDS)

    #print(is_flush(HANDS))
