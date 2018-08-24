def horizontal(board, turn):
	cnt = 0
	for i in range(3):
		for j in range(3):
			if not board[i][j] == turn:
				cnt += 1
		if cnt == 0:
		    return True
		cnt = 0
	return False

def vertical(board, turn):
	cnt = 0
	for i in range(3):
		for j in range(3):
			if not board[j][i] == turn:
				cnt += 1
		if cnt == 0:
		    return True
		cnt = 0
	return False

def diagonal_frwd(board, turn):
	cnt = 0
	for i in range(3):
		if not board[i][i] == turn:
				cnt += 1
	if cnt == 0:
		return True
	return False	

def diagonal_back(board, turn):
	cnt = 0
	j = 2
	for i in range(3):
		if not board[i][i] == turn:
				cnt += 1
		j -= 1
	if cnt == 0:
		return True
	return False

def main():
 cnt = 0
 cnt_x = 0
 cnt_o = 0
 cnt_dot = 0
 cnt_other = 0
 row_1 = input().split()
 row_2 = input().split()
 row_3 = input().split()
 board = [row_1, row_2, row_3]
 
 for i in range(3):
 	for j in range(3):
 		if board[i][j] == 'x':
 			cnt_x += 1
 		elif board[i][j] == 'o':
 			cnt_o += 1
 		elif board[i][j] == '.':
 			cnt_dot += 1
 		else:
 			cnt_other += 1
if cnt_other != 0:
	print("Invalid input")
	cnt += 1
elif cnt_x>cnt_o+1 or cnt_o>cnt_x+1:
	print("Invalid game..")
	cnt+=1
turn_x = 'x'
boolean_x = (horizontal(board,turn_x)
	         or vertical(board,turn_x)
	         or diagonal_frwd(board,turn_x)
	         or diagonal_back(board,turn_x))

turn_o = 'o'
boolean_o = (horizontal(board,turn_o)
	         or vertical(board,turn_o)
	         or diagonal_frwd(board,turn_o)
	         or diagonal_back(board,turn_o))

if boolean_x and boolean_o and cnt == 0:
	print("Invalid game")
if boolean_x and cnt == 0:
	print(turn_x)
	cnt += 1
if boolean_o and cnt == 0:
    print(turn_o)
    cnt += 1
if cnt == 0:
   	print("Draw")

if __name__ == '__main__':
	main()
	