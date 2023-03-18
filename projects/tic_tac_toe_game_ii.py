from tic_tac_toe_ii import display_board, \
     enter_move, make_list_of_free_fields, \
     victory_for, draw_move

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

move = 0
while True:
    move += 1
    if move % 2 == 1:
        draw_move(board)
        display_board(board)
    else:
        enter_move(board)
            
    #display_board(board)    
    if victory_for(board, "X"):
        print("Computer won")
        break

    if victory_for(board, "O"):
        print("You won")
        break

    if not make_list_of_free_fields:
        print("Tie")
        break
