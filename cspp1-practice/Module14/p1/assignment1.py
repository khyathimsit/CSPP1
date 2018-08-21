class Cipher:
    def __init__(self, text):
        self.text = text
   
    def shift(self, number):
        lower_case = ""
        upper_case = ""
        lower_case = "-" + string.ascii_lowercase() + string.ascii_lowercase()
        upper_case = "-" + string_ascii_uppercase() + string_ascii_uppercase()
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
    print(Cipher.shift(data_input, shift_number))

if __name__ == "__main__":
    main()
