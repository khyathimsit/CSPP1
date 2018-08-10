# Assignment-3
'''
Author : Khyathi
'''

def is_valid_word(wo_rd, ha_nd, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    count_val = 0
    len_val = len(wo_rd)
    for i in wo_rd:
        if i in ha_nd:
            count_val += 1

    if len_val == count_val:
        if wo_rd in word_list:
            return True
        return False
    return False

def main():
    '''main function'''
    wo_rd = input()
    num_n = int(input())
    a_dict = {}
    for i in range(num_n):
        data = input()
        l_1 = data.split()
        a_dict[l_1[0]] = int(l_1[1])
        i += 1
    l_2 = input().split()
    print(is_valid_word(wo_rd, a_dict, l_2))

if __name__ == "__main__":
    main()
