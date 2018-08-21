'''
Class intro
'''
import string
class Cipher:
    '''
    Ceaser cipher code
    '''
    def __init__(self, text):
        '''
        init method
        '''
        self.text = text
    def __len__(self):
        count = 0
        for _ in self.text:
            count += 1
        return count
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
    cipher_obj = Cipher(data_input)
    print(cipher_obj.shift(shift_number))
    #print(Cipher.shift(data_input, shift_number))

if __name__ == "__main__":
    main()
