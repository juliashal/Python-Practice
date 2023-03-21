'''The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

game = [[0, 0, X],
	    [0, 0, 0],
	    [0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.'''

"""game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

players = {'Player 1': 'X', 'Player 2': 'O'}"""


def check_turn(size):

    while True:
        turn = input("Type your move (format: row number,column number): ")
        # digits count and max position checks
        digits = [x for x in turn if x.isdigit() and int(x) <= size and int(x) > 0]
        if len(digits) == 2 and ("," in turn):
            break

    turn = list(turn)
    turn.remove(",")
    '''create indexes pair'''
    turn = [int(x)-1 for x in turn]
    return turn


def turn(game, size, player):
    turn = check_turn(size)

    while game[turn[0]][turn[1]] != 0:
        print("This cell is occupied")
        turn = check_turn()

    game[turn[0]][turn[1]] = player
    return game
