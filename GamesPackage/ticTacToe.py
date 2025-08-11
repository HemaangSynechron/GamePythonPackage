from rich import print

board = [["" for _ in range(1,4)] for __ in range(1,4)]
count = 1
for i in range(3):
	for j in range(3):
		board[i][j] = ""
		count += 1

x_str = "[bold red]X[/bold red]"
o_str = "[bold green]O[/bold green]"

def printBoard():
	count = 1
	print("-" * 13)
	for row in board:
		for col in row:
			if col == "":
				col = str(count)
			print("|", col, end=" ")
			count += 1
		print("|\n","-" * 11)

def checkWin(board:list[list])->int:
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] != "":
			return 1 if board[i][0]==x_str else 2
		if board[0][i] == board[1][i] == board[2][i] != "":
			return 1 if board[0][i]==x_str else 2
	# Diagonal
	if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
		return 1 if board[1][1]==x_str else 2
	return 0
def play():
	global board, count
	while True:
		printBoard()	
		move = input(f"Enter your {'X' if count % 2 == 0 else 'O'}'s move (1-9): ")
		if move.isdigit() and 1 <= int(move) <= 9:
			move = int(move) - 1
			row, col = move//3,move%3
			if board[row][col] == "":
				board[row][col] = x_str if count % 2 == 0 else o_str
				printBoard()
				if winV:=checkWin(board):
					print("Winv", winV)
					print(f"{'X' if winV==1 else 'O'} wins!")
					break
				count += 1
			else:
				print("Invalid move! Try again.")
		else:
			print("Invalid input! Please enter a number between 1 and 9.")