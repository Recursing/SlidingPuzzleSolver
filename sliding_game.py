from functools import lru_cache
import board_utils


class SlidingGame:
    def __init__(self, width, height, start_board):
        self.width = width
        self.height = height
        self.start_board = start_board

    def move(self, board, spaces, space, target):
        raise NotImplementedError("Must specify move rules")

    def children(self, board, spaces):
        assert all(board[space] == 0 for space in spaces), "wrong spaces position"
        children_list = set()
        for space in spaces:
            for target in board_utils.neighbours(space, self.width, self.height):
                moved = self.move(board, spaces, space, target)
                if moved:
                    children_list.add(moved)
        return children_list

    def pretty_print(self, boards):
        colors = ["", "\x1b[1;30;42m"]
        ENDC = "\x1b[0m"
        print("-" * (self.width * 2))
        for line_num in range(self.height):
            lines = (
                board[line_num * self.width : (line_num + 1) * self.width]
                for board in boards
            )
            print(
                " ".join(
                    "".join(f"{colors[value != 0]}{value:>2}{ENDC}" for value in line)
                    for line in lines
                )
            )

