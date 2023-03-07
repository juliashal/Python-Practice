'''Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

import getpass # this library will help to hide players answers 😉

next = 'Y'

while next == 'Y':
    while True:
        player1 = getpass.getpass(
            "Player1 turn. \n Type 'R'-rock, 'S'-scissors,'P'-paper: ").upper()
        if player1 in ('R', 'S', 'P'):
            break

    while True:
        player2 = getpass.getpass(
            "Player2 turn. \n Type 'R'-rock, 'S'-scissors,'P'-paper: ").upper()
        if player2 in ('R', 'S', 'P'):
            break

    if player1 == player2:
        print("It's a draw.")
    elif ((player1 == 'R') & (player2 == 'S')) | ((player1 == 'S') & (player2 == 'P')) | ((player1 == 'R') & (player2 == 'S')):
        print("Player 1 WINS. Congratulaitons!\n")
    else:
        print("Player 2 WINS. Congratulaitons!\n")

    next = input("Do you want to try again? (Y)/(N)").upper()
