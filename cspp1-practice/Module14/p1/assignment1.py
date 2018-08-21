import string
'''
Class intro
'''
class Cipher:
    '''
    Ceaser cipher code
    '''
    def __init__(self, text):
        '''
        init method
        '''
        self.text = text
    def shift(self, number):
        '''
        Shift method to move to the next required letter
        '''
        lower_case = ""
        upper_case = ""
        lower_case = "-" + string.ascii_lowercase + string.ascii_lowercase
        upper_case = "-" + string.ascii_uppercase + string.ascii_uppercase
        result_string = ""
        for i in range(0, len(self.text)):
            if self.text[i] in lower_case:
                result_string += lower_case[lower_case.index(self.text[i]) + number]
            elif self.text[i] in upper_case:
                result_string += upper_case[upper_case.index(self.text[i]) + number]
            else:
                result_string += self.text[i]

        return result_string


def main():
    '''
        Function to handle testcases
    '''
    data_input = input()
    shift_number = int(input())
    Cipher_obj = Cipher(data_input)
    print(Cipher_obj.shift(shift_number))
    #print(Cipher.shift(data_input, shift_number))

if __name__ == "__main__":
    main()
