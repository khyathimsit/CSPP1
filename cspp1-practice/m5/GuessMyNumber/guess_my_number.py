'''

Author : Khyathi
Date : 03 Aug 2018

'''
def main():
    ''' This function is used to make guess'''
    print("Guess a number between 1 and 100")
    l_ow= 0
    h_igh = 100
    m_id = (l_ow + h_igh)//2
    s_1 = ''
    #print("Is your number greater than M ")

    while s_1 != 'c':
        if s_1 == 'h':
            l_ow = m_id
            m_id = (l_ow + h_igh)//2
        if s_1 == 'l':
            h_igh = m_id
            m_id = (l_ow + h_igh)//2
        print("Is your number greater than M ?")
        print("Mid number is" + str(m_id))
        print("Enter h : high l: low and c: correct")
        s_1 = input()
    print("Number is : " + str(m_id))
if __name__ == "__main__":
    main()
