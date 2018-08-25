'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    length = len(sudoku)
    num = 1
    while num <= length:
        i = 0
        while i < length:
            cnt_row = 0
            cnt_col = 0
            j = 0
            while j < length:
                if sudoku[i][j] == num:
                    cnt_row = cnt_row + 1
                if sudoku[j][i] == num:
                    cnt_col = cnt_col + 1
                j = j+1
            if cnt_row != 1 or cnt_col != 1:
                return False
            i = i +1
        num = num + 1
    return True

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
