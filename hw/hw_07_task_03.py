from typing import List


def check_win(board: List[List]) -> str:
    win_coord = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for each in win_coord:
        combination = [board[i] for i in each]
        if len(set(combination)) == 1 and combination[0] != "-":
            return combination[0]
    return ""


def tic_tac_toe_checker(board: List[List]) -> str:
    flatten_board = [val for sublist in board for val in sublist]
    winner = check_win(flatten_board)
    if winner:
        return winner + " wins!"
    elif any(x == "-" for x in flatten_board):
        return "unfinished"
    else:
        return "draw!"
