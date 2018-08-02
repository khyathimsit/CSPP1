'''

Author : Khyathi C

Date: 2-8-18

'''
def main():
    ''' This code is used to find the longest substring in the given string'''
    s_1 = input()
    s_2 = ''
    f_s = ''
    n_1 = len(s_1)
    f_max = 0
    f_cnt = 0
    f_s = s_1[0]
    for i in range(0, n_1-1):
        if ord(s_1[i]) <= ord(s_1[i+1]):
            f_cnt += 1
            f_s = f_s + s_1[i+1]
        else:
            if f_cnt > f_max:
                f_max = f_cnt
                s_2 = f_s
            f_cnt = 0
            f_s = s_1[i+1]
    if f_cnt > f_max:
        s_2 = f_s
    print(s_2)
if __name__ == "__main__":
    main()
