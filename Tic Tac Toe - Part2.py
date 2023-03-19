'''If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.'''

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


board_size = len(game)

'''check rows and columns'''
for i in range(board_size):

    set_row = list(set(game[i]))
    column = [game[j][i] for j in range(board_size)]
    set_column = list(set(column))

    if len(set_row)==1:
        winner = set_row[0]
    elif len(set_column)==1:
        winner = set_column[0]

'''check diagonal'''
diagonal = [game[j][j] for j in range(board_size)]
set_diagonal = list(set(diagonal))
if len(set_diagonal)==1:
    winner = set_diagonal[0]

'''print the result'''
if not winner:
    print(f"There is no winner")
else:
    print(f"the Winner is Player {winner}")

