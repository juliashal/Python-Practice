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

while True:
    grid_size = input("Type a board side length (ex., for 3x3 board the side is 3): \n")
    if grid_size.isnumeric():
        break

grid_size = int(grid_size)


def draw_board(size):
    grid1 = ''' ---'''
    grid2 = '''|   '''
    for i in range(size):
        print(grid1*size)
        print(grid2*(size+1))
    print(grid1*size)

draw_board(grid_size)
