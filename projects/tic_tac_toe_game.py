from tic_tac_toe import display_board, enter_move, make_list_of_free_fields, \
    victory_for, draw_move

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

while True:
    if len(make_list_of_free_fields(board)) == 0:
        break

    # Computer to move
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer won!")
        break

    if len(make_list_of_free_fields(board)) == 0:
        break

    # User to move
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("Yon won!")
        break

if victory_for(board, 'X') or victory_for(board, 'O'):
    pass
else:
    print("It's a tie!")
