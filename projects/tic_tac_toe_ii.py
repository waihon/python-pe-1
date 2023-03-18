from random import choice

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
    """)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    number_coordinates = { '1': (0, 0),
                           '2': (0, 1),
                           '3': (0, 2),
                           '4': (1, 0),
                           '5': (1, 1),
                           '6': (1, 2),
                           '7': (2, 0),
                           '8': (2, 1),
                           '9': (2, 2) }
    
    while True:
        player_move = input("Enter your move (1-9): ")
        valid_input = [ str(i) for i in range(1, 10) ]
        if player_move not in valid_input:
            print("Valid move is from 1 to 9.")
            continue
        coordinate = number_coordinates[player_move]
        if coordinate not in make_list_of_free_fields(board):
            print(player_move, "is already occupied.")
            continue

        board[coordinate[0]][coordinate[1]] = 'O'
        break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    result = []
    rows = 3
    cols = 3
    for row in range(rows):
        for col in range(cols):
            if board[row][col] not in ['X', 'O']:
                result.append((row, col))
    return result

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    rows = 3
    for row in range(rows):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True

    cols = 3
    for col in range(cols):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 9:
        board[1][1] = 'X'
    else:
        random_move = choice(make_list_of_free_fields(board))
        board[random_move[0]][random_move[1]] = 'X'

if __name__ == "__main__":
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print(make_list_of_free_fields(board))
    draw_move(board)
    display_board(board)
