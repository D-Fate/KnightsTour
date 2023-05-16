from knight import Knight
from random import choice


def make_tour(start: tuple, board_size: int, next_move_func) -> list:
    board = [[0] * board_size for _ in range(board_size)]
    board[start[0]][start[1]] = 1
    knight = Knight(start, board_size)

    while True:
        next_move = next_move_func(knight)
        if next_move is None:
            return board
        knight.current_position = next_move
        board[next_move[0]][next_move[1]] = knight.current_index + 1


def warnsdorff_rule(knight: Knight) -> tuple or None:
    moves = [*knight.get_moves()]
    move_weights = [0] * len(moves)
    min_weight = 8
    i = 0
    for move in moves:
        move_weights[i] = len([*knight.get_moves(next_position=move)])
        if move_weights[i] < min_weight:
            min_weight = move_weights[i]
        i += 1
    chosen_moves = []
    i = 0
    for weight in move_weights:
        if weight == min_weight:
            chosen_moves.append(moves[i])
        i += 1
    return choice(chosen_moves) if chosen_moves else None
