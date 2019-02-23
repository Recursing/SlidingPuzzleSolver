from sliding_game import SlidingGame
import board_utils


class Klotski(SlidingGame):
    def __init__(
        self,
        width=4,
        height=5,
        start_board=(2, 6, 6, 2, 3, 6, 6, 3, 2, 4, 5, 2, 3, 1, 1, 3, 1, 0, 0, 1),
        goals=(17, 18),
    ):
        super().__init__(width, height, start_board)
        self.goals = goals

    def move(self, board, spaces, space, target):
        other_space = spaces[0] if spaces[0] != space else spaces[1]
        assert board[other_space] == board[space] == 0
        cell_type = board[target]
        if cell_type == 1:  # small square
            return board_utils.swap(board, target, space), (target, other_space)

        ABOVE = -self.width
        BELOW = self.width
        LEFT = -1
        RIGHT = +1

        if cell_type == 2:  # upper part of vertical rectangle
            if target - space == BELOW:
                return (
                    board_utils.rotate(board, space, target, target + BELOW),
                    (target + BELOW, other_space),
                )
            elif other_space - space == BELOW:
                return (
                    board_utils.double_swap(
                        board, space, other_space, target, target + BELOW
                    ),
                    (target, target + BELOW),
                )
        elif cell_type == 3:  # lower part of vertical rectangle
            assert board[target + ABOVE] == 2
            if target - space == ABOVE:
                return (
                    board_utils.rotate(board, space, target, target + ABOVE),
                    (target + ABOVE, other_space),
                )
            elif other_space - space == ABOVE:
                return (
                    board_utils.double_swap(
                        board, space, other_space, target, target + ABOVE
                    ),
                    (target, target + ABOVE),
                )
        elif cell_type == 4:  # left part of horizontal rectangle
            assert board[target + RIGHT] == 5
            if target - space == RIGHT:
                return (
                    board_utils.rotate(board, space, target, target + RIGHT),
                    (target + RIGHT, other_space),
                )
            elif other_space - space == RIGHT:
                return (
                    board_utils.double_swap(
                        board, space, other_space, target, target + RIGHT
                    ),
                    (target, target + RIGHT),
                )
        elif cell_type == 5:  # right part of horizontal rectangle
            assert board[target + LEFT] == 4
            if target - space == LEFT:
                return (
                    board_utils.rotate(board, space, target, target + LEFT),
                    (target + LEFT, other_space),
                )
            elif other_space - space == LEFT:
                return (
                    board_utils.double_swap(
                        board, space, other_space, target, target + LEFT
                    ),
                    (target, target + LEFT),
                )
        elif cell_type == 6:  # any part of big square
            direction = target - space
            if (
                0 <= other_space + direction < self.width * self.height
                and board[other_space + direction] == 6
            ):
                new_board = board_utils.double_swap(
                    board,
                    space,
                    other_space,
                    space + direction * 2,
                    other_space + direction * 2,
                )
                return new_board, (space + direction * 2, other_space + direction * 2)

    def is_goal(self, board):
        return all(board[goal] == 6 for goal in self.goals)

    def pretty_print(self, boards):
        print("-" * (self.width * 2))
        ENDC = "\x1b[0m"
        colors = [
            "",
            "\x1b[0;30;41m",
            "\x1b[0;30;42m",
            "\x1b[0;30;42m",
            "\x1b[0;30;42m",
            "\x1b[0;30;42m",
            "\x1b[1;37;43m",
            "\x1b[0;30;40m",
        ]
        for line_num in range(self.height):
            lines = [
                board[line_num * self.width : (line_num + 1) * self.width]
                for board in boards
            ]
            print(
                " ".join(
                    "".join(
                        "{}{} {}".format(colors[value], value, ENDC) for value in line
                    )
                    for line in lines
                )
            )
