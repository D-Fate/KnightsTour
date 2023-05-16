class Knight:
    def __init__(self, init_position: tuple, board_size=8):
        self.__current_position = init_position
        self.__current_index = 0
        self.__move_history = [init_position] * board_size ** 2
        self.__board_size = board_size

    @property
    def current_position(self):
        return self.__current_position

    @current_position.setter
    def current_position(self, position: tuple):
        self.__current_position = position
        self.__current_index += 1
        self.__move_history[self.__current_index] = position

    @property
    def current_index(self):
        return self.__current_index

    def get_moves(self, next_position=None):
        x, y = self.__current_position if not next_position else next_position
        candidates = [
            (x - 2, y - 1), (x - 2, y + 1), (x - 1, y - 2), (x - 1, y + 2),
            (x + 1, y - 2), (x + 1, y + 2), (x + 2, y - 1), (x + 2, y + 1)
        ]
        for move in candidates:
            if move not in self.__move_history[:self.__current_index + 1] and \
                    self.__board_size > move[0] > -1 and \
                    self.__board_size > move[1] > -1:
                yield move
