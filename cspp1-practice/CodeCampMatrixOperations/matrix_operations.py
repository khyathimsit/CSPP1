def mult_matrix(m1, m2, row_1, col_1, row_2, col_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if col_1 == row_2:
        mul = []
        for i in range(0, row_1):
            a = []
            for j in range(0, row_1):
                sum_val = 0
                for k in range(0, col_1):
                    sum_val = sum_val+(m1[i][k]*m2[k][j])
                a.append(sum_val)
            mul.append(a)
        return mul
    else:
        print("Error: Matrix shapes invalid for mult")


def add_matrix(m1, m2, row_1, col_1, row_2, col_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if row_1==col_1 and row_2==col_1:
        add = []
        for i in range(0, row_1):
            a = []
            for j in range(0, col_1):
                a.append(m1[i][j] + m2[i][j])
            add.append(a)
        return add
    else:
        print("Error: Matrix shapes invalid for addition")

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    row_1,col_1 = input().split(',')
    row_1 = int(row_1)
    col_1 = int(col_1)

    matrix_1 = []
    matrix_2 = []
    for i in range(0, row_1):
        matrix_1.append(list(map(int,input().split())))
    #print(matrix_1)
    
    row_2,col_2 = input().split(',')
    row_2 = int(row_2)
    col_2 = int(col_2)
    for i in range(0, row_2):
        matrix_2.append(list(map(int,input().split())))
    #print(matrix_2)

    flag =True
    for i in matrix_1:
        count = 0
        for j in i:
            count += 1
        if count != col_1s:
            flag = False
    #print(flag)
    
    if flag == False:
        print ("Error: Invalid input for the matrix")
      
    flag =True
    for i in matrix_2:
        count = 0
        for j in i:
            count += 1
        if count != col_2:
            flag = False

    #print(flag)

    if flag == False:
        print ("Error: Invalid input for the matrix")

    #print(flag)

    if flag == True:
        print(add_matrix(matrix_1, matrix_2, row_1, col_1, row_2, col_2))
        print(mult_matrix(matrix_1, matrix_2, row_1, col_1, row_2, col_2))

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    read_matrix()
    
if __name__ == '__main__':
    main()
