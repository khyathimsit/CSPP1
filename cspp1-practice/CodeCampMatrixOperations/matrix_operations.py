def mult_matrix(m_1, m_2, row_1, col_1, row_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if col_1 == row_2:
        mul_res = []
        for i_val in range(0, row_1):
            a_temp = []
            for j_val in range(0, row_1):
                sum_val = 0
                for k_val in range(0, col_1):
                    sum_val = sum_val + (m_1[i_val][k_val]*m_2[k_val][j_val])
                a_temp.append(sum_val)
            mul_res.append(a_temp)
        return mul_res
    print("Error: Matrix shapes invalid for mult")


def add_matrix(m_1, m_2, row_1, col_1, row_2, col_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if row_1 == row_2 and col_1 == col_2:
        add_res = []
        for i_val in range(0, row_1):
            a_temp = []
            for j_val in range(0, col_1):
                a_temp.append(m_1[i_val][j_val] + m_2[i_val][j_val])
            add_res.append(a_temp)
        return add_res
    print("Error: Matrix shapes invalid for addition")

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    row_1, col_1 = input().split(',')
    row_1 = int(row_1)
    col_1 = int(col_1)

    matrix_1 = []
    matrix_2 = []
    for i in range(0, row_1):
        matrix_1.append(list(map(int, input().split())))
    #print(matrix_1)

    row_2, col_2 = input().split(',')
    row_2 = int(row_2)
    col_2 = int(col_2)
    for i in range(0, row_2):
        matrix_2.append(list(map(int, input().split())))
    #print(matrix_2)

    flag = True
    for i in matrix_1:
        count = 0
        for _ in i:
            count += 1
        if count != col_1:
            flag = False
    #print(flag)

    if flag is False:
        print("Error: Invalid input for the matrix")

    flag = True
    for i in matrix_2:
        count = 0
        for j in i:
            count += 1
        if count != col_2:
            flag = False

    #print(flag)

    if flag is False:
        print("Error: Invalid input for the matrix")

    #print(flag)

    if flag is True:
        print(add_matrix(matrix_1, matrix_2, row_1, col_1, row_2, col_2))
        print(mult_matrix(matrix_1, matrix_2, row_1, col_1, row_2))

def main():
    '''
    Main Function
    '''
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    read_matrix()
    
if __name__ == '__main__':
    main()
