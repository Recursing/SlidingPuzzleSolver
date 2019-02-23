from collections import deque
from itertools import chain
from klotski import Klotski
from number_puzzle import NumberPuzzle


def solve(puzzle):
    """ finds a solution by simple breadth first search, and prints it """
    start_board = puzzle.start_board
    if puzzle.is_goal(start_board):
        print("Board is already solved")
        return [start_board]
    spaces = tuple(i for i, value in enumerate(start_board) if value == 0)
    to_visit = deque([])
    to_visit.append((puzzle.start_board, spaces))
    board_parents = {start_board: None}

    solution = None
    while to_visit and solution is None:
        board, spaces = to_visit.popleft()
        for new_board, new_spaces in puzzle.children(board, spaces):
            if new_board not in board_parents:
                board_parents[new_board] = board
                if puzzle.is_goal(new_board):
                    solution = new_board
                to_visit.append((new_board, new_spaces))

    solution_moves = [solution]
    last_board = solution
    while last_board != start_board:
        last_board = board_parents[last_board]
        solution_moves.append(last_board)

    solution_moves.reverse()
    return solution_moves


def print_solution(puzzle, solution, boards_per_line=5):
    for move_number in range(0, len(solution), boards_per_line):
        puzzle.pretty_print(solution[move_number : move_number + boards_per_line])
        print(move_number)

    print("Length: ", len(solution) - 1)


def solve_demo():
    red_donkey = Klotski()
    solution = solve(red_donkey)
    print("Solved Red Donkey:")
    print_solution(red_donkey, solution)

    super_century = Klotski(
        start_board=(2, 1, 1, 1, 3, 2, 6, 6, 2, 3, 6, 6, 3, 4, 5, 1, 0, 0, 4, 5)
    )
    solution = solve(super_century)
    print("\nSolved Super Century:")
    print_solution(super_century, solution)

    puzzle8 = NumberPuzzle()
    solution = solve(puzzle8)
    print("\nSolved 8-Puzzle:")
    print_solution(puzzle8, solution)

    # Sadly the full 15 puzzle is too hard to solve by simple breadth first search
    # but can find a very suboptimal solution just by solving intermediate states

    puzzle15 = NumberPuzzle(
        width=4,
        height=4,
        start_board=(15, 2, 4, 12, 5, 8, 6, 11, 1, 9, 10, 7, 3, 13, 14, 0),
        goal=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0),
    )
    full_goal = puzzle15.goal
    full_solution = [puzzle15.start_board]
    print("\nSolving 15 Puzzle")
    for i in range(1, 16):
        puzzle15.start_board = full_solution[-1]
        puzzle15.goal = full_goal[:i]
        puzzle15.pretty_print([puzzle15.start_board])
        partial_solution = solve(puzzle15)
        print("Reached: ", puzzle15.goal)
        print("Moves: ", len(partial_solution))
        full_solution.extend(partial_solution[1:])
    print("\nSolved 15-Puzzle")
    print_solution(puzzle15, full_solution)


if __name__ == "__main__":
    solve_demo()
