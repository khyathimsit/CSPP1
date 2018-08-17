'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
import copy
def word_list(input1, input2):
    f_1 = ""
    f_2 = ""
    
    f_1 = re.sub('[^ a-z]','',input1.lower())
    f_2 = re.sub('[^ a-z]','',input2.lower())
    
    # f_1 = f_1.replace("'", "")
    # f_2 = f_2.replace("'", "")
    # print(f_1, f_2)

    list_1 = []
    list_2 = []
    
    list_1 = f_1.split()
    list_2 = f_2.split()
    #print(list_1)
   
    remove_1 = load_stopwords("stopwords.txt")
    key_list = list(remove_1.keys())

    word_list_1 = list_1[:]

    for i in word_list_1:
    	if i in key_list:
    		list_1.remove(i)

    word_list_1 = list_2[:]

    for i in word_list_1:
    	if i in key_list:
    		list_2.remove(i)

    # for i in key_list:
    #     for j in list_1:
    #         if i == j:
    #             list_1.remove(j)
    
    # for i in key_list:
    #     for j in list_2:
    #         if i == j:
    #             list_2.remove(j)   
    #print(list_1,list_2)
    return freq_count(list_1, list_2)

def freq_count(list_1, list_2):
    dict_1 = {}
    dict_2 = {}
    common_dict = {}
    for k in list_1:
        if k not in dict_1:
            dict_1[k] = 1
        else:
            dict_1[k] += 1
    #print(dict_1)

    for k in list_2:
        if k not in dict_2:
            dict_2[k] = 1
        else:
            dict_2[k] += 1
    #print(dict_2)
    for i in dict_1:
        if i in dict_2:
            common_dict[i] = [dict_1[i], dict_2[i]]
        else:
        	common_dict[i] = [dict_1[i], 0]
    for j in dict_2:
    	if j not in common_dict:
    		common_dict[j] = [0, dict_2[j]]
    d1 = copy.deepcopy(common_dict)

    for l in d1:
    	len_1 = len(l)
    	if len_1 == 0:
    		del common_dict[l]
    print(sorted(common_dict.keys()))
    return common_dict

    
    


def similarity(dict1):
    '''
        Compute the document distance as given in the PDF
    '''
    num_val = 0
    a_1 = 0
    b_1 = 0
    distance = 0
    for i in dict1:
        num_val += dict1[i][0] * dict1[i][1]
        a_1 += dict1[i][0] ** 2
        b_1 += dict1[i][1] ** 2
    print(num_val,a_1,b_1)
    distance = (num_val)/(math.sqrt(a_1)*math.sqrt(b_1))
    return distance

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    common_dict_1 = word_list(input1, input2)
    print(similarity(common_dict_1))

if __name__ == '__main__':
    main()
