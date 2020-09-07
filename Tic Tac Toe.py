# Create a board
# display the board
# play game
# Check if win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player
    # display game board
    # Player 1 turn
    # check Win or tie
    # Player 2 turn


#-------------------------Global variables-----------------------------
game_board = ["__", "__", "__",
              "__", "__", "__",
              "__", "__", "__"]
game_still_on = True
winner = None
current_player = "X"


def display_board():
    print(game_board[0] + "  " + game_board[1] + "  " + game_board[2])
    print(game_board[3] + "  " + game_board[4] + "  " + game_board[5])
    print(game_board[6] + "  " + game_board[7] + "  " + game_board[8])


def handle_turn(player):
    print(player + "'s turn.")
    choose_square = input("Choose a square from 1-9: ")

    valid = False
    while not valid:

        while choose_square not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            choose_square = input("Invalid input. Choose a square from 1-9: ")

        choose_square = int(choose_square) - 1

        if game_board[choose_square] == "__":
            valid = True
        else:
            print("You can't play there. Play again!")

    game_board[choose_square] = player

    display_board()


def check_if_game_over():
    check_for_win()
    check_if_tie()


def check_for_win():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_on
    row1 = game_board[0] == game_board[1] == game_board[2] != "__"
    row2 = game_board[3] == game_board[4] == game_board[5] != "__"
    row3 = game_board[6] == game_board[7] == game_board[8] != "__"
    if row1 or row2 or row3:
        game_still_on = False
    if row1:
        return game_board[0]
    elif row2:
        return game_board[3]
    elif row3:
        return game_board[6]
    return


def check_columns():
    global game_still_on
    column1 = game_board[0] == game_board[3] == game_board[6] != "__"
    column2 = game_board[1] == game_board[4] == game_board[7] != "__"
    column3 = game_board[2] == game_board[5] == game_board[8] != "__"
    if column1 or column2 or column3:
        game_still_on = False
    if column1:
        return game_board[0]
    elif column2:
        return game_board[1]
    elif column3:
        return game_board[2]
    return


def check_diagonals():
    global game_still_on
    diagonal1 = game_board[0] == game_board[4] == game_board[8] != "__"
    diagonal2 = game_board[6] == game_board[4] == game_board[2] != "__"
    if diagonal1 or diagonal2:
        game_still_on = False
    if diagonal1:
        return game_board[0]
    elif diagonal2:
        return game_board[6]
    return


def check_if_tie():
    global game_still_on
    if "__" not in game_board:
        game_still_on = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def play_game():
    display_board()

    while game_still_on:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("This is a tie")


play_game()