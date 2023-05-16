from manim import *
from random import randint
from tour import make_tour, warnsdorff_rule


def foolproof_input() -> int:
    while True:
        try:
            input_number = int(input('Enter board size: '))
        except ValueError:
            print('You did not enter an integer.\nTry again.')
            continue
        if input_number > 0:
            return input_number
        print('You must enter a positive integer.\nTry again.')


def index(board: list, n: int) -> tuple:
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == n:
                return i + 1, j + 1


class Board(Scene):
    def construct(self):
        size = foolproof_input()
        tour = make_tour(
            start=(randint(0, size - 1), randint(0, size - 1)),
            board_size=size,
            next_move_func=warnsdorff_rule
        )

        table = Table(
            [[*map(lambda x: str(x), row)] for row in tour],
            include_outer_lines=True
        )\
            .scale_to_fit_width(0.9 * config["frame_width"])\
            .scale_to_fit_height(0.9 * config["frame_height"])
        self.play(table.create())
        self.wait(0.4)
        for n in range(1, size * size + 1):
            cell = index(tour, n)
            self.play(table.add_highlighted_cell(cell, color=GREEN).animate)
            self.wait(0.4)
