import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
marker = ""


def display_board(board):
    print("1 " + board[1] + "|" + board[2] + "|" + board[3])
    print("  -----")
    print("4 " + board[4] + "|" + board[5] + "|" + board[6])
    print("  -----")
    print("7 " + board[7] + "|" + board[8] + "|" + board[9])


def place_marker(board, marker):
    while True:
        position = int(input("Where you wanna put marker? 1-9: "))
        if board[position] == " ":
            board[position] = marker
            break
        else:
            print("Wrong position")

    return board


def space_check(board, position):
    if board[position] == " ":
        return False


def win_check(board, marker):
    if board[1] == marker and board[2] == marker and board[3] == marker:
        print(marker + " WINS")
        return False
    if board[4] == marker and board[5] == marker and board[6] == marker:
        print(marker + " WINS")
        return False
    if board[7] == marker and board[8] == marker and board[9] == marker:
        print(marker + " WINS")
        return False
    if board[1] == marker and board[4] == marker and board[7] == marker:
        print(marker + " WINS")
        return False
    if board[2] == marker and board[5] == marker and board[8] == marker:
        print(marker + " WINS")
        return False
    if board[3] == marker and board[6] == marker and board[9] == marker:
        print(marker + " WINS")
        return False
    if board[1] == marker and board[5] == marker and board[9] == marker:
        print(marker + " WINS")
        return False
    if board[3] == marker and board[5] == marker and board[7] == marker:
        print(marker + " WINS")
        return False
    return True


def first_player():
    randomize = random.randint(0, 1)
    if randomize == 0:
        print("X starts")
        return "X"
    else:
        print("O starts")
        return "O"


def second_player(first_player):
    if first_player == "X":
        return "O"
    else:
        return "X"


def full_board(board):
    if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[
        6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
        print("Tie!")
        return False
    else:
        return True


def game(board):
    game_on = True
    player_one = first_player()
    player_two = second_player(player_one)
    display_board(board)
    place_marker(board, player_one)
    while game_on:

        place_marker(board, player_two)
        display_board(board)
        if full_board(board) == False:
            break
        if win_check(board, player_two) == False:
            break

        place_marker(board, player_one)
        display_board(board)
        if full_board(board) == False:
            break
        if win_check(board, player_one) == False:
            break


game(board)
