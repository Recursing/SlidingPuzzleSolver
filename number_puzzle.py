from sliding_game import SlidingGame
import board_utils


class NumberPuzzle(SlidingGame):
    def __init__(
        self,
        width=3,
        height=3,
        start_board=(8, 6, 7, 2, 5, 4, 3, 0, 1),
        goal=(1, 2, 3, 4, 5, 6, 7, 8, 0),
    ):
        super().__init__(width, height, start_board)
        self.goal = goal

    def move(self, board, spaces, space, target):
        assert board[space] == 0
        return board_utils.swap(board, target, space), (target,)

    def is_goal(self, board):
        # Accept partial goals
        return board[:len(self.goal)] == self.goal
