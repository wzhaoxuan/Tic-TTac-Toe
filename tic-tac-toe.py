import random

possible_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
PLAYER = 'X'
COMPUTER = 'O'
winner_player = None  # set this variable to null value
game = True
next_turn = 0
move = 1
board = ["-", "-", "-",  # Declare a list to represent each position of tic-tac-toe
         "-", "-", "-",
         "-", "-", "-"]

# Open file to record all move
f = open('logfile_21033105.txt', 'w')
f.write("Tic-tac-toe moves\n")
f.close()


# Display the rules of Tic-tac Toe
def rules():
    print('\nWelcome to TIC-TAC-TOE!')
    print('\nRules')
    print("""1. The game is played on a grid that's 3 squares by 3 squares. Each position are below:
                               |------|------|------|
                               |  1   |  2   |  3   |
                               |------|------|------|
                               |  4   |  5   |  6   |
                               |------|------|------|
                               |  7   |  8   |  9   |
                               |------|------|------|\n
2. You are X, the computer is O. Players take turns putting their marks in empty squares.
\tPlayer   = 'X'
\tComputer = 'O'\n
3. The first player to get 3 of marks in a row (horizontally, vertically or diagonally) is the winner.  
\t|------|------|------|\t\t|------|------|------|\t\t|------|------|------|
\t|  X   |      |      |\t\t|  X   |  X   |  X   |\t\t|  X   |      |      |
\t|------|------|------|\t\t|------|------|------|\t\t|------|------|------|                                    
\t|  X   |      |      |\t\t|      |      |      |\t\t|      |  X   |      |
\t|------|------|------|\t\t|------|------|------|\t\t|------|------|------|
\t|  X   |      |      |\t\t|      |      |      |\t\t|      |      |  X   |
\t|------|------|------|\t\t|------|------|------|\t\t|------|------|------|
         Horizontally                 Vertically                  Diagonally      \n                                                             
4. When all 9 squares are full and no player has 3 marks in a row, the game ends in a TIE.
                                |------|------|------|
                                |  X   |  O   |  X   |
                                |------|------|------|
                                |  X   |  O   |  X   |
                                |------|------|------|
                                |  O   |  X   |  O   |
                                |------|------|------|
                                         Tie          \n
________________________________________________________________________________________________________________________
Let's get started!""")


def show_board():
    """ Create a function to show tic-tac-toe board and match each index with the board array list"""
    print('\t\t\t\t\t|------|------|------|')
    print('\t\t\t\t\t|  ' + board[0] + '   |  ' + board[1] + '   |  ' + board[2] + '   | ')
    print('\t\t\t\t\t|------|------|------|')
    print('\t\t\t\t\t|  ' + board[3] + '   |  ' + board[4] + '   |  ' + board[5] + '   | ')
    print('\t\t\t\t\t|------|------|------|')
    print('\t\t\t\t\t|  ' + board[6] + '   |  ' + board[7] + '   |  ' + board[8] + '   | ')
    print('\t\t\t\t\t|------|------|------|\n')


def who_start():
    """ Create a function to prompt user to decide who will begin the game. If user
         choose player or letter start with p, player will go first. Else, computer
         will go first"""

    choose = input('Who would you like to start (computer or player): ').lower()
    if choose == 'player' or choose.startswith('p'):
        return 'player'

    else:
        return 'computer'


def player_move():
    """Create a function for player move and a loop that keeps asking player for
        their input until a valid choice is made. Player will have to try again
        if number is out of range. After player has input a valid choice in empty
        space, turn will plus one and pass to computer """

    # Global keyword to modify variable next_turn and move
    global next_turn, move
    while True:
        number_choice = int(input("\nSelect a position (1-9): "))
        if number_choice < 1 or number_choice > 9:
            print('This number is out of range. Please try again\n')
            show_board()
            continue

        if board[number_choice - 1] == '-':  # if the position is empty
            print(f"[P]: 'X' place at the {number_choice} position")
            board[number_choice - 1] = PLAYER   # number minus one to match the index
            f = open('logfile_21033105.txt', 'a')
            f.write(f"Move {move}, [P]: 'X' place at the {number_choice} position\n")
            f.close()
            move += 1  # keep track the number of move
            next_turn += 1
            break

        else:
            print('This position has taken. Please try again\n')
            show_board()


# Define a function for computer move
def computer_move():
    """Computer random choose a number from 1-9 and place it if the space is empty.
        The number will later be removed to prevent choosing the same number. After that,
        turn plus one and pass to player """

    # Global keyword to modify variable next_turn and move
    global next_turn, move
    while True:
        computer_choice = random.choice(possible_number)
        if board[computer_choice - 1] == '-':
            board[computer_choice - 1] = COMPUTER
            print(f"[C]: 'O' place at the {computer_choice} position")
            move_record = open('logfile_21033105.txt', 'a')
            move_record.write(f"Move {move}, [C]: 'O' place at the {computer_choice} position \n")
            move_record.close()
            possible_number.remove(computer_choice)
            move += 1  # keep track the number of move
            next_turn += 1
            break


def check_win_tie():
    """Create a function to check winner or tie. If a winner born, winner will equal to
        one of the index of the ways they win and return it. If it doesn't and all space
        has occupied, return a tie and stop the game"""

    # Global keyword to modify variable winner_player and game
    global winner_player, game
    # Horizontal win
    if board[0] == board[1] == board[2] and board[0] != "-":  # first row
        winner_player = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":  # second row
        winner_player = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":  # third row
        winner_player = board[6]
        return True

    # Vertical win
    elif board[0] == board[3] == board[6] and board[0] != "-":  # first column
        winner_player = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":  # second column
        winner_player = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":  # third column
        winner_player = board[2]
        return True

    # Diagonal win
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner_player = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner_player = board[2]
        return True

    # Tie
    elif "-" not in board:
        print("It is a tie!")
        move_record = open('logfile_21033105.txt', 'a')
        move_record.write(f'It is a tie!')
        move_record.close()
        game = False


def winner_tie():
    """Create a function to show the winner or tie"""

    global game  # global keyword to modify variable game
    if check_win_tie():
        print(f'Congratulation. {winner_player} won!')
        move_record = open('logfile_21033105.txt', 'a')
        move_record.write(f'\nCongratulation. {winner_player} won!')
        move_record.close()
        game = False


"""Game start"""
rules()
turn = who_start()
print('The', turn, 'will go first')

while game:
    """If the game start with player, player will move since the turn start from zero with 
        the reminder zero and next will be computer's turn with reminder one. Same goes to if 
        the game start with computer. This process will loop until the winner is checked and 
        game stop"""

    if turn == 'player':
        # When reminder is zero, player turn
        if next_turn % 2 == 0:
            player_move()
            show_board()

        # When reminder is one, computer turn
        else:
            computer_move()
            show_board()

    # If the game start with computer
    elif turn == 'computer':
        # When reminder is zero, computer turn
        if next_turn % 2 == 0:
            computer_move()
            show_board()

        # When reminder is one, player turn
        else:
            player_move()
            show_board()

    # Show a winner or tie
    winner_tie()
print('Hope you enjoy the game! ^_^')
