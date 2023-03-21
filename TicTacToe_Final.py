'''In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

Draw the Tic Tac Toe game board
Checking whether a game board has a winner
Handle a player move from user input

The next step is to put all these three components together to make a two-player Tic Tac Toe game! 
Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend.'''

from TicTacToe_Board import draw_board
from TicTacToe_Fill_the_board import turn
from TicTacToe_Winner import check_winner

while True:
    grid_size = input(
        "Type a board side length (ex., for 3x3 board the side is 3): \n")
    if grid_size.isnumeric():
        break

players = {'Player 1': 'X', 'Player 2': 'O'}

grid_size = int(grid_size)
'''generate an empty board'''
game = [[0]*grid_size for i in range(grid_size)]

draw_board(game, grid_size)

'''check how many empty cells left'''
spaces_left = sum([sublist.count(0) for sublist in game])

while spaces_left > 0:
    for player in players:
        print(f"it's {player} turn")
        game = turn(game, grid_size, players[player])
        draw_board(game, grid_size)
        winner = check_winner(game)
        '''print the result'''
        if winner:
            print(f"the Winner is {player}")
            spaces_left = 1

        spaces_left -= 1
        if spaces_left == 0:
            print(f"End of the game")
            break

    spaces_left

if not winner:
    print(f"NO winner")