'''Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.'''

"""game = [ [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]"""


def draw_board(game, size):
    grid1 = ''' ---'''
    grid2 = '''|'''
    for line in game:
        print(grid1*size)
        new_line = []
        for cell in line:
            new_line.append(cell)
            new_line.append(grid2)
        new_line = list(grid2)+new_line
        print(*new_line)

    print(grid1*size)


