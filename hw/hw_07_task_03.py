from typing import List, Union


def check_win(board: List[List]) -> Union[int, str]:
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
        if board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] != "-":
            return board[each[0]]
    return 0


def tic_tac_toe_checker(board: List[List]) -> str:
    flatten_board = [val for sublist in board for val in sublist]
    res = check_win(flatten_board)
    if res != 0:
        return res + " wins!"
    elif any(x == "-" for x in flatten_board):
        return "unfinished"
    else:
        return "draw!"
