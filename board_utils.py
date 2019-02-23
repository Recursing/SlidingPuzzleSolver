from functools import lru_cache


def is_inside(y, x, height, width):
    return 0 <= y < height and 0 <= x < width


@lru_cache()
def neighbours(pos, width, height):
    """ returns tuple of neighbours of position """
    y, x = divmod(pos, width)
    deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))
    return tuple(
        (y + dy) * width + x + dx
        for dy, dx in deltas
        if is_inside(y + dy, x + dx, height, width)
    )


def swap(board, start, target):
    """ returns board with start and target swapped """
    copy = list(board)
    copy[start], copy[target] = board[target], board[start]
    return tuple(copy)


def double_swap(board, start1, start2, target1, target2):
    copy = list(board)
    copy[start1], copy[start2], copy[target1], copy[target2] = (
        board[target1],
        board[target2],
        board[start1],
        board[start2],
    )
    return tuple(copy)


def rotate(board, pos1, pos2, pos3):
    """ pos1 → pos3, pos2 → pos1, pos3 → pos2 """
    copy = list(board)
    copy[pos1], copy[pos2], copy[pos3] = board[pos2], board[pos3], board[pos1]
    return tuple(copy)
