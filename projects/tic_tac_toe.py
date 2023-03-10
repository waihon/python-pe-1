"""
Write a simple program which pretends to play tic-tac-toe with the user.
To make it all easier for you, we've decided to simplify the game. Here are
our assumptions:

o the computer (i.e., your program) should play the game using 'X's;
o the user (e.g., you) should play the game using 'O's;
o the first move belongs to the computer − it always puts its first 'X' in
  the middle of the board;
o all the squares are numbered row by row starting with 1 (see the example
  session below for reference)
o the user inputs their move by entering the number of the square they
  choose − the number must be valid, i.e., it must be an integer, it must be
  greater than 0 and less than 10, and it cannot point to a field which is
  already occupied;
o the program checks if the game is over − there are four possible verdicts:
  the game should continue, the game ends with a tie, you win, or the computer
  wins;
o the computer responds with its move and the check is repeated;
o don't implement any form of artificial intelligence − a random field choice
  made by the computer is good enough for the game.

The example session with the program may look as follows:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
You won!

Requirements
Implement the following features:

o the board should be stored as a three-element list, while each element is
  another three-element list (the inner lists represent rows) so that all of
  the squares may be accessed using the following syntax:
  board[row][column]
o each of the inner list's elements can contain 'O', 'X', or a digit
  representing the square's number (such a square is considered free)
o the board's appearance should be exactly the same as the one presented in the
  example.
o implement the functions defined for you in the editor.

"""

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
"""
    )


def enter_move(board):
    # The function accepts the board's current status, asks the user about their
    # move, checks the input, and updates the board according to the user's
    # decision.
    move_to_indexes = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                       4: (1, 0), 5: (1, 1), 6: (1, 2),
                       7: (2, 0), 8: (2, 1), 9: (2, 2)}
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10):
                print("Invalid move! Please try again.")
                continue

            row = move_to_indexes[move][0]
            col = move_to_indexes[move][1]
            square_val = board[row][col]
            if square_val not in range(1, 10):
                print("That's already occupied! Please try again.")
                continue

            # That's not occupied yet, so update it with what user plays
            board[row][col] = 'O'
            break
        except:
            print("A possible move is between 1 and 9.")
        

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column
    # numbers.
    result = []
    for row in range(3):
        for col in range(3):
            if board[row][col] in range(1, 10):
                result.append((row, col))

    return result


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if the player
    # using 'O's or 'X's has won the game.
    # Check diagonally first
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) \
    or (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True

    # Check horizontally next
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    # Check vertically last
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    from random import choice
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 9:
        # Nothing occupied yet, so occupy the center
        board[1][1] = 'X'
    else:
        # The initial version of computer's moves doesn't implement any AI,
        # just a random choice of occupied squares.
        row, col = choice(free_fields)
        board[row][col] = 'X'
      

if __name__ == "__main__":
    # Computer plays first and always puts X in the middle
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    display_board(board)

    draw_move(board)
    display_board(board)

    enter_move(board)
    display_board(board)

    free_fields = make_list_of_free_fields(board)
    print(len(free_fields))
    print(free_fields)

    draw_move(board)
    display_board(board)

    board = [['O', 2,   'X'],
             [4,   'X', 6],
             ['X', 8,   'O']]
    display_board(board)
    print('X:', victory_for(board, 'X'))
    print('O:', victory_for(board, 'O'))

    board = [['X', 2,   'X'],
             [4,   'X', 6],
             ['O', 'O', 'O']]
    display_board(board)
    print('X:', victory_for(board, 'X'))
    print('O:', victory_for(board, 'O'))

    board = [['O', 'X', 2],
             [4,   'X', 6],
             ['O', 'X', 9]]
    display_board(board)
    print('X:', victory_for(board, 'X'))
    print('O:', victory_for(board, 'O'))
